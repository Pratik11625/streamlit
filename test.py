import streamlit as st
# import cv2
from PIL import Image, ImageFilter
import numpy as np

# Function to convert image to grayscale


def grayscale(image):
    grayscale_image = image.convert('L')
    grayscale_image1 = grayscale_image.filter(ImageFilter.SMOOTH_MORE)
    grayscale_image2 = grayscale_image1.filter(ImageFilter.SHARPEN)

    return grayscale_image2

# Function to apply image blur


# def apply_blur(image):
#     blur_strength = st.slider("Select blur strength:", 1, 31, 3)
#     blurred_image = image.filter(ImageFilter.GaussianBlur(blur_strength))
#     return blurred_image

# def apply_blur(image):
    # if option_2 == "Gaussianblur":
    #     blur_strength = st.slider("Select blur strength:", 1, 31, 3)
    #     blurred_image = image.filter(ImageFilter.GaussianBlur(blur_strength))
    #     st.image(blurred_img, caption="Blurred Image",
    #          use_column_width=True)
    # elif option_2 == "Boxblur":
    #     blur_strength = st.slider("Select blur strength:", 1, 31, 3)
    #     blurred_image = image.filter(ImageFilter.BoxBlur(blur_strength))
    #     st.image(blurred_img, caption="Blurred Image",
    #          use_column_width=True)


def GaussianBlur(image):
    blur_strength = st.slider("Select blur strength:", 1, 31, 3)
    blurred_image = image.filter(ImageFilter.GaussianBlur(blur_strength))
    return blurred_image


def BoxBlur(image):
    blur_strength = st.slider("Select blur strength:", 1, 31, 3)
    blurred_image = image.filter(ImageFilter.BoxBlur(blur_strength))
    return blurred_image

# Function to detect edges in the image


def detect_edges(image, threshold1, threshold2):
    # Convert the PIL image to a numpy array
    img_array = np.array(image)

    # Perform Canny edge detection
    edges = cv2.Canny(img_array, threshold1, threshold2)

    # Convert the resulting edges back to a PIL image
    edges_image = Image.fromarray(edges)

    return edges_image


def edge_detection_1(image):
    image = image.convert("L")
    image = image.filter(ImageFilter.FIND_EDGES)
    image = image.filter(ImageFilter.EDGE_ENHANCE_MORE)
    image = image.filter(ImageFilter.FIND_EDGES)
    st.image(image, caption="Edge Detected Image",
             use_column_width=True)

# Function to crop the image


def crop_image(image, left, top, right, bottom):
    cropped_image = image.crop((left, top, right, bottom))
    print(image.size)
    return cropped_image


def FLIP_LEFT_RIGHT(image):
    flipped_image = image.transpose(Image.FLIP_LEFT_RIGHT)
    return flipped_image


def FLIP_TOP_BOTTOM(image):
    flipped_image = image.transpose(Image.FLIP_TOP_BOTTOM)
    # flipped_image1 = cv2.flip(image,0)
    return flipped_image


def ROTATE_90(image):
    r1 = st.slider("Select Rotate deg:", 0, 360, 45)
    rotate_image = image.rotate(r1, expand=True)
    # flipped_image1 = cv2.flip(image,0)
    return rotate_image


def show(image):
    # file = ("images.png")
    # file = image.point(lambda x: 0 if x == 255 else 255)
    # file.show()
    # file.load()
    # return file

    red, green, blue = image.split()
    return red, green, blue


# Main function to run the Streamlit app


def main():
    # Set title of the app
    st.title("Image Processing App")

    # Upload image
    uploaded_image = st.file_uploader(
        "Choose an image", type=["jpg", "jpeg", "png"])

    if uploaded_image is not None:
        # Display the uploaded image
        img = Image.open(uploaded_image)
        st.image(img, caption="Original Image", use_column_width=True)

        # Buttons for image processing
        option = st.radio("Choose an option:", ("Grayscale",
                          "Blur", "Edge Detection", "Edge Detection_1", "Crop", "Transpose", "Split"))

        if option == "Grayscale":
            grayscale_img = grayscale(img)
            st.image(grayscale_img, caption="Grayscale Image",
                     use_column_width=True)

          # elif option == "Blur":
          #     blurred_img = apply_blur(img)
          #     st.image(blurred_img, caption="Blurred Image",
          #      use_column_width=True)

        elif option == "Blur":
            option_2 = st.radio("Choose an option:", ("Gaussianblur",
                                                      "Boxblur"))
        # blurred_img = apply_blur(img)
            if option_2 == "Gaussianblur":
                blurred_img = GaussianBlur(img)
                st.image(blurred_img, caption="Blurred Image",
                         use_column_width=True)

            elif option_2 == "Boxblur":
                blurred_img = BoxBlur(img)
                st.image(blurred_img, caption="Blurred Image",
                         use_column_width=True)

        elif option == "Edge Detection":
            Image.open(uploaded_image)
    #     threshold1 = st.slider("Select threshold 1:", 0, 255, 50)
    #     threshold2 = st.slider("Select threshold 2:", 0, 255, 150)
    #     edge_img = detect_edges(img, threshold1, threshold2)
    #     st.image(edge_img, caption="Edge Detected Image",
    #              use_column_width=True)

        elif option == "Edge Detection_1":
            image = Image.open(uploaded_image)
            edge_detection_1(image)

        elif option == "Crop":
            st.header("keep the top side < bottom side")
            left = st.slider("Left side:", 0, img.width, 0)
            top = st.slider("Top side:", 0, img.height, 0)
            right = st.slider("Right side:", 0, img.width, img.width)
            bottom = st.slider("Bottom side:", 0, img.height, img.height)
            cropped_img = crop_image(img, left, top, right, bottom)
            st.image(cropped_img, caption="Cropped Image",
                     use_column_width=True)

        elif option == "Transpose":
            option1 = st.radio("Choose an option:", ("FLIP_LEFT_RIGHT",
                                                     "FLIP_TOP_BOTTOM", "ROTATE"))
            if option1 == "FLIP_LEFT_RIGHT":
                flipped_img = FLIP_LEFT_RIGHT(img)
                st.image(flipped_img, caption="Flipped Left to Right Image",
                         use_column_width=True)

            elif option1 == "FLIP_TOP_BOTTOM":
                flipped_img = FLIP_TOP_BOTTOM(img)
                st.image(flipped_img, caption="Flipped TOP TO BOTTOM Image",
                         use_column_width=True)
                # blue = st.button("blue")
                # if blue == True:
                #     btn = st.download_button(
                #         label='Download img file',
                #         data=img,
                #         file_name="new_file.jpge",
                #         mime="image/png")

            elif option1 == "ROTATE":
                rotate_image = ROTATE_90(img)
                st.image(rotate_image, caption="Rotate_90 deg Image",
                         use_column_width=True)

        elif option == "split":
            # uploaded_image.show()
            # red, green, blue = Image.split(uploaded_image)
            # red.show()
            # green.show()
            # blue.show()

            # file = "cam103_person_75.jpg"
            # with Image.open(file) as img:
            #     img.load()
            # for _ in range(3):
            #     img = img.filter(ImageFilter.MinFilter(3))

            red, green, blue = show(img)
            st.image(red, caption="Red Channel", use_column_width=True)
            st.image(green, caption="Green Channel", use_column_width=True)
            st.image(blue, caption="Blue Channel", use_column_width=True)
        # pass

        # step = erode(12,img)
        # Image.open(step)
        else:

            st.title("Image Splitting App")
            st.subheader('Download Grayscale Image')
        #     btn = st.download_button(
        #     label='Download Grayscale Image',
        #     data=grayscale_image2,
        #     file_name="grayscale_image.jpg",  # Change the file name and extension as needed
        #     mime="image/jpeg"  # Change the MIME type if necessary
        # )
            blue = st.button("blue")
            if blue == True:
                btn = st.download_button(
                    label='Download img file',
                    data=flipped_image,
                    file_name="new_file.jpge",
                    mime="image/png"
                )


    # Run the main function
if __name__ == "__main__":
    main()
