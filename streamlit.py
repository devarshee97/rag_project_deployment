import streamlit as st
import requests

# ----------------------------
# Backend API URL (Render)
# ----------------------------
API_URL = "https://rag-for-documents.onrender.com/query"

# ----------------------------
# UI Config
# ----------------------------
st.set_page_config(page_title="RAG Chat", page_icon="🤖")
st.title("📄 RAG Document Assistant")

st.write("Ask questions based on your documents")

# ----------------------------
# Input box
# ----------------------------
query = st.text_input("Enter your query:")

# ----------------------------
# Button click
# ----------------------------
if st.button("Ask"):
    if not query.strip():
        st.warning("Please enter a query")
    else:
        with st.spinner("Thinking..."):
            try:
                response = requests.post(
                    API_URL,
                    json={"query": query}
                )

                data = response.json()

                st.subheader("Answer")
                st.write(data["answer"])

            except Exception as e:
                st.error(f"Error: {str(e)}")