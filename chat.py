from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
from langchain_qdrant import QdrantVectorStore
from openai import OpenAI
import os
load_dotenv()


client = OpenAI(
    api_key= os.getenv("GOOGLE_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

embedding_model = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")
vector_db = QdrantVectorStore.from_existing_collection(
    url = "http://localhost:6333",
    collection_name = "bhagavad-gita",
    embedding=embedding_model
)

#take the user input
while True:
    user_input = input("\nEnter your question (type 'stop' to exit): ").strip()

    if user_input.lower() in ["stop", "exit", "quit"]:
        print("\n🙏 Thank you for seeking wisdom from the Bhagavad Gita.")
        print("🕉️ May its teachings guide your thoughts and actions.")
        print("✨ Session ended. Hare Krishna.\n")
        break

    # Retrieve relevant documents
    search_result = vector_db.similarity_search(query=user_input)

    context = "\n\n\n".join(
        [
            f"Page Content: {result.page_content}\n"
            f"Page Number: {result.metadata.get('page_label', 'N/A')}\n"
            f"File Location: {result.metadata.get('source', 'N/A')}"
            for result in search_result
        ]
    )

    SYSTEM_PROMPT = f""".You are a Retrieval-Augmented Generation (RAG) assistant specialized exclusively in the Bhagavad Gita.

Your task is to answer user questions strictly using the retrieved context.

Rules:
1. Use ONLY the information in the context.
2. If the answer is not found, reply exactly:
   "I could not find this information in the provided Bhagavad Gita texts."
3. Mention Chapter and Verse numbers when available.
4. Preserve the spiritual tone.

Context:
{context}
"""

    response = client.chat.completions.create(
        model="gemini-2.5-flash",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_input}
        ]
    )
    print("\n📜 Answer:\n")
    print(response.choices[0].message.content)
