# 📖 Bhagavad Gita RAG Agent

A Retrieval-Augmented Generation (RAG) based AI assistant that answers questions strictly using the **Bhagavad Gita** text.

---

## 🚀 Features
- 🔍 Semantic search using **Qdrant**
- 🧠 Context-grounded responses (No hallucination)
- 📜 Chapter & Verse-based answers
- 🤖 Powered by **Gemini embeddings**
- ⚠️ Faithful to scripture (no external knowledge)

---

## 🛠 Tech Stack
- Python
- LangChain
- Google Gemini (Embeddings + LLM)
- Qdrant Vector Database
- FastAPI (optional)
- dotenv

---

## 📂 Project Structure
c:/Users/yadav/OneDrive/Desktop/udemy/RAG/
├─] .env (ignored)
├── .gitignore
├── chat.py
├── docker-compose.yml
├── index.py
├─] RAG_env/ (ignored)
├── requirements.txt
└── The Bhagavad Gita.pdf

## ⚙️ Setup Instructions
git clone 
2️⃣ Create virtual environment
python -m venv RAG_env
RAG_env\Scripts\activate
3️⃣ Install dependencies
pip install -r requirements.txt
4️⃣ Add .env
Create .env file:
GOOGLE_API_KEY=your_api_key_here
5️⃣ Run the project
python chat.py