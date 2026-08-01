# Proper Virtual Environment (venv) Setup

## Step 1: Go to Project Folder
```bash
cd /d/Rag/chatbot
pwd
```

## Step 2: Remove Old Virtual Environment (if exists)
```bash
rm -rf venv
```

## Step 3: Create a New Virtual Environment
```bash
python -m venv venv
```

## Step 4: Activate the Virtual Environment (Git Bash)
```bash
source venv/Scripts/activate
```

## Step 5: Verify Installed Packages
```bash
pip list
```

## Step 6: Install Required Packages
```bash
pip install langchain langchain-community langchain-google-genai langchain-huggingface

pip install chromadb sentence-transformers
pip install chromadb
pip install tesseract
pip install pymupdf pytesseract pdf2image

pip install streamlit python-dotenv
```

## Step 7: Verify Installation
```bash
pip list
```

## Step 8: Run the Application
```bash
streamlit run app.py
```

## Step 9: Verify Tesseract OCR Installation
```bash
tesseract --version
```

<!-- ******************************** -->
You'll also need Tesseract OCR itself installed on your system (not just the Python wrapper) — sudo apt install tesseract-poppler-utils poppler-utils on Linux, or the Windows installer if you're on Windows.

Files to create
pdf-chatbot/
├── app.py                  # Streamlit UI — upload PDF, chat interface
├── requirements.txt        # pinned versions for deployment
├── .env                    # GOOGLE_API_KEY=your_gemini_key (get free at aistudio.google.com)
├── .gitignore              # ignore .env, chroma_db/, __pycache__
├── utils/
│   ├── __init__.py
│   ├── pdf_loader.py        # extract text; falls back to OCR if page has no text
│   ├── vectorstore.py       # chunk text, embed, build/query Chroma
│   └── qa_chain.py          # LangChain retrieval chain + Gemini call
└── chroma_db/               # auto-created, stores the vector index (gitignore this)

What goes in each: