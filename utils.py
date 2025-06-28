import fitz
import os
import base64
import io
import json
import pdfplumber
from PIL import Image
from together import Together

def get_image_caption(base64_image: base64) -> str:
    """Image captioning by using a Vision Language Model"""
    
    client = Together()
    prompt = "Give a suitable caption for the provided image"
    
    stream = client.chat.completions.create(
    model="meta-llama/Llama-Vision-Free",
    # Other vision model choices
    # Meta Llama 3.2 90B Vision Instruct Turbo $ 1.2
    # Meta Llama 3.2 11B Vision Instruct Turbo $ 0.18
    # Meta Llama Guard 3 11B Vision Turbo $ 0.18
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": prompt},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{base64_image}",
                    },
                },
            ],
        }
    ],
    stream=True,
    )
    
    caption = ""
    for chunk in stream:
        if chunk.choices and chunk.choices[0].delta:
            content = chunk.choices[0].delta.content
            caption += content
    
    return caption

def prompt_table_cleaning(table_str: str):
    messages = [
        {
            "role": "system",
            "content": "You are a Markdown formatting assistant."
        },
        {
            "role": "user",
            "content": f"""
        I have extracted a table from a PDF using OCR. It is in the form of a nested list of rows (some cells are `null` meaning continuation of above cell). Please convert this into a clean, readable markdown table.

        - If some cells are meant to span multiple rows, fill in the blanks based on context.
        - Properly handle newlines inside cells.
        - DO NOT add any explanations or extra text.
        - Just return the cleaned markdown table — no headings, no descriptions, no comments.

        Here is the table:
        {table_str}
        """
        }
        ]
    return messages

def process_table(table):

    table_str = json.dumps(table, indent=2)
    client = Together()
    response = client.chat.completions.create(
    model="meta-llama/Llama-3.3-70B-Instruct-Turbo-Free",
    messages=prompt_table_cleaning(table_str)
    )
    md_table = response.choices[0].message.content
    return md_table

def process_pdf(pdf_path: str) -> str:
    """
        Processes a PDF, extracts text, images (gets captions), and tables,
        and returns a Markdown string.
    """
    doc = fitz.open(pdf_path)
    print(f"Processing PDF: {pdf_path} with {len(doc)} pages.")
    c = 0
    final_doc = []
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        
        page_content = []
        page_content.append(f"\n## Page {page_num + 1}\n")
        
        # Extracting Text
        text = page.get_text("text")
        if text.strip():
            page_content.append("### Text\n")
            page_content.append(text.strip())
            page_content.append("\n")
            
        
        # Extracting Images and getting caption
        image_list = page.get_images(full=True)
        print(f"Page: {page_num}")
        if image_list:
            # print(f"YESS: {page_num}")
            page_content.append("### Images\n")
            
            for img in image_list:
                
                # get the XREF of the image
                xref = img[0]

                base_image = doc.extract_image(xref)
                # base_image is a dictionary with lot of info
                
                # this is the bytes of the image
                image_bytes = base_image["image"]
                
                # converting it to base 64 to make it easy to use with Together AI
                base64_image = base64.b64encode(image_bytes).decode("utf-8")
                
                # get the image extension(useful for saving the img)
                # image_ext = base_image["ext"]
                
                # Caption the image and add it to our page_content
                caption = get_image_caption(base64_image)
                page_content.append(caption)
                page_content.append("\n")

        
        # Extracting tables
        tables = page.find_tables()
        if tables.tables:
            
            page_content.append("### Table\n")
            for table in tables.tables:
                
                data = table.extract() # List[List[str]]
                md_table = process_table(data)
                
                page_content.append(md_table)
                page_content.append("\n")

        final_doc.extend(page_content)
    return final_doc

import fitz
import base64

def process_pdf_generator(pdf_path: str):
    """
    Processes a PDF page by page and yields (current_page, total_pages, page_content_str)
    """
    doc = fitz.open(pdf_path)
    total_pages = len(doc)
    
    for page_num in range(total_pages):
        page = doc.load_page(page_num)
        
        page_content = []
        page_content.append(f"\n## Page {page_num + 1}\n")
        
        # Extracting Text
        text = page.get_text("text")
        if text.strip():
            page_content.append("### Text\n")
            page_content.append(text.strip())
            page_content.append("\n")
        
        # Extracting Images and getting caption
        image_list = page.get_images(full=True)
        if image_list:
            page_content.append("### Images\n")
            for img in image_list:
                xref = img[0]
                base_image = doc.extract_image(xref)
                image_bytes = base_image["image"]
                base64_image = base64.b64encode(image_bytes).decode("utf-8")
                
                caption = get_image_caption(base64_image)
                page_content.append(caption)
                page_content.append("\n")
        
        # Extracting tables
        tables = page.find_tables()
        if tables.tables:
            page_content.append("### Table\n")
            for table in tables.tables:
                data = table.extract()  # List[List[str]]
                md_table = process_table(data)
                page_content.append(md_table)
                page_content.append("\n")
        
        # Yield processed page content
        yield page_num + 1, total_pages, '\n'.join(page_content)
