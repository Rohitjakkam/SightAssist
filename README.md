# 👁️ SightAssist - Empowering the Visually Impaired  


**SightAssist** is an AI-powered application crafted to empower visually impaired individuals. By combining the latest in Generative AI, OCR, and Text-to-Speech technologies, SightAssist provides a seamless experience to help users navigate their surroundings with confidence.  

---

## 🚀 Key Features  

### 🔍 Scene Understanding  
AI-driven detailed descriptions of images to help users comprehend their surroundings and make informed decisions.  

### 📝 Text Extraction  
Extracts text from images using cutting-edge OCR technology, making signage, documents, and other text sources accessible.  

### 🔊 Text-to-Speech Conversion  
Transforms extracted text into clear, audible speech, enhancing accessibility and convenience.  

### 📦 Built for Accessibility  
Streamlined and intuitive workflows designed to deliver real-time assistance tailored for the visually impaired.  

---

## 🛠️ Tech Stack  

- **Frontend:** [Streamlit](https://streamlit.io/)  
- **Backend:** [Google Generative AI (Gemini)](https://cloud.google.com/generative-ai)  
- **OCR:** [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)  
- **Text-to-Speech:** [pyttsx3](https://pypi.org/project/pyttsx3/)  
- **Programming Language:** Python 3.10  

---

## 📋 Prerequisites  

1. **Python 3.10+**  
2. **Tesseract OCR**  
   - Install following [official instructions](https://github.com/tesseract-ocr/tesseract#installation).  
3. **Google Generative AI API Key**  
   - Obtain an API key from [Google Cloud Console](https://console.cloud.google.com/).  

---

## 🖥️ Installation  

### 1️⃣ Clone the Repository  
```bash  
git clone  https://github.com/Rohitjakkam/SightAssist.git
cd SightAssist
```
2️⃣ Create a Virtual Environment
```bash
python -m venv venv  
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
3️⃣ Install Dependencies
```bash
pip install -r requirements.txt  
```
4️⃣ Set up Tesseract Path (if required)
Add the Tesseract OCR executable path in the script (example for Windows):
```bash
import pytesseract  
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```
🏃‍♂️ Usage
Start the Streamlit App
```bash
streamlit run app.py
```
**Upload an Image**
Click on "Choose an image" to upload files (.jpg, .jpeg, or .png).
**Select Features**
- 🔍 Describe Scene: AI-generated detailed image description.
- 📝 Extract Text: Extract text from uploaded images.
- 🔊 Text-to-Speech: Hear extracted text as audible speech.
---
**View the Results**
Results are displayed dynamically below each feature, providing real-time feedback.
**🎯 Project Goals**
- Accessibility: Enhance the quality of life for visually impaired individuals.
- Generative AI in Action: Harness AI to solve real-world challenges.
- Inclusivity: Build tools that promote equal opportunities for all.
**🛡️ Security Note**
Keep your Google Generative AI API Key secure.
Use environment variables or a secure secrets management tool to protect sensitive information.

---
📜 License
This project is licensed under the MIT License.
---
📧 Contact
Rohit Jakkam
- **Gitbub:** [Rohitjakkam](https://github.com/Rohitjakkam)  
- **LinkedIn:** [Rohit Jakkam](https://www.linkedin.com/in/rohitjakkam/)  
Feel free to connect for any queries or collaboration opportunities! 🌟
