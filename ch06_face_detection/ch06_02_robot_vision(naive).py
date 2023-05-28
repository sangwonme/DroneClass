from djitellopy import Tello
import cv2, math, time

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

tello = Tello()
tello.connect()
tello.streamon()
frame_read = tello.get_frame_read()

tello.takeoff()

while True:
    # In reality you want to display frames in a seperate thread. Otherwise
    #  they will freeze while the drone moves.
    img = frame_read.frame

    # flip
    img = cv2.flip(img, 1)

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Draw the rectangle around each face
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

        # Calculate the center point
        center_x = x + w//2
        center_y = y + h//2

        # Draw the red dot
        cv2.circle(img, (center_x, center_y), radius=10, color=(0, 0, 255), thickness=-1)

        # Put the text (coordinate)
        # load font
        font = cv2.FONT_HERSHEY_SIMPLEX 
        cv2.putText(img, '({}, {})'.format(center_x, center_y), (x, y-10), font, 2, (0, 255, 0), 2)

    cv2.imshow("drone", img)

    key = cv2.waitKey(1) & 0xff
    if key == 27: # ESC
        break
    elif key == ord('w'):
        tello.move_forward(30)
    elif key == ord('s'):
        tello.move_back(30)
    elif key == ord('a'):
        tello.move_left(30)
    elif key == ord('d'):
        tello.move_right(30)
    elif key == ord('e'):
        tello.rotate_clockwise(30)
    elif key == ord('q'):
        tello.rotate_counter_clockwise(30)
    elif key == ord('r'):
        tello.move_up(30)
    elif key == ord('f'):
        tello.move_down(30)
    else:
        isMove = False
    
tello.land()