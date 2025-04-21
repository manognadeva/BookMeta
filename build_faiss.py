# ✅ File: build_faiss.py
import pandas as pd
import faiss
import pickle
from sentence_transformers import SentenceTransformer

df = pd.read_csv("bookkg_clean_10000.csv")
model = SentenceTransformer('all-MiniLM-L6-v2')

def get_text(row):
    title = row['original_title'] if pd.notnull(row['original_title']) else row['title']
    author = row['authors'].split(',')[0]
    tags = ', '.join(eval(row['tag_name'])) if isinstance(row['tag_name'], str) else ""
    return f"{title} by {author}. Tags: {tags}"

df['embedding_text'] = df.apply(get_text, axis=1)
embeddings = model.encode(df['embedding_text'].tolist(), show_progress_bar=True)

index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)
faiss.write_index(index, "faiss_index.bin")

metadata = df[['book_id', 'title', 'original_title', 'authors', 'original_publication_year', 'tag_name']]
with open("metadata.pkl", "wb") as f:
    pickle.dump(metadata.to_dict(orient="records"), f)
print("✅ FAISS index and metadata saved.")
