import os
import json
from google.cloud import vision

# Set the environment variable for the API key
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/Users/soorhansalia/Lab/key.json'

def detect_text(image_path):
    # Create a client
    client = vision.ImageAnnotatorClient()
    
    # Load the image
    with open(image_path, 'rb') as image_file:
        content = image_file.read()
    
    # Construct an image instance
    image = vision.Image(content=content)
    
    # Perform text detection
    response = client.text_detection(image=image)
    texts = response.text_annotations
    
    # Print out the detected text
    if texts:
        for text in texts:
            print(f"Detected text: {text.description}")
    
    # Return the detected text or None if no text found
    return texts[0].description if texts else None

folder_path = '/Users/soorhansalia/Lab/images/stake_images'
output_json_path = '/Users/soorhansalia/Lab/outputs/google_vision_output.json'

ocr_results = {}


# Loop through the images and perform OCR
for i in range(30, 42):
    frame_filename = f'frame{i}.jpg'
    frame_path = os.path.join(folder_path, frame_filename)
    
    if os.path.isfile(frame_path):
        # Perform OCR
        extracted_texts = detect_text(frame_path)
        
        # Store the extracted texts in the dictionary
        ocr_results[frame_filename] = extracted_texts

# Save the OCR results to a JSON file
with open(output_json_path, 'w') as json_file:
    json.dump(ocr_results, json_file, indent=4)

print(f"OCR results saved to {output_json_path}")


   