import streamlit as st
from PIL import Image, ImageFilter
import numpy as np
from io import BytesIO
import cv2

# Function to convert image to grayscale


def grayscale(image):
    grayscale_image = image.convert('L')
    grayscale_image = grayscale_image.filter(
        ImageFilter.SMOOTH_MORE).filter(ImageFilter.SHARPEN)
    return grayscale_image

# Function to apply Gaussian blur


def apply_gaussian_blur(image):
    blur_strength = st.slider("Select Gaussian blur strength:", 1, 10, 1)
    blurred_image = image.filter(ImageFilter.GaussianBlur(blur_strength))
    return blurred_image

# Function to apply Box blur


def apply_box_blur(image):
    blur_strength = st.slider("Select Box blur strength:", 1, 10, 1)
    blurred_image = image.filter(ImageFilter.BoxBlur(blur_strength))
    return blurred_image

# Function to detect edges


def edge_detection(image):
    image = image.convert("L")
    image = image.filter(ImageFilter.FIND_EDGES).filter(
        ImageFilter.EDGE_ENHANCE).filter(ImageFilter.FIND_EDGES)
    return image

# Function to crop the image


def crop_image(image, left, top, right, bottom):
    cropped_image = image.crop((left, top, right, bottom))
    return cropped_image

# Function to flip the image left to right


def flip_left_right(image):
    flipped_image = image.transpose(Image.FLIP_LEFT_RIGHT)
    return flipped_image

# Function to flip the image top to bottom


def flip_top_bottom(image):
    flipped_image = image.transpose(Image.FLIP_TOP_BOTTOM)
    return flipped_image

# Function to rotate the image


def rotate_image(image):
    angle = st.slider("Select rotation angle:", 0, 360, 45)
    rotated_image = image.rotate(angle, expand=True)
    return rotated_image

# Function to split the image into RGB channels


def split_image(image):
    red, green, blue = image.split()
    return red, green, blue

# Main function to run the Streamlit app


buf = BytesIO()


def main():
    st.title("Image Processing App")

    # Upload image
    uploaded_image = st.file_uploader(
        "Choose an image", type=["jpg", "jpeg", "png"])

    if uploaded_image is not None:
        # Display the uploaded image
        img = Image.open(uploaded_image)
        st.image(img, caption="Original Image", use_column_width=True)

        # Select image processing option
        option = st.radio("Choose an option:", ("Grayscale", "Gaussian Blur", "Box Blur",
                          "Edge Detection", "Crop", "Flip Left Right", "Flip Top Bottom", "Rotate", "ALL"))

        # Process the image based on selected option
        if option == "Grayscale":
            processed_image = grayscale(img)
            st.image(processed_image, caption="Grayscale Image",
                     use_column_width=True)
            buf = BytesIO()
            # Save the processed image to a buffer
            processed_image.save(buf, format="JPEG")
            byte_rotate = buf.getvalue()
    # Provide download button for the rotated image
            btn_rotate = st.download_button(
                label="Download Grayscale Image",
                data=byte_rotate,
                file_name="Grayscale_image.jpg",
                mime="image/jpeg"
            )

        elif option == "Gaussian Blur":
            processed_image = apply_gaussian_blur(img)
            st.image(processed_image, caption="Gaussian Blurred Image",
                     use_column_width=True)
            buf = BytesIO()
            # Save the processed image to a buffer
            processed_image.save(buf, format="JPEG")
            byte_rotate = buf.getvalue()
    # Provide download button for the rotated image
            btn_rotate = st.download_button(
                label="Download Gaussian Blurred Image",
                data=byte_rotate,
                file_name="gaussian_blurred_image.jpg",
                mime="image/jpeg"
            )

        elif option == "Box Blur":
            processed_image = apply_box_blur(img)
            st.image(processed_image, caption="Box Blurred Image",
                     use_column_width=True)
            buf = BytesIO()
            # Save the processed image to a buffer
            processed_image.save(buf, format="JPEG")
            byte_rotate = buf.getvalue()
    # Provide download button for the rotated image
            btn_rotate = st.download_button(
                label="Download Box Blurred Image",
                data=byte_rotate,
                file_name="box_blurred_image.jpg",
                mime="image/jpeg"
            )

        elif option == "Edge Detection":
            processed_image = edge_detection(img)
            st.image(processed_image, caption="Edge Detected Image",
                     use_column_width=True)
            buf = BytesIO()
            # Save the processed image to a buffer
            processed_image.save(buf, format="JPEG")
            byte_rotate = buf.getvalue()
    # Provide download button for the rotated image
            btn_rotate = st.download_button(
                label="Download edge detection Image",
                data=byte_rotate,
                file_name="edge_detection_image.jpg",
                mime="image/jpeg"
            )

        elif option == "Crop":
            st.header("Keep the top side < bottom side")
            left = st.slider("Left:", 0, img.width, 0)
            top = st.slider("Top:", 0, img.height, 0)
            right = st.slider("Right:", 0, img.width, img.width)
            bottom = st.slider("Bottom:", 0, img.height, img.height)
            processed_image = crop_image(img, left, top, right, bottom)
            st.image(processed_image, caption="Cropped Image",
                     use_column_width=True)
            buf = BytesIO()
            # Save the processed image to a buffer
            processed_image.save(buf, format="JPEG")
            byte_rotate = buf.getvalue()
    # Provide download button for the rotated image
            btn_rotate = st.download_button(
                label="Download crop Image",
                data=byte_rotate,
                file_name="cropped_image.jpg",
                mime="image/jpeg"
            )

        elif option == "Flip Left Right":
            processed_image = flip_left_right(img)
            st.image(processed_image,
                     caption="Flipped Left Right Image", use_column_width=True)
            buf = BytesIO()
            # Save the processed image to a buffer
            processed_image.save(buf, format="JPEG")
            byte_rotate = buf.getvalue()
    # Provide download button for the rotated image
            btn_rotate = st.download_button(
                label="Download flip left right Image",
                data=byte_rotate,
                file_name="Flip_left_right_image.jpg",
                mime="image/jpeg"
            )

        elif option == "Flip Top Bottom":
            processed_image = flip_top_bottom(img)
            st.image(processed_image,
                     caption="Flipped Top Bottom Image", use_column_width=True)
            buf = BytesIO()
            # Save the processed image to a buffer
            processed_image.save(buf, format="JPEG")
            byte_rotate = buf.getvalue()
    # Provide download button for the rotated image
            btn_rotate = st.download_button(
                label="Download flip top bottom Image",
                data=byte_rotate,
                file_name="Flip_top_bottom_image.jpg",
                mime="image/jpeg"
            )

        elif option == "Rotate":
            processed_image = rotate_image(img)
            st.image(processed_image, caption="Rotated Image",
                     use_column_width=True)
    # Save the processed image to a buffer
            buf = BytesIO()
            processed_image.save(buf, format="JPEG")
            byte_rotate = buf.getvalue()
    # Provide download button for the rotated image
            btn_rotate = st.download_button(
                label="Download rotate Image",
                data=byte_rotate,
                file_name="Rotate_image.jpg",
                mime="image/jpeg"
            )

        elif option == "ALL":
            st.write("Starting ALL transformations")

            # Grayscale transformation
            processed_image = grayscale(img)
            st.image(processed_image, caption="Grayscale Image",
                     use_column_width=True)
            buf = BytesIO()
            # Blur transformation
            blur_option = st.radio(
                "Apply blur:", ("None", "Gaussian Blur", "Box Blur"))
            if blur_option == "Gaussian Blur":
                processed_image = apply_gaussian_blur(processed_image)
                st.image(
                    processed_image, caption="Gaussian Blurred Image", use_column_width=True)

            elif blur_option == "Box Blur":
                processed_image = apply_box_blur(processed_image)
                st.image(processed_image, caption="Box Blurred Image",
                         use_column_width=True)

            # Edge detection transformation
            edge_option = st.radio(
                "Apply edge detection:", ("None", "Edge Detection"))
            if edge_option == "Edge Detection":
                processed_image = edge_detection(processed_image)
                st.image(processed_image, caption="Edge Detected Image",
                         use_column_width=True)

            # Crop transformation
            st.header("Keep the top side < bottom side")
            left = st.slider("Left:", 0, processed_image.width, 0)
            top = st.slider("Top:", 0, processed_image.height, 0)
            right = st.slider(
                "Right:", 0, processed_image.width, processed_image.width)
            bottom = st.slider(
                "Bottom:", 0, processed_image.height, processed_image.height)
            processed_image = crop_image(
                processed_image, left, top, right, bottom)
            st.image(processed_image, caption="Cropped Image",
                     use_column_width=True)

            # Flip transformation
            flip_option = st.radio(
                "Apply flip:", ("None", "Flip Left Right", "Flip Top Bottom"))
            if flip_option == "Flip Left Right":
                processed_image = flip_left_right(processed_image)
                st.image(
                    processed_image, caption="Flipped Left Right Image", use_column_width=True)
            elif flip_option == "Flip Top Bottom":
                processed_image = flip_top_bottom(processed_image)
                st.image(
                    processed_image, caption="Flipped Top Bottom Image", use_column_width=True)

            # Rotate transformation
            processed_image = rotate_image(processed_image)
            st.image(processed_image, caption="Rotated Image",
                     use_column_width=True)

            # Split transformation
            # split_option = st.radio("Apply split:", ("None", "Split"))
            # if split_option == "Split":
            #     red, green, blue = split_image(processed_image)
            #     st.image(red, caption="Red Channel", use_column_width=True)
            #     st.image(green, caption="Green Channel", use_column_width=True)
            #     st.image(blue, caption="Blue Channel", use_column_width=True)

            # Download button for the final processed image
            buf = BytesIO()
            processed_image.save(buf, format="JPEG")
            byte_processed = buf.getvalue()

            st.download_button(
                label="Download ALL Processed Image",
                data=byte_processed,
                file_name="allprocessed_image.jpg",
                mime="image/jpeg"
            )

# elif option == "Split":
#     red, green, blue = split_image(img)
#     st.image(red, caption="Red Channel", use_column_width=True)
#     st.image(green, caption="Green Channel", use_column_width=True)
#     st.image(blue, caption="Blue Channel", use_column_width=True)

#     cv2.imshow("red_img",red)
#     Image.open("red_img", red,formats="JPEG")

#     # Save the processed image to a buffer
#     processed_image.save(buf, format="JPEG")
#     byte_rotate = buf.getvalue()
# # Provide download button for the rotated image
#     btn_rotate = st.download_button(
#         label="Download R Image",
#         data=byte_rotate,
#         file_name="processed_image.jpg",
#         mime="image/jpeg"
#     )


if __name__ == "__main__":
    main()

 # Provide download button for the processed image
    # st.download_button(
    #     label="Download Processed Image",
    #     data=processed_image.tobytes(),
    #     file_name="processed_image.png",
    #     mime="image/jpg"
    # )

 # elif option == "Rotate":
    #     processed_image = rotate_image(img)
    #     st.image(processed_image, caption="Rotated Image",
    #              use_column_width=True)
    #     rotate_image_save = img.save( format="JPEG")
    #     byte_rotate = buf.getvalue()

    #     btn_rotate = st.download_button(
    #         label="Download Processed Image",
    #         data=byte_rotate,
    #         file_name="processed_image.png",
    #         mime="image/jpg"
    #     )
