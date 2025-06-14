
[PAGE 6]
[TABLE 1]
Fieldsof Application | KeywordsforPaperSearch | TasksOfApplication |  | Numberofpapers | 
 |  |  |  | Relevantmodels usingkeywords | Selectedmodels forTaxonomy
NaturalLanguage Processing | “NaturalLanguageProcessing”, “NLP”,“Text”,“TextProcessing”, “Transformer”,“Attention”, “Self-attention”,“multi-head attention”,“Languagemodel”. | LanguageTranslation |  | 257 | 25
 |  | TextClassification&Segmentation |  |  | 
 |  | QuestionAnswering |  |  | 
 |  | TextSummarization |  |  | 
 |  | TextGeneration |  |  | 
 |  | NaturalLanguageReasoning |  |  | 
 |  | AutomatedSymbolic Reasoning |  |  | 
ComputerVision | “Transformer”,“Attention”, “Self-attention”,“Image”, “Naturalimage”,“medical image”,“Biomedical”, “health”,“Imageprocessing”, “Computervision”,“Vision”. | NaturalImage Processing | Image Classification | 197 | 27
 |  |  | Recognition& ObjectDetection |  | 
 |  |  | Image Segmentation |  | 
 |  |  | ImageGeneration |  | 
 |  | MedicalImage Processing | Image Segmentation |  | 
 |  |  | Image Classification |  | 
 |  |  | Image Translation |  | 
Multi-modal | “Transformer”,“Attention”, “Self-attention”,“multi-head attention”,“multimodal”, “multi-modality”,“text-image”, “image-text”,“video-audio- text,“text-audio”,“audio-text”, “vision-language”, “language-vision”. | Classification& Segmentation |  | 94 | 20
Continuedonnextpage |  |  |  |  | 


[PAGE 7]
[TABLE 1]
Fieldsof Application | KeywordsforPaperSearch | TasksOfApplication | Numberofpapers | 
 |  |  | Relevantmodels usingkeywords | Selectedmodels forTaxonomy
 |  | VisualQuestionAnswering |  | 
 |  | VisualCaptioning |  | 
 |  | VisualCommon-sense Reasoning |  | 
 |  | Text/Image/Video/Speech Generation |  | 
 |  | CloudTaskComputing |  | 
Audio&Speech | “Transformer”,“Attention”, “Self-attention”,“multi-head attention”,“audio”,“Speech”, “audioprocessing”,“speech processing”, | Audio&SpeechRecognition | 70 | 16
 |  | Audio&SpeechSeparation |  | 
 |  | Audio&SpeechClassification |  | 
SignalPro- cessing | “Transformer”,“Attention”, “Self-attention”,“multi-head attention”,“signal”,“signal processing”,“wireless”, “wirelesssignal”,“wireless network”,“biosignal”,“medical signal”. | WirelessnetworkSignal processing | 23 | 11
 |  | MedicalSignalProcessing |  | 


[PAGE 8]
[TABLE 1]
Approach | Fieldsof Application | Similarities | Differences
QFournier etal. (Fournier etal.,2021) | Performance /Archi- tecture | • Aclassificationofthetrans- formersissuggested,andthis classificationisbasedonatten- tionmechanismmodificationor architecturemodification | • Thisparesurveyedthedifferentalternativesofthestandard transformersthataremoreefficientintermsoftimeandmem- orycomplexities,andthesealternativesarecategorizedbyei- thermodifyingtheattentionmechanismorthenetworkarchi- tecture. Theirclassificationisbasedonthechangeinarchitec- tureorchangeinattentionmechanism,whileourclassification isdrivenbyapplicationareas.
T.Linet al. (Lin etal.,2022) | Performance /Archi- tecture | • ProposedtaxonomyofX- formerscoveringseveralfields | • ThisexistingsurveycomparedX-formersfromarchitectural modification,pre-training,andaverysmallrangeofapplication perspectives,whileoursurveydeeplyfocusesonpopulartasks undereachfieldofapplication. • Thewireless/medicalsignalprocessingandcloudcomputing tasksapplicationweremissinginthisexcitingsurvey,whileour surveycoversthesetasksandapplications.
Continuedonnextpage |  |  | 


[PAGE 9]
[TABLE 1]
Approach | Fieldsof Application | Similarities | Differences
Y.Tayet al. (Tay etal.,2023) | Performance /Archi- tecture | • Proposedataxonomyconsid- eringtheprimaryusecaseof transformermodelsinlanguage andvisiondomains. | • Thisexistingsurveycomparedthecomputationalpowerand memoryefficiencyoftransformermodels,whereasoursurvey focusesondeeplearningtasksandapplications. • Thisexcitingsurveyfocusedonlanguageandvisiondomain only,whilewecoverothertopfivefieldsoftransformerappli- cations: NLP,computervision,multi-modality,audio/speech, andsignalprocessing.
A.M.P. Bras¸oveanu etal. (Brasoveanu &Andonie, 2020) | Natural language Processing- NLP | • Explaintransformerarchitec- tureandexplainitsfeatures. | • Oursurveydescribesthetransformermodelandthesignificant models’workingprocessingforarangeoftasks. However,this existingpaperfocusedonvisualizationtechniquesusedtoex- plainthemostrecenttransformerarchitecturesandexplored twolargetoolclassestoexplaintheinnerworkingsofTrans- formers. • wecoveredfivefieldsoftransformerapplications: NLP,com- putervision,multi-modality,audio/speech,andsignalprocess- ingandthisexcitingsurveyfocusedonthemodelsforNLP only.
WGuanet al. (Wang etal., 2020a) | Natural language Processing- NLP | • Surveyanapplicationareaof transformers,whichistext summarization,whichisone oftheapplicationareascovered inoursurvey | • Theauthorsproposeatransformer-basedsummarizerthat solvestheissuesofstandardtransformersthatcannottakea longtextasaninput. Theysurveydifferentusecasesofapply- ingtransformerstodifferenttextsummarizationtasksandthey onlycovertextsummarization. noproposedtransformershave beenbuiltinoursurvey.
RKumar (Kaliyar, 2020) | Natural language Processing- NLP | • DiscussionofdifferentNLP downstreamtasksthatBERT performs. BERTiscovered inoursurveyaswellasthe differentNLPtasks | • SurveydifferenttechniquesonusingBERTasaword- embedderagainsttraditionalword-embeddingtechniques. Theirsurveyisonlyfocusedasusingtransformersasatool forembeddingtext
FAcheam- pongetal. (Acheam- pongetal., 2021) | Natural language Processing- NLP | • Surveydifferenttransformer architecturesthataccomplish theemotiondetectiontask. We dothesame,theapplicationof differenttransformerstothe sametypeiftask | • Surveytheapplicationoftransformerarchitecturetoasingle applicationareabutintoomuchdetail,whichisemotiondetec- tionfromtext-baseddata,aformofsentimentanalysisbutthe goalistoextractfine-grainedemotionfromthedata. Thetask ofsentimentanalysisiscoveredinoursurvey,butwedidn’t coverespeciallythetaskofdetectingemotionsondifferentlev- elsandnotjustasabinaryclassificationtaskasusuallydonein sentimentanalysis
Continuedonnextpage |  |  | 


[PAGE 10]
[TABLE 1]
Approach | Fieldsof Application | Similarities | Differences
RGruet- zemacheret al. (Gruet- zemacher &Paradice, 2022) | Natural language Processing- NLP | • Surveytheprogressoftrans- formersinthetext-miningap- plicationarea. Wedocover inoursurveytheprogressof transformersonawidevariety oftasks | • Tacklethedifferenttransformersonhowtheycanbeusedas textminersfororganizationsthathavehugeamountsofun- structureddataagainsttraditionalNLPtext-miningtechniques
J.Selvaet al. (Selva etal.,2023) | Computer Vision | • Thispaperisanoverviewof transformersdevelopedfor modelingimagesandvideo data | • Thissurveyfocusessolelyonimageandvideodata. Models arecomparedbasedontheirperformanceinvideoclassifica- tion,itdoesnotcoveranyotherapplications. Thepaperpro- posesataxonomyofvarioustransformermodelsbasedontheir recurrenceproperties,memorycapacities,andarchitecturalde- sign
K.S. Kalyanet al. (Subra- manyam etal., 2021a) | Natural language Processing- Medical | • Thispaperprovidesan overviewofthedeveloped transformer-basedBPLMsfor awiderangeofNLPtasks, includingNaturallanguage inference,Entityextraction, Relationextraction,Semantic textualsimilarity,Textclassi- fication,Questionanswering, andTextsummarization | • Thissurveyaddressesonlytransformer-basedbiomedicalpre- trainedlanguagemodels,whichrestrictsitsscopetothespe- cificfieldofbiomedicalnaturallanguageprocessing. Thetax- onomydoesnotdistinguishmodelsbasedonthetypeofap- plicationtheyareusedfor,butratherbasedonthedatasetof pre-training,theembeddingtype,andothercriteriasuchasthe targetedlanguage
K.Hanet al. (Han etal.,2023) | Computer Vision | • Categorizedvisiontransformer modelsbasedondifferenttasks | • Thisexistingpaperanalyzedtransformermodels’advantages anddisadvantages,andefficienttransformermethodsforthe backbonenetwork,whileoursurveycategorizestransformer modelsbasedontasksandsummarizedownstreamtasksand commonlyuseddataset. • Whileoursurveypaperclassifiedcomputervisiontasksinto twosegments: naturalimageprocessing&medicalimagepro- cessingandthenfocusedonpopularcomputervisionlikevi- sualquestionanswering,classification,segmentation,ques- tionanswering,andsoon,thenthisexistingpaperfocusedon high/mid-levelvision,low-levelvision,andvideoprocessing computervisiontasks. • Thissurveyfocusedoncomputervisiontasksonly,whilewe coveredotherfourfieldsofapplications-NLP,Multi-modal, Audio/speech,andsignalprocessingbesidescomputervision
Continuedonnextpage |  |  | 


[PAGE 11]
[TABLE 1]
Approach | Fieldsof Application | Similarities | Differences
Y.Xuet al. (Xu etal.,2022) | Computer Vision | • Thesurveycoversthefields ofcomputervisionandmulti- modalinasimilarfashionto oursurvey | • Thissurveyfocusesprimarilyonrecentadvancementsincom- putervisionbycomparingtheperformanceofdifferenttrans- formermodels. Specifically,thisstudydiscussesfourareasof research: advancesinthedesignoftheViTmodelsforimage classification,high-levelvisiontasks(suchasobjectdetection andsemanticsegmentation),low-levelvisiontasks(suchas super-resolution,andimagegeneration),andmultimodallearn- ing(suchasvisualquestionanswering(VQA),imagecaption- ing)
JLietal. (Lietal., 2023) | Computer Vision | • Comparativeanalysisoftrans- formermodelsispresented inthispaperforseveraltasks involvedinmedicalvision. Severalcriteriaareconsidered whencomparingpapers,in- cludingthetypeofdataset,the typeofinputdata,andthear- chitectureofthemodel | • Thispaperdescribesindetailseveraltransformermodelsthat havebeendevelopedformedicalimages;however,itdoesnot provideinformationregardingmedicalsignals
FShamshad etal. (Shamshad etal.,2023) | Computer Vision- medical | • Areviewofanumberoftrans- formermodelswithafocus onsometasksrelatedtomedi- calimagesanddifferentimage modalities,andadescriptionof thedatasetsusedforthesetasks | • ThispapercomparesdeeplearningmodelsstartingwithCNNs andmovinguptovisiontransformers. Inthispaper,medical imagemodalitiesandseveralmedicalcomputervisiontasks arediscussedtocomparepapersthroughthespecificationof datasetsusedandalsoprovideanoverviewofmodels’perfor- mance. Inthispaper,thecomparisonisbasedsolelyonmedical images;medicalsignalsarenotconsidered
Salman Khanet al. (Khan etal.,2022) | Computer Vision | • Aoverviewofexistingtrans- formercomputervisionmodels andclassifiedthemodelsbased onpopulartasks | • Whilethisexistingsurveypapercomparedthepopulartech- niquesintermsofarchitecturaldesignandexperimentalvalue, whileoursurveyworkedbasedonpopulartasksandapplica- tions. • Inthecomputervisionsection,weputaspecialfocusonMedi- calimagetasksbesidesnaturalimageprocessing. • Thissurveyfocusedoncomputervisiontasksonly,whilewe coveredotherfourfieldsofapplications,namelyNLP,Multi- modal,Audio/speech,andsignalprocessingbesidescomputer vision
L.Ruanet al. (Ruan& Jin,2022) | Multi- modal(NLP- CV) | • Categorizetransformervision- languagemodelsbasedontasks andsummarizedownstream tasksandcommonlyusedvideo dataset | • Thisexistingsurveyfocusedonmulti-modal(NLP-CV)tasks only,whilewecoveredotherfourfieldsofapplications-NLP, Computervision,Audio/speech,andsignalprocessingbesides multi-modal
Continuedonnextpage |  |  | 


[PAGE 12]
[TABLE 1]
Approach | Fieldsof Application | Similarities | Differences
AShinet al. (Shin etal.,2022) | Multi-modal (Perfor- mance /Archi- tecture) | • Theysurveytransformersfor multi-modaltasks,whichwe doalsoincludeinourdifferent applicationtasks | • Coveronlyoneapplicationareaindetail,whichismultimodal visual-linguistictasks


[PAGE 15]
[TABLE 1]
Transformer Models | TaskAc- complished | Year | Architecture (Encoder/ Decoder) | Pre- trained (Yes/NO) | Pre-training Dataset | Dataset(Fine-tuning, Training,Testing)
Transformer- 2017 (Vaswani etal.,2017) | Language Translation | 2017 | Encoder& Decoder | No | NA | WMT2014English- German,WMT2014 English-French
XLM (Conneau &Lample, 2019) | Translationand Classification formultiple language | 2019 | Encoder& Decoder | Yes | WMT’16,WMT’14 English-French, WMT’16 (English-German, English-Romanian, Romanian-English) | Wikipediaof16XNLIlan- guages(English,French,Span- ish,Russian,Arabic,Chinese, Hindi,German,Greek,Bul- garian,Turkish,Vietnamese, Thai,Urdu,Swahili,Japanese)
BART(Lewis etal.,2020) | Language Translation, Sentence Reconstruction, Comprehension, textGeneration | 2019 | Encoder& Decoder | Yes | Corruptingdocu- ments,1Msteps onacombina- tionofbooksand Wikipediadata, news,stories,and webtext(Training) | SQuAD,MNLI,ELI5, XSum,ConvAI2,CNN/DM, CNN/DailyMail,WMT16 Romanian-English,augmented withback-translationdata fromSennrichetal. (2016).
Switch Transformer (Fedus etal.,2021) | Language understanding task-Translation, question answering, Classification, andsoon. | 2021 | Encoder& Decoder | Yes | C4(ColossalClean CrawledCorpus) | GLUEandSuperGLUE benchmarks,CNNDM,BBC XSum,andSQuADdatasets, ARCReasoningChallenge,3 closed-bookquestionan- sweringdatasets(Natural Questions,WebQuestions, andTriviaQA),Wino- grandeSchemaChallenge, AdversarialNLIBenchmark


[PAGE 16]
[TABLE 1]
Transformer Models | TaskAc- complished | Year | Architecture (Encoder/ Decoder) | Pre- trained (Yes/NO) | Pre-training Dataset | Dataset(Fine-tuning, Training,Testing)
GPT& variants (Radford etal.,2018; 2019,Brown etal.,2020) | Textclassifica- tion,Question answering, textualentail- ment,semantic similarity | 2018 | Decoder | Yes | Bookcorpus | SNLI,MNLI,QNLI,Sc- iTail,RTE,RACE,CNN, SQuaD,MRPC,QQP, STS-B,SST2&CoLA
XLM (Conneau &Lample, 2019) | Translationand Classification formultiple language | 2019 | Encoder& Decoder | Yes | WMT’16,WMT’14 English-French, WMT’16 (English-German, English-Romanian, Romanian-English) | Wikipediaof16XNLIlan- guages(English,French,Span- ish,Russian,Arabic,Chinese, Hindi,German,Greek,Bul- garian,Turkish,Vietnamese, Thai,Urdu,Swahili,Japanese)
T5(Raffel etal.,2020) | Textsummariza- tion,Question answering,text classification | 2020 | Encoder& Decoder | Yes | C4(ColossalClean CrawledCorpus) | GLUEandSuperGLUE benchmarks,CNN/Daily Mailabstractivesumma- rization,SQuADquestion answering,WMTEn- glishtoGerman,French, andRomaniantranslation
Charformer (Tayetal., 2022) | Classification task,toxicity detection, andsoon. | 2022 | Encoder& Decoder | Yes | Thesamedatasets usedinT5model- C4(ColossalClean CrawledCorpus) | GLUEIMDb,AGNews,(Maas etal.,2011),(Zhangetal., 2015),CivilComments, WikipediaComments, TyDiQA-GoldP,XQuAD, MLQA,XNLI,PAWS-X..
Continuedonnextpage |  |  |  |  |  | 


[PAGE 17]
[TABLE 1]
Transformer Models | TaskAc- complished | Year | Architecture (Encoder/ Decoder) | Pre- trained (Yes/NO) | Pre-training Dataset | Dataset(Fine-tuning, Training,Testing)
Switch Transformer (Fedus etal.,2021) | Language understanding task-Translation, question answering, Classification, andsoon. | 2021 | Encoder& Decoder | Yes | C4(ColossalClean CrawledCorpus) | GLUEandSuperGLUE benchmarks,CNNDM,BBC XSumandSQuADdatasets, ARCReasoningChallenge,3 closed-bookquestionan- sweringdatasets(Natural Questions,WebQuestions, andTriviaQA),Wino- grandeSchemaChallenge, AdversarialNLIBenchmark

[TABLE 2]
Transformer Models | TaskAc- complished | Year | Architecture (Encoder/ Decoder) | Pre- trained (Yes/NO) | Pre-training Dataset | Dataset(Fine-tuning, Training,Testing)
BERT (Devlin etal.,2019) | Question answering, Sentence Prediction, language understanding | 2018 | Encoder | Yes | BookCorpus, EnglishWikipedia | SQuADv1.1,SQuAD v2.0,SWAG,QNLI,MNLI
ELECTRA (Clarketal., 2020a) | Language understanding tasks-Question answering andsoon | 2020 | Encoder | Yes | Wikipedia, BooksCorpus, ClueWeb,Common- Crawl,Gigaword | SQuAD1.1, SQuAD2.0,GLUE
Continuedonnextpage |  |  |  |  |  | 


[PAGE 18]
[TABLE 1]
Transformer Models | TaskAc- complished | Year | Architecture (Encoder/ Decoder) | Pre- trained (Yes/NO) | Pre-training Dataset | Dataset(Fine-tuning, Training,Testing)
GPT& variants (Radford etal.,2018; 2019,Brown etal.,2020) | Textclassifica- tion,Question answering, textualentail- ment,semantic similarity | 2018 | Decoder | Yes | Bookcorpus | SNLI,MNLI,QNLI,Sc- iTail,RTE,RACE,CNN, SQuaD,MRPC,QQP, STS-B,SST2&CoLA
Switch Transformer (Fedus etal.,2021) | Language understanding task-Translation, question answering, Classification, andsoon. | 2021 | Encoder& Decoder | Yes | C4(ColossalClean CrawledCorpus) | GLUEandSuperGLUE benchmarks,CNNDM,BBC XSum,andSQuADdatasets, ARCReasoningChallenge,3 closed-bookquestionan- sweringdatasets(Natural Questions,WebQuestions, andTriviaQA),Wino- grandeSchemaChallenge, AdversarialNLIBenchmark
T5(Raffel etal.,2020) | Textsummariza- tion,Question answering,text classification | 2020 | Encoder& Decoder | Yes | C4(ColossalClean CrawledCorpus) | GLUEandSuperGLUE benchmarks,CNN/Daily Mailabstractivesumma- rization,SQuADquestion answering,WMTEn- glishtoGerman,French, andRomaniantranslation
InstructGPT (Ouyang etal.,2022) | TextGeneration, Question Answering, summarization, andsoon. | 2022 | Decoder | Yes | Basedonthe pre-training modelGPT-3 | SFTdataset,RMdataset,PPO dataset,adatasetofprompts andcompletionsWinogender, CrowS-Pairs,RealToxicity Prompts,TruthfulQA,DROP, QuAC,SquadV2,Hellaswag, SST,RTEandWSC,WMT 15Fr! En,CNN/DailyMail Summarization,RedditTLDR Summarizationdatasets.


[PAGE 19]
[TABLE 1]
Transformer Models | TaskAc- complished | Year | Architecture (Encoder/ Decoder) | Pre- trained (Yes/NO) | Pre-training Dataset | Dataset(Fine-tuning, Training,Testing)
GPT& variants (Radford etal.,2018; 2019,Brown etal.,2020) | Textclassifica- tion,Question answering, textualentail- ment,semantic similarity | 2018 | Decoder | Yes | Bookcorpus | SNLI,MNLI,QNLI,Sc- iTail,RTE,RACE,CNN, SQuaD,MRPC,QQP, STS-B,SST2&CoLA
PEGASUS (Zhang etal.,2020a) | Textsum- marization | 2020 | Encoder& Decoder | Yes | C4,HugeNews | XSum,CNN/DailyMail, NEWSROOM,Multi-News, Gigaword,arXiv,PubMed, BIGPATENT,WikiHow, RedditTIFU,AESLC,BillSum
Switch Transformer (Fedus etal.,2021) | Language understanding task-Translation, question answering, Classification, andsoon. | 2021 | Encoder& Decoder | Yes | C4(ColossalClean CrawledCorpus) | GLUEandSuperGLUE benchmarks,CNNDM,BBC XSum,andSQuADdatasets, ARCReasoningChallenge,3 closed-bookquestionan- sweringdatasets(Natural Questions,WebQuestions, andTriviaQA),Wino- grandeSchemaChallenge, AdversarialNLIBenchmark
T5(Raffel etal.,2020) | Textsummariza- tion,Question answering,text classification | 2020 | Encoder& Decoder | Yes | C4(ColossalClean CrawledCorpus) | GLUEandSuperGLUE benchmarks,CNN/Daily Mailabstractivesumma- rization,SQuADquestion answering,WMTEn- glishtoGerman,French, andRomaniantranslation
InstructGPT (Ouyang etal.,2022) | TextGeneration, Question Answering, summarization, andsoon. | 2022 | Decoder | Yes | Basedonthe pre-training modelGPT-3 | SFTdataset,RMdataset,PPO dataset,adatasetofprompts andcompletionsWinogender, CrowS-Pairs,RealToxicity Prompts,TruthfulQA,DROP, QuAC,SquadV2,Hellaswag, SST,RTE,andWSC,WMT 15Fr! En,CNN/DailyMail Summarization,RedditTLDR Summarizationdatasets.
Continuedonnextpage |  |  |  |  |  | 


[PAGE 20]
[TABLE 1]
Transformer Models | TaskAc- complished | Year | Architecture (Encoder/ Decoder) | Pre- trained (Yes/NO) | Pre-training Dataset | Dataset(Fine-tuning, Training,Testing)

[TABLE 2]
Transformer Models | TaskAc- complished | Year | Architecture (Encoder/ Decoder) | Pre- trained (Yes/NO) | Pre-training Dataset | Dataset(Fine-tuning, Training,Testing)
CTRL (Keskar etal.,2019) | TextGeneration | 2019 | Encoder& Decoder | Yes | ProjectGutenberg, subreddits,News Data,Amazon Review,open WebText,WMT Translationdate, question-answer pairs,MRQA | MultilingualWikipedia andOpenWebText.
BART(Lewis etal.,2020) | Language Translation, Sentence Reconstruction, Comprehension, textGeneration | 2019 | Encoder& Decoder | Yes | Corruptingdocu- ments,1Msteps onacombina- tionofbooksand Wikipediadata, news,stories,and webtext(Training) | SQuAD,MNLI,ELI5, XSum,ConvAI2,CNN/DM, CNN/DailyMail,WMT16 Romanian-English,augmented withback-translationdata fromSennrichetal. (2016).
ProphetNET (Qietal., 2020) | TextPrediction | 2020 | Encoder& Decoder | Yes | Bookcorpus,English Wikipedianews, books,stories, andwebtext | CNN/dailymail,Giga-word Corpus,SQuADdataset.
Continuedonnextpage |  |  |  |  |  | 


[PAGE 21]
[TABLE 1]
Transformer Models | TaskAc- complished | Year | Architecture (Encoder/ Decoder) | Pre- trained (Yes/NO) | Pre-training Dataset | Dataset(Fine-tuning, Training,Testing)
InstructGPT (Ouyang etal.,2022) | TextGeneration, Question Answering, summarization andsoon. | 2022 | Decoder | Yes | Basedonthe pre-training modelGPT-3 | SFTdataset,RMdataset,PPO dataset,datasetofprompts andcompletionsWinogender, CrowS-Pairs,RealToxicity Prompts,TruthfulQA,DROP ,QuAC,SquadV2,Hellaswag ,SST,RTEandWSC,WMT 15Fr! En,CNN/DailyMail Summarization,RedditTLDR Summarizationdatasets.

[TABLE 2]
Transformer Models | TaskAc- complished | Year | Architecture (Encoder/ Decoder) | Pre- trained (Yes/NO) | Pre-training Dataset | Dataset(Fine- tuning,Train- ing,Testing)
(Clarketal.,2020) (Clarketal.,2020b) | BinaryClas- sification | 2020 | RoBERTa (Encoder) | Yes | RACE | RuleTaker
(Richardsonetal., 2022)(Richardson &Sabharwal,2022) | BinaryClas- sification | 2022 | RoBERTa Large(Encoder) | Yes | RACE | Hard-RuleTaker
(Sahaetal.,2020) (Sahaetal.,2020) | BinaryClassifi- cation,Sequence Generation | 2020 | PRover [RoBERTa- based](Encoder) | No | NA | RuleTaker
(Sinhaetal.,2019) (Sinhaetal.,2019) | Sequence Generation | 2019 | BERT(Encoder) | No | NA | CLUTRR


[PAGE 22]
[TABLE 1]
Transformer Models | TaskAc- complished | Year | Architecture (Encoder/ Decoder) | Pre- trained (Yes/NO) | Pre-training Dataset | Dataset(Fine- tuning,Train- ing,Testing)
(Piccoetal.,2021) (Piccoetal.,2021) | BinaryClas- sification | 2021 | BERT-Based (Encoder) | Yes | RACE | RuleTaker


[PAGE 23]
[TABLE 1]
Transformer Models | TaskAc- complished | Year | Architecture (Encoder/ Decoder) | Pre- trained (Yes/NO) | Pre-training Dataset | Dataset(Fine- tuning,Train- ing,Testing)
(Shietal.,2022) (Shietal.,2022b) | BinaryClas- sification | 2022 | SATFormer (Encoder/ Decoder) | No | NA | Synthetic
(Shietal.,2021) (Shietal.,2021) | BinaryClas- sification | 2021 | TRSAT(Encoder /Decoder) | No | NA | Synthetic,SATLIB
(Hahnetal.,2021) (Hahnetal.,2021) | Sequence Generation | 2021 | Transformer (Encoder/ Decoder) | No | NA | Synthetic
(Poluetal, 2020)(Polu& Sutskever,2020) | Sequence Generation | 2020 | GPT-f(Decoder) | Yes | CommonCrawl, Github, arXiv, WebMath | set.mm


[PAGE 24]
[TABLE 1]
Transformer Models | TaskAc- complished | Year | Architecture (Encoder/ Decoder) | Pre- trained (Yes/NO) | Pre-training Dataset | Dataset(Fine-tuning, Training,Testing)
VIT(Doso- vitskiy etal.,2021) | Imageclassifi- cation,image recognition | 2021 | Encoder | Yes | JFT-300M, ILSVRC-2012 ImageNet, ImageNet-21k | ImageNet-RL,CIFAR- 10/100,OxfordFlowers-102, Oxford-IIITPets,VTAB
ViTVariants (d’Ascoli etal.,2021, Ahmed etal.,2021, Touvron etal.,2021, Arnab etal.,2021) | Imageclas- sification | 2020- 2021 | Encoder | Yes | ConViT:ImageNet (BasedonDeiT) SiT:STL10, CUB200,CIFAR10, CIFAR100, ImageNet-1K, PascalVOC, MS-COCO,Visual- Genome DEIT: ImageNet. ViViT: ImageNet,JFT | ConViT:ImageNet,CIFAR100 SiT:CIFAR-10,CIFAR-100, STL-10,CUB200,ImageNet- 1K,PascalVOC,MS-COCO, Visual-Genome. DEIT: ImageNet,iNaturalist2018, iNaturalist2019,Flowers-102, StanfordCars,CIFAR-100, CIFAR-10. ViViT:LargerJFT, Kinetics,EpicKitchens-100, MomentsinTime,SSv2.
BEIT(Bao etal.,2022) | Imageclas- sification& segmentation | 2021 | Encoder | Yes | ImageNet-1K, ImageNet-22k | ILSVRC-2012ImageNet, ADE20K,CIFAR-100
IBOT(Zhou etal.,2021b) | Imageclas- sification, segmentation, objectdetection &recognition | 2022 | Encoder | Yes | ImageNet-1K,ViT- L/16,ImageNet-22K | COCO,ADE20K
Conformer (Pengetal., 2021) | Imagerecog- nition&object detection, Classification | 2021 | Encoder | Not mentioned inpaper | N/A | LibriSpeech


[PAGE 25]
[TABLE 1]
Transformer Models | TaskAc- complished | Year | Architecture (Encoder/ Decoder) | Pre- trained (Yes/NO) | Pre-training Dataset | Dataset(Fine-tuning, Training,Testing)
VIT(Doso- vitskiy etal.,2021) | Imageclassifi- cation,image recognition | 2021 | Encoder | Yes | JFT-300M, ILSVRC-2012 ImageNet, ImageNet-21k | ImageNet-RL,CIFAR- 10/100,OxfordFlowers-102, Oxford-IIITPets,VTAB
Conformer (Pengetal., 2021) | Imagerecog- nition&object detection, classification | 2021 | Encoder | Not mentioned inpaper | N/A | LibriSpeech
LoFTR(Sun etal.,2021a) | Imagefeature matching &visual localization | 2021 | Encoder& Decoder | No | NA | MegaDepth,ScanNet HPatches,ScanNet, MegaDepth,VisLoc benchmark(theAachen- Day-Night,InLoc)
CMT(Guo etal.,2022a) | Imagerecogni- tion,detection &segmentation | 2022 | Encoder | No | NA | ImageNet,CIFAR10, CIFAR100,Flowers,Stand- fordcars,Oxford-IIIT pets,COCOval2017
Transformer in Transformer- TNT(Han etal.,2021) | Image recognition | 2021 | Encoder& Decoder | Yes | ImageNet ILSVRC2012 | COCO2017,ADE20K, Oxford102Flowers,Oxford- IIITPets,iNaturalist2019, CIFAR-10,CIFAR-100
SWIN(Liu etal.,2021) | Objectdetection andsegmentation | 2021 | Encoder | Yes | ImageNet-22k | ImageNet-1k,COCO 2017,ADE20K
DETR (Carion etal.,2020) | Objectdetection &prediction | 2020 | Encoder& Decoder | Yes | ImageNetpretrained backboneResNet-50 | COCO2017,panoptic segmentationdatasets
Continuedonnextpage |  |  |  |  |  | 


[PAGE 26]
[TABLE 1]
Transformer Models | TaskAc- complished | Year | Architecture (Encoder/ Decoder) | Pre- trained (Yes/NO) | Pre-training Dataset | Dataset(Fine-tuning, Training,Testing)
HOTR(Kim etal.,2021a) | Human-object interaction detection | 2021 | Encoder& Decoder | Yes | MS-COCO | V-COCOHICO-DET

[TABLE 2]
Transformer Models | TaskAc- complished | Year | Architecture (Encoder/ Decoder) | Pre- trained (Yes/NO) | Pre-training Dataset | Dataset(Fine-tuning, Training,Testing)
SWIN(Liu etal.,2021) | Objectdetection andsegmentation | 2021 | Encoder | Yes | ImageNet-22k | ImageNet-1k,COCO 2017,ADE20K
CMT(Guo etal.,2022a) | Imagerecogni- tion,detection &segmentation | 2022 | Encoder | No | NA | ImageNet,CIFAR10, CIFAR100,Flowers,Stand- fordcars,Oxford-IIIT pets,COCOval2017
Continuedonnextpage |  |  |  |  |  | 


[PAGE 27]
[TABLE 1]
Transformer Models | TaskAc- complished | Year | Architecture (Encoder/ Decoder) | Pre- trained (Yes/NO) | Pre-training Dataset | Dataset(Fine-tuning, Training,Testing)
SETR(Zheng etal.,2021) | Imageseg- mentation | 2020 | Encoder& Decoder | Yes | ImageNet-1k, pre-trainedweights providedby ViTorDeiT | ADE20K,Pascal Context,CityScapes
IBOT(Zhou etal.,2021b) | Imageclas- sification, segmentation, objectdetection &recognition | 2022 | Encoder | Yes | ImageNet-1K,ViT- L/16ImageNet-22K | COCO,ADE20K

[TABLE 2]
Transformer Models | TaskAc- complished | Year | Architecture (Encoder/ Decoder) | Pre- trained (Yes/NO) | Pre-training Dataset | Dataset(Fine-tuning, Training,Testing)
ImageTransformer (Parmaretal.,2018) | ImageGen- eration | 2018 | Encoder& Decoder | Not mentioned | N/A | ImageNet,CIFAR-10,CelebA
I-GPT(Chen etal.,2020b) | ImageGen- eration | 2020 | Decoder | Yes | BooksCorpus dataset, 1BWord Benchmark | SNLI,MultiNLI,Question NLI,RTE,SciTail,RACE, StoryCloze,MSRParaphrase Corpus,QuoraQuestionPairs, STSBenchmark,Stanford SentimentTreebank-2,CoLA
VideoGPT(Yan etal.,2021) | VideoGeneration | 2021 | Decoder | No | NA | BAIRRobotNet,Mov- ingMNIST,ViZDoom, UCF-101,TumblrGIF


[PAGE 28]
[TABLE 1]
Transformer Name | Fieldof application | Year | Fully Transformer Architecture | Image type | Transformer Task | Dataset
FTN(He etal.,2022) | Skinlesion | 2022 | YES | 2D | Imageseg- mentation/ classification | ISIC2018dataset
RAT-Net(Zhu etal.,2022) | Oncology (breastcancer) | 2022 | NO | 3D ultrasound | Imageseg- mentation | adatasetof256subjects(330 AutomaticBreastUltrasound imagesforeachpatient)
nnFormer (Zhouetal., 2021a) | Braintumor multi-organ cardiacdiagnosis | 2022 | YES | 3D | Imageseg- mentation | MedicalSegmentationDe- cathlon(MSD),Synapse multiorgansegmentation, AutomaticCardiacDiag- nosisChallenge(ACDC)
TransConver (Liang etal.,2022) | Braintumor | 2022 | NO | 2D/3D | ImageSeg- mentation | MICCAIBraTS2019, MICCAIBraTS2018
SwinBTS (Jiangetal., 2022b) | Braintumor | 2022 | NO | 3D | ImageSeg- mentation | BraTS2019,BraTS 2020,BraTS2021
MTPA Unet (Jiangetal., 2022a) | Retinalvessel | 2022 | NO | 2D | Imageseg- mentation | DRIVE,CHASEDB1, andSTAREDatasets
Continuedonnextpage |  |  |  |  |  | 


[PAGE 29]
[TABLE 1]
Transformer Name | Fieldof application | Year | Fully Transformer Architecture | Image type | Transformer Task | Dataset
Dilated Transformer (Shenetal., 2022b) | Oncology (BreastCancer) | 2022 | NO | 2D ultrasound | Imageseg- mentation | 2smallbreastultra- soundimagedatasets
TFNet(Wang etal.,2021b) | Oncology (Breastlesion) | 2022 | NO | 2D ultrasound | ImageSeg- mentation | BUSIDatasetDDTIDataset
ChestL- Transformer (Guetal., 2022) | Chestradiograph /Thoracic diseases | 2022 | NO | 2D | ImageClas- sification/ Segmentation | SIIM-ACRPneumoth- oraxSegmentation datasetcontains12,047


[PAGE 30]
[TABLE 1]
Transformer Name | Fieldof application | Year | Fully Transformer Architecture | Image type | Transformer Task | Dataset
CCT-based Model(Islam etal.,2022) | MalariaDisease | 2022 | NO | 2D images | ImageClas- sification | NationalLibraryof Medicinemalariadataset
ChestL- Transformer (Guetal., 2022) | Chestradiograph /Thoracic diseases | 2022 | NO | 2D | ImageClas- sification/ Segmentation | SIIM-ACRPneumoth- oraxSegmentation datasetcontains12,047


[PAGE 31]
[TABLE 1]
Transformer Name | Fieldof application | Year | Fully Transformer Architecture | Image type | Transformer Task | Dataset
MMTrans (Yanetal., 2022b) | Magnetic resonance imaging(MRI) | 2022 | NO | 2D | Medicalimage- to-image translation | BraTs2018,fastMRI,The clinicalbrainMRIdataset
TransCBCT (Chenetal., 2022c) | Oncology (prostateCancer) | 2022 | NO | 2D | Image Translation | 91patientswith prostatecancer


[PAGE 32]
[TABLE 1]
Transformer Models | Processed Data type(i/o) | TaskAc- complished | Year | Architecture (Encoder/ Decoder) | Pre- trained (Yes/NO) | Pre-training Dataset | Dataset(Fine-tuning, Training,Testing)
BERT- Verients (Huangetal., 2020,Tan &Bansal, 2019,Lu etal.,2019, Suetal., 2020,Chen etal.,2020c) | Textand Image | Question Answering, Commonsense reasoning | 2019- 2020 | Encoder | Yes | Pixel-BERT: MS-COCO, VisualGenome LX-MERT:MS COCO,Visual Genome,VQA v2.0,GQA,VG- QA ViLBERT: VisualGenome, COCO VL- BERT:Concep- tualCaptions, BooksCor- pus,English Wikipedia Uniter: COCO, VG,CC,SBU | Pixel-BERT:VQA2.0 NLVR2,Flickr30KMS- COCO LX-MERT: VQA,GQA,NLVR ViLBERT:Con- ceptualCaptions, Flickr30k VL-BERT: VCRdataset,Re- fCOCOUniter: COCO,Flickr30K, VG,CC,SBU
VIOLET(Fu etal.,2021) | Video andText | VideoQuestion Answering, Text-to-video retrieval, Visual-Text Matching | 2022 | Encoder | Yes | Conceptual Captions-3M, WebVid- 2.5M,YT- Temporal-180M | MSRVTT,DiDeMo, YouCook2,LSMDC, TGIF-Action,TGI- Transition,TGIF- Frame,MSRVTT- MC,MSRVTT-QA, MSVD-QA,LSMDC- MC,LSMDC-FiB
GIT(Wang etal.,2022a) | Image andText | Image Classification, Image/video captioning, Question answering | 2022 | Encoder& Decoder | Yes | combinationof COCO,SBU, CC3M,VG, GITL,ALT200M andCC12M | Karpathysplit- COCO,Flickr30K, nocaps,TextCaps, VizWiz-Captions, CUTE,TextOCR
SIMVLM (Wangetal., 2022d) | Image andText | Visual Question answering, image captioning | 2022 | Encoder& Decoder | Yes | ALIGN& ColossalClean CrawledCorpus (C4)datasets | SNLI-VE,SNLI, MNLI,Multi30k, 10%ALIGN,CC-3M
BLIP(Li etal.,2022) | Image, Video andText | Question Answering, Image Captioning, image-text retrieval | 2022 | Encoder& Decoder | Yes | Bootstrapped dataset- COCO,VG, SBU,CC3M, CC12M,LAION | COCO,Flickr30K, NoCaps,MSRVTT


[PAGE 33]
[TABLE 1]
Transformer Models | Processed Data type(i/o) | TaskAc- complished | Year | Architecture (Encoder/ Decoder) | Pre- trained (Yes/NO) | Pre-training Dataset | Dataset(Fine-tuning, Training,Testing)
CLIP (Radford etal.,2021) | Image andText | image Classification | 2021 | Encoder | Yes | Pre-training datasetfrom internetforCLIP | ImageNet,ImageNet V2,ImageNetRendi- tion,ObjectNet,Ima- geNetSketch,ImageNet Adversarial30datasets
VATT (Akbari etal.,2021) | Video, Audio andText | Audioevent classification, Image classification, Videoaction recognition, Text-To-Video retrieval | 2021 | Encoder | Yes | AudioSet, HowTo100M | UCF10,HMDB5, Kinetics-400,Kinetics- 600,MomentsinTime, ESC50,AudioSet, YouCook2,MSR- VTT,ImageNet
Continuedonnextpage |  |  |  |  |  |  | 


[PAGE 34]
[TABLE 1]
Transformer Models | Processed Data type(i/o) | TaskAc- complished | Year | Architecture (Encoder/ Decoder) | Pre- trained (Yes/NO) | Pre-training Dataset | Dataset(Fine-tuning, Training,Testing)
Unicoder-VL (Lietal., 2020a) | Image andText | Object Classification, Visual- linguistic Matching, visual commonsense reasoning, image-text retrieval | 2020 | Encoder | Yes | Conceptual Captions-3M, SBUCaptions | MSCOCO,Flickr30K
ViLT(Kim etal.,2021b) | Image andText | Visual Question Answering, Imagetext matching, Natural Language forVisual Reasoning | 2021 | Encoder | Yes | MS- COCO,Visual Genome,SBU Captions,Google Conceptual Captions | VQA2.0,NLVR2, MSCOCO,Flickr30K
MBT (Nagrani etal.,2021) | Audioand Visual | Audio-visual classification | 2022 | Encoder | Yes | VGGSoun, Kinetics400 andAS-500K, VGGSound | Audioset-miniand VGGSound,Moments InTime,Kinetics
ALIGN(Jia etal.,2021) | Image andText | Visual Classification | 2021 | Encoder | Yes | ALIGNtraining data,0% randomly sampledALIGN trainingdata, andCC-3M | ConceptualCaptions- CC,Flickr30K, MSCOCO, ILSVRC-2012
Florence (Yuan etal.,2021) | Image andText | Classification, imagecaption, visualaction recognition, Text-visual &visual-text retrieval | 2021 | Encoder | Yes | FLD-900M, ImageNet(Swin transformer &CLIP) | Web-scalebydata curation,UniCL, ImageNet,COCO, Kinetics-600,Flickr30k, MSCOCO,SR-VTT
GIT(Wang etal.,2022a) | Image andText | Image Classification, Image/video captioning, Question answering | 2022 | Encoder& Decoder | Yes | combinationof COCO,SBU, CC3M,VG, GITL,ALT200M andCC12M | Karpathysplit- COCO,Flickr30K, nocaps,TextCaps, VizWiz-Captions, CUTE,TextOCR


[PAGE 35]
[TABLE 1]
Transformer Models | Processed Data type(i/o) | TaskAc- complished | Year | Architecture (Encoder/ Decoder) | Pre- trained (Yes/NO) | Pre-training Dataset | Dataset(Fine-tuning, Training,Testing)
BLIP(Li etal.,2022) | Image, Video andText | Image Captioning, Question Answering, image-text retrieval | 2022 | Encoder& Decoder | Yes | Bootstrapped dataset- COCO,VG, SBU,CC3M, CC12M,LAION | COCO,Flickr30K, NoCaps,MSRVTT
SIMVLM (Wangetal., 2022d) | Image andText | Image captioning, Visual Question answering | 2022 | Encoder& Decoder | Yes | ALIGN& ColossalClean CrawledCorpus (C4)datasets | SNLI-VE,SNLI, MNLI,Multi30k, 10%ALIGN,CC-3M
Florence (Yuan etal.,2021) | Image andText | Classification, imagecaption, visualaction recognition, Text-visual &visual-text retrieval | 2021 | Encoder | Yes | FLD-900M, ImageNet(Swin transformer &CLIP) | Web-scalebydata curation,UniCL, ImageNet,COCO, Kinetics-600,Flickr30k, MSCOCO,SR-VTT
GIT(Wang etal.,2022a) | Image andText | Image Classification, Image/video captioning, Question answering | 2022 | Encoder& Decoder | Yes | combinationof COCO,SBU, CC3M,VG, GITL,ALT200M andCC12M | Karpathysplit- COCO,Flickr30K, nocaps,TextCaps, VizWiz-Captions, CUTE,TextOCR


[PAGE 36]
[TABLE 1]
Transformer Models | Processed Data type(i/o) | TaskAc- complished | Year | Architecture (Encoder/ Decoder) | Pre- trained (Yes/NO) | Pre-trainingDataset | Dataset(Fine-tuning, Training,Testing)
BERT- Verients (Huangetal., 2020,Tan &Bansal, 2019,Lu etal.,2019, Suetal., 2020,Chen etal.,2020c) | Textand Image | Question Answering, Common sense reasoning | 2019- 2020 | Encoder | Yes | Pixel-BERT:MS- COCO,VisualGenome LX-MERT:MS COCO,Visual Genome,VQA v2.0,GQA,VG-QA ViLBERT:Visual Genome,COCO VL-BERT:Con- ceptualCaptions, BooksCorpus,English WikipediaUniter: COCO,VG,CC,SBU | Pixel-BERT: VQA2.0NLVR2, Flickr30KMS- COCO LX-MERT: VQA,GQA,NLVR ViLBERT:Con- ceptualCaptions, Flickr30k VL-BERT: VCRdataset,Re- fCOCOUniter: COCO,Flickr30K, VG,CC,SBU
ViLT(Kim etal.,2021b) | Image andText | Visual Question Answering, Imagetext matching, Natural Language forVisual Reasoning | 2021 | Encoder | Yes | MS-COCO,Visual Genome,SBU Captions,Google ConceptualCaptions | VQA2.0,NLVR2, MSCOCO,Flickr30K
Unicode-VL (Lietal., 2020a) | Image andText | ObjectClas- sification, Visual- linguistic Matching, visualcom- monsense reasoning, image-text retrieval | 2020 | Encoder | Yes | ConceptualCaptions- 3M,SBUCaptions | MSCOCO,Flickr30K
Continuedonnextpage |  |  |  |  |  |  | 


[PAGE 37]
[TABLE 1]
Transformer Models | Processed Data type (i/o) | TaskAc- complished | Year | Architecture (Encoder/ Decoder) | Pre- trained (Yes/NO) | Pre-trainingDataset | Dataset(Fine-tuning, Training,Testing)

[TABLE 2]
Transformer Models | Processed Data type(i/o) | TaskAc- complished | Year | Architecture (Encoder/ Decoder) | Pre- trained (Yes/NO) | Pre-training Dataset | Dataset(Fine-tuning, Training,Testing)
DALL-E (Ramesh etal.,2021) | Image andText | Image Generation fromtext | 2021 | Encoder& Decoder | Yes | Notdisclosed | ConceptualCaptions(MS- COCOextension),Wikipedia (text-imagepairs),and YFCC100M(filteredsubset)
GLIDE (Nichol etal.,2022) | Image andText | Image generation& editfromtext | 2021 | Encoder& Decoder | No | NA | MS-COCO,ViT-BCLIP (noised),CLIPand DALL-Efiltereddatasets
Chimera(Li &Hoefler, 2021) | Audio andText | Text generation fromspeech | 2021 | Encoder& Decoder | Yes | ALIGN& MT-Dataset | MuST-C,Augmented LibriSpeechDataset(En-Fr), MachineTranslationDatasets (WMT2016,WMT2014, OPUS100,OpenSubtitles)
CogView (Dingetal., 2021) | Image andText | Classification, Image generation fromtext | 2021 | Decoder | Yes | VQ-VAE | MSCOCO,Wudao Corpora-extensiondataset.


[PAGE 38]
[TABLE 1]
Transformer Models | Processed Data type(i/o) | TaskAc- complished | Year | Architecture (Encoder/ Decoder) | Pre- trained (Yes/NO) | Pre-training Dataset | Dataset(Fine-tuning, Training,Testing)
VMD&R- Transformer (Zhou etal.,2020) | workload sequence | cloud workload forecasting | 2020 | Encoder& Decoder | No | NA | Googleclustertrace, Alibabaclustertrace
ACT4JS (Xu& Zhao,2022) | Cloud jobs/task | Cloud computing resourcejob scheduling. | 2022 | Encoder | No | NA | AlibabaCluster-V2018
TEDGE- Catching (Hajiakhondi- Meybodi etal.,2022) | Sequential request pattern ofthe contents (Ex: video, image, websites, etc) | Predictthe content popularity inproactive caching schemes. | 2021 | Encoder | No | NA | MovieLens
SACCT (Wangetal., 2022b) | Network status (Band- width, storage, andetc) | Optimize network basedon network status. | 2021 | Encoder | No | NA | Notmentionedclearly


[PAGE 39]
[TABLE 1]
Transformer Models | TaskAc- complished | Year | Architecture (Encoder/ Decoder) | Pre- trained (Yes/NO) | Pre-training Dataset | Dataset(Fine-tuning, Training,Testing)
Conformer(Peng etal.,2021) | Speech Recognition | 2020 | Encoder& Decoder | No | NA | Librispeech,test/testother.
SpeechTrans- former(Dong etal.,2018) | Speech Recognition | 2018 | Encoder& Decoder | No | NA | WallStreetJournal(WSJ), NVIDIAK80G-PU
VQ-Wav2vec (Baevski etal.,2020a) | Speech Recognition | 2020 | Encoder | Yes | Librispeech | TIMIT,WSJ- WallStreetJournal
Wav2vec 2.0(Baevski etal.,2020b) | Speech Recognition | 2020 | Encoder | Yes | Librispeech, LibriVox | Librispeech,Lib- riVox,TIMIT
HuBERT(Hsu etal.,2021) | Speech Recognition | 2021 | Encoder | Yes | Librispeech, Libri-light | Librispeech(train-clean), Libri-light(train-clean)
BigSSL(Zhang etal.,2022) | Speech Recognition | 2022 | Encoder& Decoder | Yes | wav2vec2.0, YT-U,Libri-Light | YouTube,English(US) Voicesearch(VS),Speech- Stew,LibriSpeech, CHiME6,Telephony


[PAGE 40]
[TABLE 1]
Whisper(Radford etal.,2022) | Speechrecogni- tion,Translation, Language Identification | 2022 | Encoder& Decoder | Yes | NotMentioned | VoxLingua107,Lib- riSpeeech,CoVoST2, Fleurs,Kincaid46
Transformer Transducer (Zhang etal.,2020b) | Speech recognition | 2020 | Encoder | No | NA | LibriSpeeech
XLSR-Wav2Vec2 (Conneau etal.,2021) | Speech recognition | 2020 | Encoder | Yes | 53languages datasets | CommonVoice,BA- BEL,Multilingual LibriSpeech(MLS)


[PAGE 41]
[TABLE 1]
Transformer Models | TaskAc- complished | Year | Architecture (Encoder/ Decoder) | Pre- trained (Yes/NO) | Pre-training Dataset | Dataset(Fine-tuning, Training,Testing)
DPTNeT(Chen etal.,2020a) | SpeechSep- aration | 2020 | Encoder& Decoder | No | NA | WSJ0-2mix,LS-2mix
Sepformer (Subakan etal.,2021) | SpeechSep- aration | 2021 | Encoder& Decoder | No | NA | WSJ0-2mix,WSJ0-3mix
WavLM(Chen etal.,2022a) | Speechsepa- ration,speech denoising,speech prediction, SpeakerVerifi- cation,Speech recognition | 2022 | Encoder | Yes | GigaSpeech, VoxPopuli | VoxCeleb1,Vox- Celeb2,Switchboard-2 CALLHOME,LIB- RICSS,LibriSpeech


[PAGE 42]
[TABLE 1]
Transformer Models | TaskAc- complished | Year | Architecture (Encoder/ Decoder) | Pre- trained (Yes/NO) | Pre-training Dataset | Dataset(Fine-tuning, Training,Testing)
AST(Gong etal.,2021) | AudioClas- sification | 2021 | Encoder | Yes | ImageNeT | AudioSet,ESC-50, SpeechCommands
Mockingjay (Liuetal.,2020) | SpeechClas- sification& recognition | 2020 | Encoder | Yes | LibriSpeech | LibriSpeechtest clean,MOSEI
XLS-R(Babu etal.,2022) | SpeechClas- sification, SpeechTrans- lation,Speech Recognition | 2021 | Encoder& Decoder | Yes | VoxPopuli(VP- 400K),Multilingual Librispeech (MLS),Common- Voice,VoxLin- gua107,BABEL | VoxPopuli,Multilingual Librispeech(MLS), CommonVoice,BABEL
UniSpeech- SAT(Chen etal.,2022b) | SpeechClas- sification& Recognition | 2022 | Encoder | Yes | LibriVox,Lib- rispeechGi- gaSpeech,VoxPopuli | SUPERB


[PAGE 43]
[TABLE 1]
Transformer Models | TaskAccomplished | Year | Architecture (Encoder/ Decoder) | Pre- trained (Yes/NO) | Pre-training Dataset | Dataset(Fine-tuning, Training,Testing)
SigT(Ren etal.,2022) | Signaldetection, channelestimation, interference suppression,and datadecodingin MIMO-OFDM | 2022 | Encoder | No | NA | PengChenglabora- tory(PCL),localareadata
TSDN(Liu etal.,2022b) | RemoveInterference andnosefrom wirelesssignal | 2022 | Encoder& Decoder | No | NA | WallNLoS,Foil NLOS,UWBdataset
ACNNT (Wangetal., 2021a) | Wirelessinterface identification | 2021 | Encoder | No | NA | ST,BPSK,AM,NAM, SFM,LFM,4FSK, 2FSKsignaldataset
MCformer (Hamidi-Rad &Jain,2021) | Automaticmodula- tionclassification complexraw radiosignals | 2021 | Encoder | No | NA | RadioML2016.10b
Quan- Transformer (Xieetal., 2022) | Compress& recoverchannel stateinformation | 2022 | Encoder& Decoder | No | NA | CsiNet,CLNetandCRNet


[PAGE 45]
[TABLE 1]
TransformerName | Fieldof application | Year | FullyTrans- former Architecture | Signal type | Transformer Task | Dataset
Three-towertrans- formernetwork (Yanetal.,2022a) | Epilepsy | 2022 | YES | EEG | Classification ofEEGsignals | CHB-MITdatasets
TransHFO(Guo etal.,2022b) | Epilepsy | 2022 | YES | MEG | Classification ofMEG signals | 20clinicalpatients
TCNandTransformer- basedmodel (Casaletal.,2022) | Sleep pathologies | 2022 | No(using TCNwhichis basedonCNN) | Cardiac signals (Heart Rate) | Classification ofsleepstages | SleepHeartHealth Studydataset
Constrainedtrans- formernetwork (Cheetal.,2021) | Heartdisease | 2021 | No(UsingCNN) | ECG | Classification ofECGsignals | 6877patients
CRT-NET(Liu etal.,2022a) | HeartDisease | 2022 | No(Using CNNandBi- directionalGRU) | ECG | Classification andrecognition ofECGsignals | MIT-BIH,CPSC arrhythmiaclin- icalprivatedata
CAT(Yang etal.,2022) | Atrial Fibrillation | 2022 | No(UsingMLP) | ECG | Classification ofECGsignals | Shaoxingdatabase (morethan 10000patients)
