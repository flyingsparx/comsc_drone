from cardiff_drone import Drone
drone = Drone(level = 1)
drone.takeoff()
for i in range(0,11):
    drone.move_forward()
drone.turn_left()
for i in range(0,8):
    drone.move_forward()
drone.land()
    