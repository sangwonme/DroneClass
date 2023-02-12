from djitellopy import Tello
import time

tello = Tello()
tello.connect()
# tello.takeoff()

# tello.send_command_without_return('rc 10 0 40 0')
# time.sleep(20)

tello.land()