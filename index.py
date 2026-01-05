from pathlib import Path    
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from dotenv import load_dotenv
#pdf loader
load_dotenv()
pdf_path = Path(__file__).parent / "THE Bhagavad Gita.pdf"
loader = PyPDFLoader(file_path=pdf_path) 
docs = loader.load()
print(f"Number of documents loaded: {len(docs)}")

#text splitter
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000, 
    chunk_overlap=150
    )
chunks = text_splitter.split_documents(docs) 

# Vector Embeddings

embedding_model = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")

vectorstore = QdrantVectorStore.from_documents(
    documents=chunks,
    embedding=embedding_model,
    collection_name="bhagavad-gita",
    url="http://localhost:6333"
)
print(f"Number of chunks created: {len(chunks)}")
print("Vector store created successfully.")