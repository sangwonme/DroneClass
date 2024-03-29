import cv2

# Load the cascade
try:
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
except:
    face_cascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')

# To use a video file instead of a camera, pass the video file path instead of the camera index
cap = cv2.VideoCapture(0)

while True:
    # Read the frame
    _, img = cap.read()

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

    # TODO : 사람 명수를 출력하시오
    print(len(faces))


    # Display
    cv2.imshow('img', img)

    # Stop if escape key is pressed
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break
        
# Release the VideoCapture object
cap.release()
cv2.destroyAllWindows()
