# ✅ File: utils.py
from neo4j import GraphDatabase
import pandas as pd

# Neo4j connection
NEO4J_URI = "neo4j+s://f6e3d72d.databases.neo4j.io"
NEO4J_USERNAME = "neo4j"
NEO4J_PASSWORD = "oBYe9QXgE2dU8YDbISQx5RofRPcOPXLmwk-0y5v9zMQ"

driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USERNAME, NEO4J_PASSWORD))

# 🔁 Run Cypher query
def run_cypher_query(cypher: str) -> pd.DataFrame:
    try:
        with driver.session() as session:
            result = session.run(cypher)
            return pd.DataFrame(result.data())
    except Exception as e:
        return pd.DataFrame([{"error": str(e)}])

# 📘 Neo4j schema string (for Gemini prompt context)
def get_schema_string() -> str:
    return """
(:Book {book_id: int, title: string, year: int, rating: float, rating_count: int})
(:Author {name: string})
(:Tag {name: string})
(:Book)-[:WRITTEN_BY]->(:Author)
(:Book)-[:HAS_TAG]->(:Tag)
"""
# ✅ Add this to utils.py
def format_kg_response(df):
    if df.empty:
        return "No results found in the Knowledge Graph."

    response = ""
    for i, row in df.iterrows():
        title = row.get("Title", "Unknown Title")
        author = row.get("Author", "Unknown Author")
        year = row.get("Year", "Unknown Year")
        response += f"{i+1}. {title} by {author} ({year})\n"
    return response.strip()
