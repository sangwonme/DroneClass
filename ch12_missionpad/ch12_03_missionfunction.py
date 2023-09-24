from djitellopy import Tello

# create and connect
tello = Tello()
tello.connect()

# configure drone
tello.enable_mission_pads()
tello.set_mission_pad_detection_direction(2) 

tello.takeoff()

pad = tello.get_mission_pad_id()

# 함수 : 새로운 감지되면 방향을 바꾸고 위로 올라간다
def updateMove(pad):
    tmp = tello.get_mission_pad_id()
    if tmp != -1 and tmp != pad:
        tello.move_up(20)
        
        return tmp
    return pad

# 2번 감지했을 때는 flip_forward
# 3번 감지했을 때는 flip_back

while pad != 4:
    pad = updateMove(pad)
    if pad == 1:
        tello.move_forward(20)
    elif pad == 2:
        tello.move_right(20)
    elif pad == 3:
        tello.move_back(20)


# graceful termination
tello.disable_mission_pads()
tello.land()
tello.end()

