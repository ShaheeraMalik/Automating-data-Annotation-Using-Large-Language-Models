### **README.md**  

```md
# 📄 Automating Research Paper Annotation Using Large Language Models (LLMs)  

## 🚀 Project Overview  
Manually categorizing research papers is time-consuming and tedious, especially when dealing with large datasets. This project automates the **extraction**, **classification**, and **annotation** of research papers using **Google Gemini API** and **multithreading** for speed optimization.  

### ✨ **Key Features**  
✅ **Scraped PDFs Processing**: Reads research papers in **PDF format** (originally scraped from NeurIPS).  
✅ **Text Extraction**: Extracts the **title and abstract** from the first page.  
✅ **Automated Classification**: Uses **Google Gemini API** to classify papers into predefined categories.  
✅ **Efficient Storage**: Saves results into a structured **CSV file** for easy access.  
✅ **Multithreading for Speed**: Speeds up processing by handling multiple PDFs in parallel.  

### 📂 **Project Structure**  
```
📦 Automating-Data-Annotation
├── 📂 data/                     # Folder containing PDF files
├── 📜 main.py                   # Core script for extraction & classification
├── 📜 requirements.txt           # Required dependencies
├── 📜 config.py                  # API key configuration
├── 📜 README.md                  # Project documentation
└── 📜 AnnotatedPapers.csv         # Output file with classified results
```

### 📥 **Installation & Setup**  
1️⃣ **Clone this repository**  
```bash
git clone https://github.com/yourusername/Automating-Data-Annotation.git
cd Automating-Data-Annotation
```
2️⃣ **Create a virtual environment** (Optional but recommended)  
```bash
python -m venv env
source env/bin/activate  # Mac/Linux
env\Scripts\activate     # Windows
```
3️⃣ **Install required dependencies**  
```bash
pip install -r requirements.txt
```
4️⃣ **Set up API key**  
- Create a file `config.py` and add your **Google Gemini API key**  
```python
API_KEY = "your-google-gemini-api-key"
```

### 📌 **Usage**  
Run the script to start processing research papers:  
```bash
python main.py
```
- It will read PDFs from the `data/` folder.  
- Extract **title & abstract** from each paper.  
- Use **LLM classification** to assign a category.  
- Save the output in `AnnotatedPapers.csv`.  

### 🎯 **Categories Used for Classification**  
📌 **Machine Learning**  
📌 **Deep Learning**  
📌 **Optimization**  
📌 **Computer Vision**  
📌 **Natural Language Processing (NLP)**  

### 🛠 **Challenges Faced**  
🔸 **PDF Formatting Issues**: Different PDFs have varying text structures, making extraction inconsistent.  
🔸 **API Rate Limits**: Added **retry logic** with exponential backoff to handle rate limits.  
🔸 **Processing Speed**: Used **multithreading** to improve efficiency.  

### 📖 **Learn More**  
📢 **Read the Blog Post**: [Read here](https://medium.com/@shaheeramalik533/automating-data-annotation-using-large-language-models-llms-40649611ed3d)  
💼 **LinkedIn Post**: [Check out my experience]("www.linkedin.com/in/shaheera-malik-35b002318")  

### 🤝 **Contributing**  
Contributions are welcome! Feel free to submit issues or pull requests.  

### 📜 **License**  
This project is open-source and available under the **MIT License**.  
