import os
from PIL import Image, ImageOps
import streamlit as st
from io import BytesIO
from streamlit_option_menu import option_menu

# Sidebar with menu
with st.sidebar:
    selected = option_menu(
        'Information',
        ['Home', 'Member of Group', 'Image Processing App'],
        default_index=0
    )

# Page for Home
if selected == 'Home':
    st.image("Logo PU.png", width=550)
    st.title("Welcome to Our Application")
    st.write("""
    Hello and welcome to our Image Procesing App! We are from group 7 Industrial Engineering Class 3, with this 
    application we hope that user can easily access information about Image Processing.

    This app allows you to:
    - Explore the members of our group.
    - Upload and apply various processing to your images.

    Have fun! We hope you like it.
    """)

# Page for Member of Group
elif selected == 'Member of Group':
    st.title('Member of Group')

    # Member 1
    st.button("Joffandry Halike")
    st.subheader("004202300065")
    st.image("Jofan.jpeg", width=150)

    # Member 2
    st.button("Karenina Pasu Ronauli Rumapea")
    st.subheader("004202300075")
    st.image("Karenina.jpeg", width=150)

    # Member 3
    st.button("Raffi Rivanda Syam")
    st.subheader("004202300011")
    st.image("Raffi.jpeg", width=150)

    # Member 4
    st.button("Vivian Manuella")
    st.subheader("004202300017")
    st.image("Vivian.jpeg", width=150)

# Page for Image Transportation App
elif selected == 'Image Processing App':
    st.title('Image Processing App')

    # Function to display an image with a title
    def display_image_with_title(image, title):
        st.subheader(title)
        st.image(image, use_column_width=True)

    # Function to skew an image
    def skew_image(image, skew_x=0.5, skew_y=0):
        width, height = image.size
        x_shift = skew_x * height
        new_width = width + abs(x_shift)
        skew_matrix = (1, skew_x, -x_shift if x_shift > 0 else 0, skew_y, 1, 0)
        return image.transform((int(new_width), height), Image.AFFINE, skew_matrix)

    # Image upload instructions
    st.write("Upload an image and apply transformations like rotation, scaling, translation, and skewing.")

    # File uploader
    uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Open image
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # Rotation
        st.subheader("Rotate Image")
        angle = st.slider("Rotation Angle (degrees):", min_value=0, max_value=360, value=45)
        rotated_image = image.rotate(angle, expand=True)
        display_image_with_title(rotated_image, "Rotated Image")

        # Scaling
        st.subheader("Scale Image")
        scale_factor = st.slider("Scaling Factor:", min_value=0.1, max_value=3.0, value=1.0, step=0.1)
        scaled_image = image.resize((int(image.width * scale_factor), int(image.height * scale_factor)))
        display_image_with_title(scaled_image, "Scaled Image")

        # Translation
        st.subheader("Translate Image")
        translate_x = st.slider("Translation on X-axis (pixels):", min_value=0, max_value=200, value=50)
        translate_y = st.slider("Translation on Y-axis (pixels):", min_value=0, max_value=200, value=50)
        translated_image = ImageOps.expand(image, border=(translate_x, translate_y, 0, 0), fill="white")
        display_image_with_title(translated_image, "Translated Image")

        # Skewing
        st.subheader("Skew Image")
        skew_x = st.slider("Skew Factor on X-axis:", min_value=0.0, max_value=1.0, value=0.5, step=0.1)
        skewed_image = skew_image(image, skew_x=skew_x)
        display_image_with_title(skewed_image, "Skewed Image")

        # Download section
        st.subheader("Download Transformed Images")
        for transformed_image, title in zip(
            [rotated_image, scaled_image, translated_image, skewed_image],
            ["Rotated", "Scaled", "Translated", "Skewed"]
        ):
            buf = BytesIO()
            transformed_image.save(buf, format="JPEG")
            byte_data = buf.getvalue()
            st.download_button(
                label=f"Download {title} Image",
                data=byte_data,
                file_name=f"{title.lower()}_image.jpg",
                mime="image/jpeg"
            )

    # Closing message
    st.write("Don't forget to download your transformed images!")
