# ✅ File: agent.py
from langchain.tools import Tool
from langchain.agents import initialize_agent, AgentType
from langchain_google_genai import ChatGoogleGenerativeAI
from prompts import graph_prompt
from utils import run_cypher_query, format_kg_response
from faiss_search import search_books

# ✅ Initialize Gemini LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-pro",
    temperature=0.3,
    convert_system_message_to_human=True
)

# 🧠 Tool 1: Knowledge Graph Tool
def query_neo4j_agent_tool(question: str) -> str:
    cypher = graph_prompt(question)
    df = run_cypher_query(cypher)
    if "error" in df.columns or df.empty:
        return "No results from KG."
    return format_kg_response(df)

# 🧠 Tool 2: FAISS Similarity Search
def semantic_search_tool(query: str) -> str:
    results = search_books(query)
    if not results:
        return "No relevant books found."

    response = ""
    for i, r in enumerate(results, 1):
        response += f"{i}. {r['title']} by {r['authors']} ({r['original_publication_year']})\n"
    return response

# ⚙️ Define the tools
tools = [
    Tool(name="KnowledgeGraph", func=query_neo4j_agent_tool, description="For structured book info (ratings, genres, authors)"),
    Tool(name="SemanticSearch", func=semantic_search_tool, description="For book similarity or vague queries"),
]

# 🧠 Advanced RAG-style Agent logic
def run_agent(question: str) -> str:
    cypher = graph_prompt(question)
    df = run_cypher_query(cypher)
    if not df.empty and "error" not in df.columns:
        return format_kg_response(df)

    # Retry with reformulated question
    revised_q = f"Reformulate the question '{question}' to match the KG schema."
    reformulated = llm.invoke(revised_q)
    revised_cypher = graph_prompt(reformulated)
    df2 = run_cypher_query(revised_cypher)
    if not df2.empty and "error" not in df2.columns:
        return format_kg_response(df2)

    # Final fallback
    return semantic_search_tool(question)
# 🔁 Optional: Direct KG interface for debugging

def run_kg_direct(question: str):
    cypher = graph_prompt(question)
    df = run_cypher_query(cypher)
    return cypher, df
