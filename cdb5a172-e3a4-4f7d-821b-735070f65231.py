from cardiff_drone import Drone
drone = Drone(level = 3)

drone.takeoff()
for i in range(0,8):
    drone.move_forward()
drone.turn_right()
for i in range(0,7):
    drone.move_forward()
drone.land()
drone.pick_up()   