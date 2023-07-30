import time
from djitellopy import Tello
from simple_pid import PID

# PID constants
Kp = 1.0
Ki = 0.0
Kd = 0.0

# Target altitude
target_altitude = 100  # in cm

# Create the PID controller
pid = PID(Kp, Ki, Kd, setpoint=target_altitude)

# Create the Tello drone object
tello = Tello()

try:
    # Connect to the drone
    tello.connect()

    # Takeoff
    tello.takeoff()

    while True:
        # Get the current altitude
        current_altitude = tello.get_distance_tof()

        # Calculate the control variable (throttle)
        throttle = pid(current_altitude)

        # Send the control variable to the drone
        tello.send_rc_control(0, 0, int(throttle), 0)

        # Sleep for a bit
        time.sleep(0.01)

except KeyboardInterrupt:
    # Land the drone when Ctrl+C is pressed
    tello.land()
