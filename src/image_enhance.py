
import cv2 
import matplotlib.pyplot as plt 
import numpy as np 
  
# Opens the image file 
image = cv2.imread('/Users/soorhansalia/Lab/images/stake_images/frame32.jpg') 
  
#Plot the original image 
plt.subplot(1, 2, 1) 
plt.title("Original") 
plt.imshow(image) 
  
# Create the sharpening kernel 
kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]]) 
  
# Sharpen the image 
sharpened_image = cv2.filter2D(image, -1, kernel) 
  
#Save the image 
cv2.imwrite('sharpened_image.jpg', sharpened_image) 
  
#Plot the sharpened image 
plt.subplot(1, 2, 2) 
plt.title("Sharpening") 
plt.imshow(sharpened_image) 
plt.show()