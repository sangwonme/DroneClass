import cv2
import numpy as np
from djitellopy import Tello

# --------------------------------------------------------------------------------
# color detection
def color_detect(input_img):
    frame = input_img

    # Convert the image from BGR to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define the range of blue color in HSV
    lower_blue = np.array([70, 50, 50])
    upper_blue = np.array([130, 255, 255])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Perform morphological operations to remove noise and emphasize the detected object
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    # Find contours in the mask and initialize the current
    contours, _ = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Only proceed if at least one contour was found
    if len(contours) > 0:
        # Find the largest contour in the mask, then use it to compute the minimum enclosing circle and centroid
        c = max(contours, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)
        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

        # Only proceed if the radius meets a minimum size
        if radius > 10:
            # Draw the circle and centroid on the frame,
            cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
            cv2.circle(frame, center, 5, (0, 0, 255), -1)
    
    return frame, mask

# --------------------------------------------------------------------------------

# Initialize the Tello drone
tello = Tello()

tello.connect()
tello.streamon()

frame_read = tello.get_frame_read()

while True:
    # Get the current frame from the Tello drone's video stream
    frame = frame_read.frame

    # function call
    frame, mask = color_detect(frame)

    # Display the resulting frames
    cv2.imshow('Original', frame)
    cv2.imshow('Mask', mask)

    # Quit the program by pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# After the loop release the cap object
tello.streamoff()
# Destroy all the windows
cv2.destroyAllWindows()
