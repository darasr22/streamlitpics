import streamlit as st
from PIL import Image

def main():
    st.title("Image Uploader")

    uploaded_image = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_image is not None:
        image = Image.open(uploaded_image)
        st.image(image, caption="Uploaded Image", use_column_width=True)

if __name__ == "__main__":
    main()
