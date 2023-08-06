import time
from djitellopy import Tello
from simple_pid import PID
from matplotlib import pyplot as plt

# PID constants
Kp = 0.3
Ki = 0.0
Kd = 0.0

# Target altitude
target_altitude = 100  # in cm

# Create the PID controller
pid = PID(Kp, Ki, Kd, setpoint=target_altitude)

# Create the Tello drone object
tello = Tello()

# Create Datas to plot
datas = []

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

        # datas
        datas.append([current_altitude, throttle, target_altitude])

except KeyboardInterrupt:
    # Unpacking the y-values
    y1 = [item[0] for item in datas]
    y2 = [item[1] for item in datas]
    y3 = [item[2] for item in datas]

    # Generate x-values (assuming each set of y-values corresponds to a new time point)
    x = list(range(len(datas)))

    # Plotting the data
    plt.plot(x, y1, label="sensor")
    plt.plot(x, y2, label="actuation")
    plt.plot(x, y3, label="target sensor")

    # Setting plot properties
    plt.title("Y-values over time")
    plt.xlabel("Time")
    plt.ylabel("Value")
    plt.legend()

    plt.show()

    # Land the drone when Ctrl+C is pressed
    tello.land()

    


    
