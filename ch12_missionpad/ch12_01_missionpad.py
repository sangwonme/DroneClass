from djitellopy import Tello

# Create the Tello drone object
tello = Tello()

tello.connect()

tello.enable_mission_pads()

print(tello.get_mission_pad_id())