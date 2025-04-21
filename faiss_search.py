import faiss
import pickle
import pandas as pd
from sentence_transformers import SentenceTransformer

index = faiss.read_index("faiss_index.bin")
with open("metadata.pkl", "rb") as f:
    metadata = pickle.load(f)

model = SentenceTransformer('all-MiniLM-L6-v2')

def search_books(query, top_k=5):
    query_embedding = model.encode([query])
    scores, indices = index.search(query_embedding, top_k)
    return [metadata[i] for i in indices[0] if i < len(metadata)]
