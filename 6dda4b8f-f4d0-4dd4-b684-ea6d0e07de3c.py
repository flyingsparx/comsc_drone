from cardiff_drone import Drone
drone = Drone(level = 2)

def thing(drone):
	for i in range(15):
		drone.move_forward()
	drone.turn_left()

drone.takeoff()
thing()
thing()

drone.land()
    