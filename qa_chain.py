import os
from langchain_google_genai import ChatGoogleGenerativeAI
# from google import genai
from dotenv import load_dotenv

# .env file se GOOGLE_API_KEY load karo
load_dotenv()
# print("API KEY:", os.getenv("GOOGLE_API_KEY"))
# client = genai.Client(api_key = os.getenv("GOOGLE_API_KEY"))
# for model in client.models.list():
#     print(model)

def get_answer(vectorstore, question):
    """
    Vectorstore se relevant chunks dhoondta hai,
    phir Gemini ko bhej kar jawab banata hai.
    """
    # Step 1:  relevant 3 chunks 
    relevant_docs = vectorstore.similarity_search(question, k=3)
    context = "\n\n".join([doc.page_content for doc in relevant_docs])

    
    llm = ChatGoogleGenerativeAI(   
        model="gemini-2.5-flash",
        temperature=0.2,  # kam temperature = zyada factual, kam "creative" jawab
    )

        # Step 3: Prompt banao — context + sawal
    prompt = f"""
Tum ek funny aur friendly AI chatbot ho.

Rules:
- Hamesha Roman Urdu mein jawab do.
- Sirf document ka use karo.
- Har jawab halka sa funny aur natural ho.
- Kabhi kabhi emojis use kar sakte ho. 😄
- Agar jawab document mein na ho to bolo:

"Bhai 😂 document mein to yeh scene hi nahi mila. Ya to sahi sawal pocho ya phir document upload karo."

Document:
{context}

Sawal:
{question}

Jawab:
"""

    # Step 4: get ans from gemini
    response = llm.invoke(prompt)
    return response.content


# Testing ke liye
if __name__ == "__main__":
    from pdf_loader import extract_text_from_pdf
    from vectorstore import create_vectorstore

    text = extract_text_from_pdf("Linked List.pdf")
    vectorstore = create_vectorstore(text)

    question = "yeh document kis baare mein hai? always use roman urdu to give answer"
    answer = get_answer(vectorstore, question)

    print("\n--- Sawal ---")
    print(question)
    print("\n--- Jawab ---")
    print(answer)
