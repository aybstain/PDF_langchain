#!/usr/bin/env python
# coding: utf-8

# In[2]:


import streamlit as st
import os 
from PyPDF2 import PdfReader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI

# Set up OpenAI API key
os.environ["OPENAI_API_KEY"] = "Your key"

# Load PDF and create document search index
def load_pdf(pdf_path):
    # Load and split PDF pages
    pdfreader = PdfReader(pdf_path)
    raw_text = ""
    for i, page in enumerate(pdfreader.pages):
        content = page.extract_text()
        if content:
            raw_text += content

    # Split text using Character Text Splitter
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=800,
        chunk_overlap=200,
        length_function=len,
    )
    texts = text_splitter.split_text(raw_text)

    # Create document search index
    embeddings = OpenAIEmbeddings()
    document_search = FAISS.from_texts(texts, embeddings)

    return document_search


# Main Streamlit app
def main():
    st.title("PDF Chatbot")
    st.sidebar.markdown("## 🦜️🔗 Query Your PDF with Langchain")
    # File upload for PDF
    pdf_file = st.sidebar.file_uploader("Upload a PDF file", type=["pdf"])

    if pdf_file is not None:
        #openai rank lnv process
        llm = OpenAI(temperature=0)
        chain = load_qa_chain(llm=llm, chain_type= "stuff")
        # Load PDF and create index
        pdf_index = load_pdf(pdf_file)
        st.sidebar.success("PDF uploaded and indexed.")

        # User input for chatbot
        user_query = st.text_input("Ask a question:")
        if st.button("Get Answer"):
            # Perform document search
            docs = pdf_index.similarity_search(user_query)

            # Run chatbot
            result = chain.run(input_documents=docs, question=user_query)
            st.write("Answer:", result)

if __name__ == "__main__":
    main()


# In[ ]:




