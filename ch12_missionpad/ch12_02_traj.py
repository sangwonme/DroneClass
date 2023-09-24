from djitellopy import Tello

# create and connect
tello = Tello()
tello.connect()

# configure drone
tello.enable_mission_pads()
tello.set_mission_pad_detection_direction(2) 

tello.takeoff()

pad = tello.get_mission_pad_id()



print('pad number is :', pad)

while pad != 2:
    tello.move_forward(20)
    pad = tello.get_mission_pad_id()
    print(pad)

# graceful termination
tello.disable_mission_pads()
tello.land()
tello.end()