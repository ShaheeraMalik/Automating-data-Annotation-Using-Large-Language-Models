# **Automating data Annotation Using Large Language Models**  

## **Overview**  
This project automates the annotation of research papers by extracting text from PDFs, classifying them into predefined categories using **Google Gemini API**, and storing the results in a CSV file. It processes multiple PDFs efficiently using **multithreading**.  

## **Features**  
✅ Extracts **title and abstract** from the first page of each PDF.  
✅ Classifies papers into **five categories** using Google Gemini API:  
  - Machine Learning  
  - Deep Learning  
  - Optimization  
  - Computer Vision  
  - Natural Language Processing (NLP)  
✅ Handles **API rate limits** with automatic retries.  
✅ Uses **multithreading** for faster processing.  
✅ Saves classification results into a **CSV file**.  

---

## **Setup Instructions**  
### **1. Install Dependencies**  
Ensure you have **Python 3.8+** installed, then run:  

```bash
pip install pymupdf pandas google-generativeai
```

### **2. Configure Google Gemini API**  
Replace `"YOUR_ACTUAL_API_KEY"` with your **Google Gemini API key** in the script:  

```python
genai.configure(api_key="YOUR_ACTUAL_API_KEY")
```

### **3. Set File Paths**  
Modify the script to set the **input PDF folder** and **output CSV file**:  

```python
pdf_folder = r"E:\pdfs\2024"  # Path where PDFs are stored
output_csv = r"D:\AnnotatedPapers.csv"  # Output CSV file path
```

### **4. Run the Script**  
Execute the script:  

```bash
python script.py
```

---

## **How It Works**  
1. **Extract Text:** Reads the **first page** of each PDF.  
2. **Process Title & Abstract:** Identifies the **title** (first line) and **abstract** (next 5 lines).  
3. **Classify Paper:** Uses **Google Gemini API** to categorize the paper.  
4. **Store Results:** Appends results to **CSV file** with the following columns:  
   - **File Name**  
   - **Title**  
   - **Abstract**  
   - **Category**  
5. **Multithreading:** Uses **ThreadPoolExecutor** to process multiple PDFs simultaneously.  

---

## **Handling API Rate Limits**  
- If the API quota is exceeded (`429 Too Many Requests`), the script **pauses for 30 seconds** before retrying.  
- Retries up to **3 times** before marking classification as **"Error"**.  

---

## **Expected Output**  
A CSV file (`AnnotatedPapers.csv`) with data in this format:  

| File Name | Title | Abstract | Category |  
|-----------|-------|----------|----------|  
| paper1.pdf | A Study on ML | This paper explores ML techniques... | Machine Learning |  
| paper2.pdf | Deep Vision Models | Recent advancements in vision models... | Deep Learning |  

---

## **Customization**  
- **Increase Threads:** Adjust `num_threads` in the script for **faster processing**.  
- **More Categories:** Add more classification labels in the `categories` list.  
- **Change Abstract Length:** Modify how many lines are extracted from the PDF.  

---

## **Limitations**  
- Only processes the **first page** of PDFs.  
- Requires an **active Google Gemini API key**.  
- Accuracy depends on the **quality of extracted text**.  

---

## **Follow for More Updates 🚀**  
📖 **Medium:** (https://medium.com/@shaheeramalik533/automating-data-annotation-using-large-language-models-llms-40649611ed3d)  
💼 **LinkedIn:**(http://www.linkedin.com/in/shaheera-malik-35b002318)  

---

## **License**  
This project is for **educational purposes**. Modify and use it as needed.  
