# BookMeta📚
A conversational **bookbot** that answers questions, finds related titles, and recommends similar books using **LLMs + Neo4j Knowledge Graph + FAISS Vector Search**.

---

## Brief Idea💡:
BookMeta allows users to ask natural language questions like:

  “Recommend books like The Hunger Games”
  
  “How many people rated Twilight?”
  
  “Show fantasy books with high ratings”

The system intelligently routes the query through either a Neo4j-based knowledge graph or a FAISS-powered semantic search engine—based on query type and data availability. It uses Google Gemini (via LangChain) to convert user queries into Cypher queries and dynamically retrieve graph data. If no relevant graph data is found, it gracefully falls back to a vector similarity model.

The end result is a hybrid RAG application deployed on a full-stack Streamlit frontend, complete with user authentication, dynamic query handling, and interactive book discovery.

---

## 🧩 How It Works  
**Hybrid Retrieval-Augmented Generation (RAG)** system using:
- **LangChain** tools for orchestrating KG search and vector similarity
- **Google Gemini LLM** for Cypher generation and fallback handling
- **Neo4j Aura** for storing graph data: `Book`, `Author`, `Tag`
- **FAISS** for fast semantic book search using `MiniLM` embeddings

---

## 🚀 Project Structure

├── app.py

├── agent.py

├── build_faiss.py

├── faiss_search.py

├── load_neo4j.py

├── prompts.py

├── utils.py

├── bookkg_clean_10000.csv

├── faiss_index.bin

├── metadata.pkl

└── users.json

## 🎬 Getting Started

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
python faiss_search.py
```
### 4. Launch App
```bash
streamlit run app.py
```
## 💭 Example Questions

→ Recommend books like The Hunger Games  
→ When was fault in our stars released? 
→ How many people rated Twilight?  
→ Books released in 2020 and rating above 4.0

## 🗃️ Technologies Used
- Python, Streamlit, LangChain

- Neo4j AuraDB, FAISS

- Gemini LLM (Google Generative AI)


