# BookMeta
A conversational **bookbot** that answers questions, finds related titles, and recommends similar books using **LLMs + Neo4j Knowledge Graph + FAISS Vector Search**.

---

## ⚡ What It Does  
- 🧠 Understands user queries using a large language model (LLM)  
- 🔎 Searches a Neo4j **knowledge graph** of books, authors, and tags  
- 🔍 Uses **semantic similarity** via FAISS when structured search fails  
- 💬 Delivers answers and recommendations through a **Streamlit chatbot**

---

## 🧩 How It Works  
**Hybrid Retrieval-Augmented Generation (RAG)** system using:
- **LangChain** tools for orchestrating KG search and vector similarity
- **Google Gemini LLM** for Cypher generation and fallback handling
- **Neo4j Aura** for storing graph data: `Book`, `Author`, `Tag`
- **FAISS** for fast semantic book search using `MiniLM` embeddings

---

## 🚀 Getting Started

### 1. Clone & Install  
```bash
pip install -r requirements.txt
```
### 2. Load Graph
```bash
python load_neo4j.py
```
### 3. Build FAISS Index
```bash
python build_faiss.py
```
### 4. Launch App
```bash
streamlit run app.py
```
