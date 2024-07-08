import easyocr
import os
import certifi
import json

os.environ['SSL_CERT_FILE'] = certifi.where()

reader = easyocr.Reader(['en'])

folder_path = '/Users/soorhansalia/Lab/images/test'
output_json_path = '/Users/soorhansalia/Lab/outputs/test.json'

ocr_results = {}

# /Users/soorhansalia/Lab/images/stake_images/frame14.jpg
# /Users/soorhansalia/Lab/images/image.jpg

for i in range(15, 31):
    frame_filename = f'frame{i}.jpg'
    frame_path = os.path.join(folder_path, frame_filename)
    
    if os.path.isfile(frame_path):
        # Perform OCR
        text_results = reader.readtext(frame_path)
        
        # Extract only the text from the results
        extracted_texts = [text[1] for text in text_results]
        
        # Convert all text entries to strings (if they aren't already)
        extracted_texts = [str(text) for text in extracted_texts]
        
        # Store the extracted texts in the dictionary
        ocr_results[frame_filename] = extracted_texts

# Save the OCR results to a JSON file
with open(output_json_path, 'w') as json_file:
    json.dump(ocr_results, json_file, indent=4)

print(f"OCR results saved to {output_json_path}")

