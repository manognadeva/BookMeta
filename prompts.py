# ✅ File: prompts.py
import re
import google.generativeai as genai

# Set up Gemini LLM
genai.configure(api_key="AIzaSyAVfYW69I29xWvUYyuubQJLVLdndnOSxOc")  # ✅ Direct API key usage
model = genai.GenerativeModel("gemma-3-4b-it")

def graph_prompt(question: str) -> str:
    prompt = f"""
You are a Cypher query expert for a Neo4j Book Knowledge Graph.

Schema:
(:Book {{book_id: int, title: string, year: int, rating: float, rating_count: int}})
(:Author {{name: string}})
(:Tag {{name: string}})
(:Book)-[:WRITTEN_BY]->(:Author)
(:Book)-[:HAS_TAG]->(:Tag)

Cypher Query Generation Rules:
- Use toLower() and CONTAINS for case-insensitive filtering
- Use OPTIONAL MATCH for author if not sure it's always present
- Use DISTINCT when returning similar books
- Use LIMIT 10 in every query
- Always return: b.title AS Title, a.name AS Author, b.year AS Year
- For rating-based queries, use: b.rating, b.rating_count
- Do NOT include explanations, markdown, or triple backticks
- Generate Cypher query only — no comments

Few-shot examples:

Q: Books similar to The Hobbit
A:
MATCH (target:Book)
WHERE toLower(target.title) CONTAINS 'the hobbit'
MATCH (target)-[:HAS_TAG]->(t:Tag)<-[:HAS_TAG]-(b:Book)
WHERE b <> target
OPTIONAL MATCH (b)-[:WRITTEN_BY]->(a:Author)
RETURN DISTINCT b.title AS Title, a.name AS Author, b.year AS Year
LIMIT 10

Q: Recommend books like The Da Vinci Code
A:
MATCH (target:Book)
WHERE toLower(target.title) CONTAINS 'da vinci code'
MATCH (target)-[:HAS_TAG]->(t:Tag)<-[:HAS_TAG]-(b:Book)
WHERE b <> target
OPTIONAL MATCH (b)-[:WRITTEN_BY]->(a:Author)
RETURN DISTINCT b.title AS Title, a.name AS Author, b.year AS Year
LIMIT 10

Q: Books tagged with fantasy with good ratings
A:
MATCH (b:Book)-[:HAS_TAG]->(t:Tag)
WHERE toLower(t.name) CONTAINS 'fantasy' AND b.rating IS NOT NULL AND b.rating > 4.2
OPTIONAL MATCH (b)-[:WRITTEN_BY]->(a:Author)
RETURN b.title AS Title, a.name AS Author, b.year AS Year, b.rating AS Rating
LIMIT 10

Q: Books by the same author as The Notebook
A:
MATCH (target:Book)-[:WRITTEN_BY]->(auth:Author)
WHERE toLower(target.title) CONTAINS 'the notebook'
MATCH (b:Book)-[:WRITTEN_BY]->(auth)
WHERE b <> target
RETURN DISTINCT b.title AS Title, auth.name AS Author, b.year AS Year
LIMIT 10

Q: How many people rated Twilight?
A:
MATCH (b:Book)
WHERE toLower(b.title) CONTAINS 'twilight'
RETURN b.title AS Title, b.rating_count AS NumberOfRatings
LIMIT 1

Q: What is the average rating of The Fault in Our Stars?
A:
MATCH (b:Book)
WHERE toLower(b.title) CONTAINS 'the fault in our stars'
RETURN b.title AS Title, b.rating AS AverageRating
LIMIT 1

User question:
{question}
"""
    response = model.generate_content(prompt)
    raw = response.text.strip()

    # 🧼 Clean up markdown if any
    clean = re.sub(r"^```[\w]*", "", raw, flags=re.IGNORECASE).replace("```", "").strip()
    return clean
