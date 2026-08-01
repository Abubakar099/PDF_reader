import fitz  
import pytesseract
from pdf2image import convert_from_path


def extract_text_from_pdf(pdf_path):
    """
    PDF se text nikalta hai.
    Agar page pe text na mile (scanned page), to OCR use karta hai.
    """
    doc = fitz.open(pdf_path)
    all_text = ""

    for page_number in range(len(doc)):
        page = doc[page_number]
        text = page.get_text()

        if text.strip():
           
            all_text += f"\n--- Page {page_number + 1} ---\n{text}"
        else:
            # if pdf text is empty then pdf is image page, ocr is using 
            print(f"Page {page_number + 1}: text nahi mila, OCR chala rahe hain...")
            images = convert_from_path(pdf_path, first_page=page_number + 1, last_page=page_number + 1)
            ocr_text = pytesseract.image_to_string(images[0])
            all_text += f"\n--- Page {page_number + 1} (OCR) ---\n{ocr_text}"

    doc.close()
    return all_text


# just for testing 
if __name__ == "__main__":
    test_pdf_path = "Linked List.pdf" 
    result = extract_text_from_pdf(test_pdf_path)
    print(result[:1000])  
