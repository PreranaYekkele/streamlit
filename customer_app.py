import streamlit as st
from PIL import Image
def get_dynamic_response(input_type):
    if input_type == 'text':
        return "Based on your text query, check out these top picks!", ["D1.jpg", "D2.jpg"]
    elif input_type == 'image':
        return "Interesting image! Here are some related products you might like.", ["D1.jpg", "D2.jpg"]
    elif input_type == 'audio':
        return "Thanks for the voice message. We suggest these options based on your interests.", ["D1.jpg", "D2.jpg"]

def main():
    st.title('Namaste🛍️')
    # st.sidebar.title("What would you like to do?")
    app_mode = st.sidebar.selectbox("Choose the mode", ["Text", "Image", "Audio"])

    if app_mode == "Text":
        handle_text_input()
    elif app_mode == "Image":
        handle_image_upload()
    elif app_mode == "Audio":
        handle_audio_upload()

def handle_text_input():
    user_text = st.text_input("Enter your query here:")
    if user_text:
        response_text, images = get_dynamic_response('text')
        st.success(response_text)
        for img in images:
            st.image(img, use_column_width=True)

def handle_image_upload():
    user_image = st.file_uploader("Upload an image to find related products:", type=["jpg", "png"], key="image_uploader")
    if user_image:
        image = Image.open(user_image)
        st.image(image, caption='Your Uploaded Image', use_column_width=True)
        response_text, images = get_dynamic_response('image')
        st.success(response_text)
        for img in images:
            st.image(img, use_column_width=True)

def handle_audio_upload():
    user_audio = st.file_uploader("Upload an audio file and get product suggestions:", type=["wav"], key="audio_uploader")
    if user_audio:
        st.audio(user_audio)
        response_text, images = get_dynamic_response('audio')
        st.success(response_text)
        for img in images:
            st.image(img, use_column_width=True)

if __name__ == "__main__":
    main()
