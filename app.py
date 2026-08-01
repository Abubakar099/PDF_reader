import streamlit as st
import tempfile
import os

from pdf_loader import extract_text_from_pdf
from vectorstore import create_vectorstore
from qa_chain import get_answer

# st.set_page_config(page_title="PDF Chatbot", page_icon="📄")
st.title("📄 PDF Chatbot")
st.write("Apna PDF upload karo aur uske baare mein sawal poocho.")

# Session state — 
if "vectorstore" not in st.session_state:
    st.session_state.vectorstore = None

if "messages" not in st.session_state:
    st.session_state.messages = []
    print(st.session_state.messages)
    
# --- PDF upload ---
uploaded_file = st.file_uploader("Apna PDF yahan daalo", type="pdf")

if uploaded_file is not None and st.session_state.vectorstore is None:
    with st.spinner("Loading ...."):
         # upload pdf is temporary save bcz of Pymupdf need file path 
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
            tmp_file.write(uploaded_file.read())
            tmp_path = tmp_file.name

        text = extract_text_from_pdf(tmp_path)
        st.session_state.vectorstore = create_vectorstore(text)

        os.remove(tmp_path)  # temporary file is delete

    st.success("PDF process ho gaya! Ab neeche sawal poochh sakte ho.")

# --- Chat interface ---
if st.session_state.vectorstore is not None:
    # Pichle sawal-jawab dikhao
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    
    question = st.chat_input("hello ")
    

    if question:
        st.session_state.messages.append({"role": "user", "content": question})
        with st.chat_message("user"):
            st.write(question)

        with st.chat_message("assistant"):
            with st.spinner("Soch raha hoon..."):
                answer = get_answer(st.session_state.vectorstore, question)
                st.write(answer)

        st.session_state.messages.append({"role": "assistant", "content": answer})
else:
    st.info("Pehle upar se PDF upload karo.")
