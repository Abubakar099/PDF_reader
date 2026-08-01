# 📄 RAG PDF Chatbot

A simple RAG (Retrieval-Augmented Generation) PDF Chatbot built with **Streamlit**, **LangChain**, **Google Gemini**, and **ChromaDB**.

---

# 🚀 Setup Guide

## 1. Clone the Repository

```bash
git clone <your-repository-url>
cd PDF_reader
```

---

## 2. Create a Virtual Environment

```bash
python -m venv venv
```

---

## 3. Activate the Virtual Environment

### Git Bash

```bash
source venv/Scripts/activate
```

### Command Prompt (CMD)

```bash
venv\Scripts\activate
```

### PowerShell

```powershell
venv\Scripts\Activate.ps1
```

---

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install langchain langchain-community langchain-google-genai langchain-huggingface

pip install chromadb sentence-transformers

pip install pymupdf pytesseract pdf2image

pip install streamlit python-dotenv
```

---

## 5. Create a `.env` File

```env
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```

---

## 6. Install System Dependencies

### Windows

Install:

- **Tesseract OCR**
- **Poppler for Windows**

Add both of these folders to your system **PATH**:

- `Tesseract-OCR`
- `Poppler\Library\bin`

Verify installation:

```bash
tesseract --version
```

```bash
pdftoppm -v
```

### Linux (Ubuntu)

```bash
sudo apt update

sudo apt install tesseract-ocr

sudo apt install poppler-utils
```

---

## 7. Run the Application

```bash
streamlit run app.py
```

---

# 📁 Project Structure

```text
PDF_reader/
│
├── app.py
├── pdf_loader.py
├── vectorstore.py
├── qa_chain.py
├── README.md
├── requirements.txt
├── .gitignore
├── .env                # Ignored by Git
│
├── chroma_db/          # Ignored by Git
├── venv/               # Ignored by Git
└── __pycache__/        # Ignored by Git
```

---

# 📦 Technologies Used

- Python
- Streamlit
- Google Gemini API
- LangChain
- ChromaDB
- Sentence Transformers
- PyMuPDF
- pdf2image
- pytesseract
- Poppler
- Tesseract OCR

---

# 📝 Notes

- `venv/`, `chroma_db/`, `.env`, and `__pycache__/` are ignored using `.gitignore`.
- Poppler and Tesseract are **system-level dependencies** and must be installed separately.
- The vector database (`chroma_db/`) is automatically created after processing a PDF.
