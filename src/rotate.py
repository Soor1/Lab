import os
from PIL import Image

def rotate_and_resize_images(directory, size=(1300, 1300)):
    # List all files in the directory
    for filename in os.listdir(directory):
        # Construct full file path
        file_path = os.path.join(directory, filename)
        print(f"Processing file: {file_path}")

        # Check if the file is an image (you can add more extensions if needed)
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff')):
            try:
                # Open an image file
                with Image.open(file_path) as img:
                    # Rotate image by 90 degrees counter-clockwise
                    rotated_img = img.rotate(90, expand=True)
                    # Resize image to the specified size
                    resized_img = rotated_img.resize(size, Image.LANCZOS)
                    # Save it back to the directory, overwriting the original
                    resized_img.save(file_path)
                    print(f"Saved image: {file_path}")
            except Exception as e:
                print(f"Error processing image {file_path}: {e}")

if __name__ == "__main__":
    # Specify the directory containing the images
    image_directory = '/Users/soorhansalia/Lab/Stake'
    rotate_and_resize_images(image_directory)
