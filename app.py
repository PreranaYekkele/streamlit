import streamlit as st
from PIL import Image
import numpy as np
import cv2

# Streamlit app title
st.title("Image Upload and Processing Example")

# File uploader widget
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Open the uploaded image
    image = Image.open(uploaded_file)
    # Display the uploaded image
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    st.write("")
    st.write("Processing...")

    # Example processing: Convert image to grayscale
    img_array = np.array(image)
    gray_image = cv2.cvtColor(img_array, cv2.COLOR_BGR2GRAY)
    # Display the processed image
    st.image(gray_image, caption='Processed Image (Grayscale).', use_column_width=True)

    # Additional processing can be added here
