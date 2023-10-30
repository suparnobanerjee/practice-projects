from langchain.document_loaders import PyPDFLoader, DirectoryLoader, PDFMinerLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import SentenceTransformerEmbeddings
from langchain.vectorstores import chroma
import os
from constants import CHROMA_SETTINGS

persist_directory = 'db'

def main():
    for root, dirs, files in os.walk("docs"):