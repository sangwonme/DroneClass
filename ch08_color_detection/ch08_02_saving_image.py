import cv2
import numpy as np
# from skimage.measure import label

# To use a video file instead of a camera, pass the video file path instead of the camera index
cap = cv2.VideoCapture(0)

while True:
    # Read the frame
    _, img = cap.read()

    # flip
    img = cv2.flip(img, 1)

    # Convert the image to the HSV color space
    hsv_image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Define the lower and upper bounds for the blue color in HSV
    lower_blue = np.array([70, 50, 50])
    upper_blue = np.array([130, 255, 255])

    # Threshold the image to get only the blue color
    blue_mask = cv2.inRange(hsv_image, lower_blue, upper_blue)

    # connect group
    # labeled_mask = label(blue_mask, connectivity=2)

    # Apply a bitwise AND operation to the image using the blue mask
    blue_result = cv2.bitwise_and(img, img, mask=blue_mask)
    
    # Display
    cv2.imshow('Original Image', img)
    cv2.imshow('Blue Detection Result', blue_result)

    # Stop if escape key is pressed
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break
    # Save camera image when key 'y' is pressed.
    if k==ord('y'):
        cv2.imwrite('./bluesample.png', img)
        break
    # Save camera image and filtered image when key 'x' is pressed.
    if k==ord('x'):
        cv2.imwrite('./bluesample_orig.png', img)
        cv2.imwrite('./bluesample_filt.png', blue_result)
        break

        
# Release the VideoCapture object
cap.release()
cv2.destroyAllWindows()
