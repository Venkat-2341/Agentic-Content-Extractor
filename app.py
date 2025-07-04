import streamlit as st
from utils import process_pdf_generator

def main():
    st.title("PDF Parser")

    uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])
    
    if uploaded_file is not None:
        st.success(f"Uploaded {uploaded_file.name}")

        PDF_PATH = f"temp_{uploaded_file.name}"
        with open(PDF_PATH, "wb") as f:
            f.write(uploaded_file.getbuffer())

        # Initialize session state variable if not present
        if 'processed_text' not in st.session_state:
            st.session_state['processed_text'] = None

        if st.session_state['processed_text'] is None:
            st.subheader("Processing PDF...")

            progress_bar = st.progress(0)
            processed_text = ""
            page_placeholder = st.empty()

            for current_page, total_pages, page_text in process_pdf_generator(PDF_PATH):
                processed_text += page_text
                progress = current_page / total_pages
                progress_bar.progress(progress)
                page_placeholder.write(f"Processed page {current_page}/{total_pages}")

            st.session_state['processed_text'] = processed_text

            st.success("Processing complete!")
        else:
            processed_text = st.session_state['processed_text']
            st.info("Using cached processed text.")

        # Preview
        st.subheader("Preview of processed markdown:")
        st.write(processed_text[:500])

        # Download button
        st.download_button(
            label="Download Processed Markdown",
            data=processed_text,
            file_name="processed.md",
            mime="text/markdown"
        )

if __name__ == "__main__":
    main()
