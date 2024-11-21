# SightAssist
# AI Assistant for Visually Impaired Individuals

This project leverages **Generative AI** to assist visually impaired individuals in perceiving and interacting with their surroundings.

## Features
1. **Scene Understanding**: Generates a textual description of the uploaded image.
2. **Text-to-Speech Conversion**: Extracts text from an image and converts it to speech.
3. **Example Demonstrations**: Includes preloaded images to showcase the functionality.

## Technologies Used
- **Streamlit**: Interactive web application framework.
- **Google Generative AI (Gemini API)**: AI model for scene understanding.
- **Tesseract OCR**: Text extraction from images.
- **gTTS**: Text-to-speech conversion.

## Installation

### Prerequisites
- Python 3.10+
- Streamlit, Tesseract OCR, and gTTS installed.

### Steps
1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/ai_assist_visually_impaired.git
    cd ai_assist_visually_impaired
    ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Run the application:
    ```bash
    streamlit run app/main.py
    ```

## Usage
1. Upload an image in the respective feature tab.
2. View the generated scene description or extracted text.
3. Listen to the generated audio file for text-to-speech conversion.

## Deployment
- **Streamlit Cloud**: Follow the [Streamlit Deployment Guide](https://streamlit.io/cloud).
- **Docker**: Build and deploy using the provided `Dockerfile`.

## License
This project is licensed under the MIT License.
