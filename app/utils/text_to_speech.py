# app/utils/text_to_speech.py

from fastapi import UploadFile
import pytesseract
from gtts import gTTS
import os
from PIL import Image
import base64

def extract_text_from_image(image: 'UploadFile', lang="eng") -> str:
    """
    Extract text from an image using OCR.
    
    Args:
        image (UploadedFile): The image to process.
        lang (str): The language for OCR (default is English).
        
    Returns:
        str: The extracted text.
    """
    # Open the image using Pillow
    img = Image.open(image)
    text = pytesseract.image_to_string(img, lang=lang)
    return text

def convert_text_to_speech(text: str, output_path: str, lang_code="en"):
    """
    Convert text to speech and save it to an audio file.
    
    Args:
        text (str): The text to convert.
        output_path (str): The file path to save the audio.
        lang_code (str): Language code (default is "en" for English).
        
    Returns:
        str: The file path to the saved audio file.
    """
    tts = gTTS(text=text, lang=lang_code)
    tts.save(output_path)
    return output_path
