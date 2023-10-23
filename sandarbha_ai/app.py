import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space
import openai
import os
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain
from langchain.callbacks import get_openai_callback
import pickle

openai.api_key = os.environ.get('OPEN_API_KEY')

with st.sidebar:
  st.title('Sandarbha')
  st.markdown('''
  LLM Chatbot built using :
  - [Streamlit](https://streamlit.io/)
  - [LangChain](https://python.langchain.com/)
  - [OpenAI API](https://platform.openai.com/account/api-keys)
  ''')
  add_vertical_space(2)
  st.write('Created by [Suparno](https://twitter.com/sparno_/)✍️')

def main():  
  st.title('Chat with PDF💬')
  pdf=st.file_uploader('Upload your PDF',type='pdf')
  if pdf is not None:
    pdf_reader=PdfReader(pdf)
    text=''
    for page in pdf_reader.pages:
      text+=page.extract_text()
    
    text_splitter = RecursiveCharacterTextSplitter(
      chunk_size=1000,
      chunk_overlap=200,
      length_function=len
    )
    chunks=text_splitter.split_text(text=text)

    store_name=pdf.name[:-4]
    if os.path.exists(f"{store_name}.pkl"):
      with open(f"{store_name}.pkl","rb") as f:
        vector_store = pickle.load(f)
      st.write('Embeddings loaded from the disk')
    else:
      embeddings = OpenAIEmbeddings()
      vector_store = FAISS.from_texts(chunks, embeddings)
      with open(f"{store_name}.pkl","wb") as f:
        pickle.dump(vector_store, f)

  query = st.text_input("Ask Questions about your PDF Document :")
  if query:
    docs = vector_store.similarity_search(query=query, k=3)
    llm = OpenAI(model_name="gpt-3.5-turbo", temperature=0,)
    chain = load_qa_chain(llm=llm, chain_type="stuff")
    with get_openai_callback() as cb:
      response=chain.run(input_documents=docs, question=query)
      print(cb)
    st.write(response)


if __name__ == '__main__':
  main()
                                       
                                                      