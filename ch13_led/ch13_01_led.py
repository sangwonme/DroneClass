from djitellopy import Tello
import time

# create and connect
tello = Tello()
tello.connect()

while True:
  tello.send_expansion_command("led 255 0 0")
  time.sleep(1)
  tello.send_expansion_command("led 0 0 0")
  time.sleep(1)