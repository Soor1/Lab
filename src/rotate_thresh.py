import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load the image
image_path = '/Users/soorhansalia/Lab/images/stake_images/frame14.jpg'
image = cv2.imread(image_path)

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Binarize the image using a threshold
_, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Apply Canny edge detection
edges = cv2.Canny(binary, 50, 150)

# Find lines using HoughLinesP
lines = cv2.HoughLinesP(edges, 1, np.pi / 180, threshold=100, minLineLength=100, maxLineGap=10)

# Find the longest line
max_length = 0
longest_line = None
if lines is not None:
    for line in lines:
        x1, y1, x2, y2 = line[0]
        length = np.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        if length > max_length:
            max_length = length
            longest_line = line[0]

# Draw the longest line on a copy of the original image
line_image = image.copy()
if longest_line is not None:
    x1, y1, x2, y2 = longest_line
    cv2.line(line_image, (x1, y1), (x2, y2), (0, 255, 0), 2)

    # Display the longest line before rotation
    # fig, ax = plt.subplots(1, 1, figsize=(10, 10))
    # ax.imshow(cv2.cvtColor(line_image, cv2.COLOR_BGR2RGB))
    # ax.set_title('Longest Line Detected')
    # ax.axis('off')
    # plt.show()
    
    # Calculate the angle to rotate (clockwise)
    angle = np.degrees(np.arctan2(y2 - y1, x2 - x1))
    
    # Rotate the image to make the line horizontal (clockwise)
    (h, w) = image.shape[:2]
    center = (w / 2, h / 2)
    # Use a positive angle for clockwise rotation
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated_180 = cv2.warpAffine(image, M, (w, h)) # change back to rotated

    # Rotate the image an additional 180 degrees clockwise
    # M_180 = cv2.getRotationMatrix2D(center, 180, 1.0)
    # rotated_180 = cv2.warpAffine(rotated, M_180, (w, h))

    # Apply adaptive mean thresholding
    rotated_gray = cv2.cvtColor(rotated_180, cv2.COLOR_BGR2GRAY)
    adaptive_thresh = cv2.adaptiveThreshold(rotated_gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
    
    cv2.imwrite('rotated_180.jpg', rotated_180)
    cv2.imwrite('adaptive_thresh.jpg', adaptive_thresh)

    # # Display the results
    # fig, axes = plt.subplots(1, 5, figsize=(25, 10))
    # axes[0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    # axes[0].set_title('Original Image')
    # axes[0].axis('off')

    # axes[1].imshow(cv2.cvtColor(edges, cv2.COLOR_BGR2RGB))
    # axes[1].set_title('Edges')
    # axes[1].axis('off')

    # axes[2].imshow(cv2.cvtColor(rotated, cv2.COLOR_BGR2RGB))
    # axes[2].set_title('Rotated Image')
    # axes[2].axis('off')

    # axes[3].imshow(cv2.cvtColor(rotated_180, cv2.COLOR_BGR2RGB))
    # axes[3].set_title('Rotated 180 Degrees Image')
    # axes[3].axis('off')

    # axes[4].imshow(adaptive_thresh, cmap='gray')
    # axes[4].set_title('Adaptive Mean Thresholding')
    # axes[4].axis('off')

    # plt.show()
else:
    print("No lines were detected.")