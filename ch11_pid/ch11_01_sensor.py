import time
from djitellopy import Tello

tello = Tello()
tello.connect()

tello.streamon()

while True:
    height = tello.get_height()
    baro = tello.get_barometer()
    dist = tello.get_distance_tof()

    print(round(height), round(baro), round(dist))