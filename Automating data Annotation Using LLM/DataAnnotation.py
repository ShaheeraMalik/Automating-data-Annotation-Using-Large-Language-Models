import os
import fitz  # PyMuPDF
import pandas as pd
import time
import google.generativeai as genai
from concurrent.futures import ThreadPoolExecutor, as_completed

# Set up Google Gemini API key
genai.configure(api_key="AIzaSyD4d_PbBk2Ffzyx2A3GrH3EYypSOUSMztE")  # Replace with actual API key

# Define categories for classification
categories = [
    "Machine Learning",
    "Deep Learning",
    "Optimization",
    "Computer Vision",
    "Natural Language Processing (NLP)"
]

# Path to the folder containing PDFs
pdf_folder = r"E:\pdfs\2024"  # Using raw string for paths
output_csv = r"D:\AnnotatedPapers.csv"

print("Starting the annotation process...")

# Function to extract text from the first page of a PDF
def extract_text_from_pdf(pdf_path):
    try:
        doc = fitz.open(pdf_path)
        text = doc[0].get_text("text")  # Extract text from the first page
        doc.close()
        return text
    except Exception as e:
        print(f"Error extracting {pdf_path}: {e}")
        return ""

# Function to classify a paper using Google Gemini API with retry logic
def classify_paper(title, abstract):
    prompt = f"""
    Classify the following research paper into one of these categories:
    - Machine Learning
    - Deep Learning
    - Optimization
    - Computer Vision
    - Natural Language Processing (NLP)

    Title: {title}
    Abstract: {abstract}
    Category:
    """
    model = genai.GenerativeModel("gemini-pro")

    for attempt in range(3):  # Retry up to 3 times if quota is exhausted
        try:
            response = model.generate_content(prompt)
            category = response.text.strip()
            return category if category in categories else "Other"
        except Exception as e:
            if "429" in str(e):
                print("Quota exceeded. Waiting before retrying...")
                time.sleep(30)  # Wait 30 seconds before retrying
            else:
                return "Error"

    return "Error"

# Function to process a single PDF file (extract text, classify, save to CSV)
def process_pdf(pdf_file):
    pdf_path = os.path.join(pdf_folder, pdf_file)
    text = extract_text_from_pdf(pdf_path)

    if text:
        lines = text.split("\n")
        title = lines[0] if len(lines) > 0 else "Unknown Title"
        abstract = " ".join(lines[1:6]) if len(lines) > 5 else "No Abstract Found"

        category = classify_paper(title, abstract)
        paper_data = [pdf_file, title, abstract, category]

        # Save to CSV (thread-safe append)
        df = pd.DataFrame([paper_data], columns=["File Name", "Title", "Abstract", "Category"])
        df.to_csv(output_csv, mode='a', header=not os.path.exists(output_csv), index=False)

        print(f"Processed & saved: {pdf_file}")

        return paper_data

# Use threading for parallel execution
num_threads = 5  # Adjust based on system capabilities
pdf_files = [f for f in os.listdir(pdf_folder) if f.endswith(".pdf")]

data = []
with ThreadPoolExecutor(max_workers=num_threads) as executor:
    future_to_pdf = {executor.submit(process_pdf, pdf_file): pdf_file for pdf_file in pdf_files}

    for future in as_completed(future_to_pdf):
        try:
            result = future.result()
            if result:
                data.append(result)
        except Exception as e:
            print(f"Error processing file: {e}")

print(f"Annotation complete. Data stored at: {output_csv}")
