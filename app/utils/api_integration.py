# utils/api_integration.py
import requests
from app.config import GEMINI_API_KEY, GEMINI_BASE_URL

def gemini_api_request(endpoint: str, payload: dict) -> dict:
    """
    Makes a request to the Gemini API and returns the response.
    
    Args:
        endpoint (str): The API endpoint to call.
        payload (dict): The payload to send with the request.
        
    Returns:
        dict: The API response as a dictionary.
    """
    url = GEMINI_BASE_URL + endpoint
    headers = {
        "Authorization": f"Bearer {GEMINI_API_KEY}",
        "Content-Type": "application/json"
    }
    
    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error while communicating with Gemini API: {e}")
        return {"error": str(e)}
