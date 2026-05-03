#utils.py
import PyPDF2
import pytesseract
from pdf2image import convert_from_bytes
from PIL import Image
import streamlit as st
import io

def extract_text_from_file(file):
    """Extracts text from uploaded .txt or .pdf files (handles scanned PDFs via OCR)."""
    file_text = ""

    if file.type == "application/pdf":
        try:
            reader = PyPDF2.PdfReader(file)
            text_found = False

            # Try standard text extraction first
            for page in reader.pages:
                text = page.extract_text()
                if text and text.strip():
                    text_found = True
                    file_text += text

            # If no text found → fall back to OCR
            if not text_found:
                st.info("🧠 No embedded text found — running OCR on scanned pages...")
                file.seek(0)
                images = convert_from_bytes(file.read())
                for i, img in enumerate(images):
                    ocr_text = pytesseract.image_to_string(img, lang="eng")
                    if ocr_text.strip():
                        file_text += f"\n--- Page {i+1} ---\n{ocr_text}"

        except Exception as e:
            st.error(f"⚠️ Error reading PDF: {e}")
            return ""

    else:
        # Handle text files
        try:
            file_text = file.read().decode("utf-8", errors="ignore")
        except Exception as e:
            st.error(f"⚠️ Unable to read text file: {e}")
            return ""

    return file_text.strip()
