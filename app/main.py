# app/main.py

import streamlit as st
from app.utils.api_integration import gemini_api_request
from app.utils.text_to_speech import extract_text_from_image, convert_text_to_speech
import os

# Set up your Streamlit app layout
def main():
    st.title("Assistive AI for the Visually Impaired")
    
    # Select Tab
    tabs = ["Scene Understanding", "Text-to-Speech", "Feedback"]
    selected_tab = st.selectbox("Choose a feature", tabs)

    if selected_tab == "Scene Understanding":
        scene_understanding_tab()
    elif selected_tab == "Text-to-Speech":
        text_to_speech_tab()
    elif selected_tab == "Feedback":
        feedback_tab()

# Scene Understanding Tab (Image description)
def scene_understanding_tab():
    st.header("Scene Understanding")

    st.markdown("### Choose an input method:")
    input_method = st.radio("Upload an image or take a photo:", ["Upload Image", "Take Photo"])

    if input_method == "Upload Image":
        uploaded_image = st.file_uploader("Upload an Image", type=["jpg", "jpeg", "png"])
    elif input_method == "Take Photo":
        uploaded_image = st.camera_input("Take a Photo")

    if uploaded_image:
        st.image(uploaded_image, caption="Input Image", use_column_width=True)
        # Example payload for scene understanding
        payload = {"image": uploaded_image.getvalue()}  # Adjust as per Gemini API requirements
        response = gemini_api_request("your-endpoint", payload, file=uploaded_image)
        st.write(f"**Scene Description:** {response.get('description', 'No description available')}")

# Text-to-Speech Tab (Text extraction and speech conversion)
def text_to_speech_tab():
    st.header("Text-to-Speech Conversion")

    st.markdown("### Choose an input method:")
    input_method = st.radio("Upload an image or take a photo:", ["Upload Image", "Take Photo"])

    if input_method == "Upload Image":
        uploaded_image = st.file_uploader("Upload an Image with Text", type=["jpg", "jpeg", "png"])
    elif input_method == "Take Photo":
        uploaded_image = st.camera_input("Take a Photo")

    if uploaded_image:
        st.image(uploaded_image, caption="Input Image", use_column_width=True)
        # Extract text from the image
        extracted_text = extract_text_from_image(uploaded_image)
        st.write(f"**Extracted Text:** {extracted_text}")

        # Convert text to speech
        if extracted_text:
            tts_lang = st.selectbox("Select Language for Text-to-Speech", options=["English (en)", "Hindi (hi)", "Spanish (es)", "French (fr)"])
            tts_lang_code = tts_lang.split("(")[-1].strip(")")

            audio_path = convert_text_to_speech(extracted_text, "app/static/audio/generated_audio.mp3", tts_lang_code)
            st.audio(audio_path)

# Feedback Tab
def feedback_tab():
    st.header("User Feedback")
    st.markdown("We value your feedback. Share your thoughts below!")

    rating = st.slider("Rate your experience (1 - Poor, 5 - Excellent)", 1, 5)
    feedback_text = st.text_area("Share your suggestions or comments:")

    if st.button("Submit Feedback"):
        if feedback_text.strip():
            save_feedback(feedback_text, rating)
            st.success("Thank you for your feedback!")
        else:
            st.error("Please provide your feedback before submitting.")

    st.markdown("### Recent Feedback")
    try:
        with open("feedback/feedback.txt", "r") as f:
            feedback_lines = f.readlines()
            st.text("".join(feedback_lines[-10:]))  # Display last 10 feedback entries
    except FileNotFoundError:
        st.info("No feedback available yet.")

# Save user feedback to file
def save_feedback(feedback, rating):
    with open("feedback/feedback.txt", "a") as f:
        f.write(f"Rating: {rating}, Feedback: {feedback}\n")

if __name__ == "__main__":
    main()
