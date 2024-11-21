# app/utils/api_integration.py

import requests
from app.config import GEMINI_API_KEY, GEMINI_BASE_URL

def gemini_api_request(endpoint: str, payload: dict, file: 'UploadedFile' = None) -> dict:
    """
    Makes a request to the Gemini API and returns the response.
    
    Args:
        endpoint (str): The API endpoint to call.
        payload (dict): The payload to send with the request.
        file (UploadedFile, optional): The file to upload (default is None).
        
    Returns:
        dict: The API response as a dictionary.
    """
    url = GEMINI_BASE_URL + endpoint
    headers = {
        "Authorization": f"Bearer {GEMINI_API_KEY}",
        "Content-Type": "application/json" if not file else None
    }
    
    # If there's a file, use multipart/form-data to send it
    if file:
        files = {"file": file.getvalue()}  # Convert file to binary format
        response = requests.post(url, data=payload, files=files, headers=headers)
    else:
        response = requests.post(url, json=payload, headers=headers)
    
    try:
        response.raise_for_status()  # Will raise an exception for a bad response
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error while communicating with Gemini API: {e}")
        return {"error": str(e)}
