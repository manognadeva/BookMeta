import streamlit as st
from PIL import Image
from agent import run_agent

st.set_page_config(page_title="BookMeta", page_icon="📚", layout="wide")

# ----------------- HEADER -----------------
col1, col2 = st.columns([11, 1])
with col1:
    st.markdown("## 📚 BookMeta")
    st.markdown("_**Discover books · Ask questions · Get smarter recommendations**_")
with col2:
    user_icon = Image.open("assets/user_icon.jpg")
    st.image(user_icon, width=40)

st.markdown("---")

# ----------------- CUSTOM TABS BELOW HEADER -----------------
selected = st.radio(
    "Navigate", ["Home", "Chatbot", "About"],
    horizontal=True,
    label_visibility="collapsed"
)

# ----------------- HOME -----------------
if selected == "Home":
    st.markdown("## 🪐 Welcome to the Book Universe")
    st.markdown("_**Explore some of our popular books:**_")

    book_images = {
        "Fault in our Stars": "assets/fault in our stars.jpg",
        "Pride and Prejudice": "assets/pride and prejudice.jpg",
        "Little Women":"assets/little women.jpg",
        "A Court of Thorns and Roses": "assets/acotar.jpeg",
        "A Court of Mist and Fury": "assets/acomaf.jpeg",
        "A Court of Wings and Ruin": "assets/acowar.jpeg",
        "Throne of Glass": "assets/throne of glass.jpg",
        "Empire of Storms":"assets/empire of storms.jpg",
        "The Devil wears Prada": "assets/the devil wears prada.jpg",
        "A Diary of a Young Girl": "assets/a diary of a young girl.jpg",
        "Harry Potter": "assets/harry potter.jpg",
        "Crooked Kingdom":"assets/Crooked Kingdom.jpg",
        "The Hunger Games": "assets/hunger games.jpg",
        "Twilight": "assets/twilight.jpeg",
        "Time Traveller's Wife": "assets/ttw.jpeg",
        "The Hate U Give": "assets/the hate u give.jpeg",
        "Breakfast at Tiffany's": "assets/breakfast at tiffany's.jpg",
        "Fifty Shades of Grey":"assets/fifty shades of grey.jpeg",
        "A Song of Ice and Fire": "assets/asoiaf.jpeg",
        "To Kill a Mockingbird": "assets/to kill a mockingbird.jpeg",
        "The Authoritative Calvin and Hobbes": "assets/calvin and hobbes.jpeg",
        "Life of Pi":"assets/life of pi.jpg",
        "The Lovely Bones": "assets/the lovely bones.jpeg",
        "Gone Girl": "assets/gone girl.jpeg"
    }

    cols = st.columns(4)
    for i, (title, path) in enumerate(book_images.items()):
        with cols[i % 4]:
            st.image(path, width=220)

# ----------------- CHATBOT -----------------
elif selected == "Chatbot":
    st.markdown("## 💬 Your Bookbot")
    st.markdown("Ask anything about books, genres, authors, or recommendations!")

    query = st.text_input("🔍 Ask your question")
    if query:
        with st.spinner("Thinking..."):
            response = run_agent(query)
            st.success("🧠 Answer:")
            st.markdown(response)

# ----------------- ABOUT -----------------
elif selected == "About":
    st.markdown("## 🔖 About this application")
    st.markdown("""
    This is an interactive book knowledge assistant built using:
    - Agentic AI (LLMs + Neo4j Knowledge Graph)
    - Python, Streamlit, and Graph-based retrieval
    - Purpose: Help you discover books based on tags, themes, authors, and more!
    """)
