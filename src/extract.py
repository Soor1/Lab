import cv2 
import os 

cam = cv2.VideoCapture("/Users/soorhansalia/Lab/videos/og_east.mp4") 

try: 
    
    if not os.path.exists('og_east_images'): 
        os.makedirs('og_east_images') 

except OSError: 
    print ('Error: Creating directory of data') 

currentframe = 0


while(True): 
    
    ret,frame = cam.read() 

    if ret: 
        name = './og_east_images/frame' + str(currentframe) + '.jpg'
        print ('Creating...' + name) 

        cv2.imwrite(name, frame) 

        currentframe += 1
    else: 
        break

cam.release() 
cv2.destroyAllWindows() 