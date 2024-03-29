# simple example demonstrating how to control a Tello using your keyboard.
# For a more fully featured example see manual-control-pygame.py
# 
# Use W, A, S, D for moving, E, Q for rotating and R, F for going up and down.
# When starting the script the Tello will takeoff, pressing ESC makes it land
#  and the script exit.

from djitellopy import Tello
import cv2, math, time

import matplotlib.pyplot as plt
import numpy as np

y = []

tello = Tello()
tello.connect()
tello.streamon()
frame_read = tello.get_frame_read()

tello.takeoff()

while True:
    # In reality you want to display frames in a seperate thread. Otherwise
    #  they will freeze while the drone moves.
    img = frame_read.frame
    cv2.imshow("drone", img)

    isMove = True

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
    
    print(tello.get_current_state()['baro'])
    y.append(tello.get_current_state()['baro'])

tello.land()

y = np.array(y)

# Create the figure and axis objects
fig, ax = plt.subplots(1, 2)

# Plot the data as a line
ax[0].plot(y)

# Create a histogram of the data
ax[1].hist(y)

# Set the labels and title
ax[0].set_title('Noise Line Plot')
ax[1].set_title('Noise Histogram')

# Show the figure
fig.savefig('./baro_noise.png', dpi=100)
plt.show()