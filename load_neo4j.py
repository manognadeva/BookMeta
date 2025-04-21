# ✅ File: load_neo4j.py
import pandas as pd
from neo4j import GraphDatabase

# Load dataset
df = pd.read_csv("bookkg_clean_10000.csv")

# Neo4j connection info
NEO4J_URI="neo4j+s://f6e3d72d.databases.neo4j.io"
NEO4J_USERNAME="neo4j"
NEO4J_PASSWORD="oBYe9QXgE2dU8YDbISQx5RofRPcOPXLmwk-0y5v9zMQ"
driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USERNAME, NEO4J_PASSWORD))

def load(tx, book_id, title, year, rating, rating_count, author, tags):
    tx.run("""
        MERGE (b:Book {book_id: $book_id})
        SET b.title = $title, b.year = $year, b.rating = $rating, b.rating_count = $rating_count
        MERGE (a:Author {name: $author})
        MERGE (b)-[:WRITTEN_BY]->(a)
        WITH b
        UNWIND $tags AS tag
        MERGE (t:Tag {name: tag})
        MERGE (b)-[:HAS_TAG]->(t)
    """, book_id=book_id, title=title, year=year, rating=rating, rating_count=rating_count, author=author, tags=tags)

with driver.session() as session:
    for _, row in df.iterrows():
        tags = eval(row['tag_name']) if isinstance(row['tag_name'], str) else []
        session.execute_write(
            load,
            row['book_id'],
            row['original_title'] if pd.notnull(row['original_title']) else row['title'],
            int(row['original_publication_year']) if pd.notnull(row['original_publication_year']) else 0,
            float(row['average_rating']) if pd.notnull(row['average_rating']) else None,
            int(row['work_ratings_count']) if pd.notnull(row['work_ratings_count']) else 0,
            row['authors'].split(',')[0],
            tags[:3]
        )
driver.close()
print("✅ Book data loaded into Neo4j.")