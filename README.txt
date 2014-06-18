The School of Computer Science & Informatics Drone Game.

INSTRUCTIONS:
- Select a level to play
- Read the Map information for the level
- Take note of the drone's start position and bearing. Bearings are measured from North, so a bearing of 90 means the drone is facing East.
- Take note of the finish position. This is the position the drone must reach to complete the level.
- Your drone can collect items from around the map. Check the information to see if the map needs you to collect any items before finishing.
- Write your Python code to complete the map!

GENERAL:
Your Python code will start with something like this:
--------------------------------------------
    from cardiff_drone import Drone
    drone = Drone(level = 2)
--------------------------------------------
This code is automatically generated for you, so just leave that in. Write the rest of your code below these lines.

WRITING YOUR CODE:
All of your code involving Drone control should be done through the 'Drone' object created for you. For example, to move the Drone forwards one square in the direction its facing, use this command:
--------------------------------------------
    drone.move_forward()
--------------------------------------------

You need to write a series of commands, each on a new line, in order to complete most levels. For example, to move the drone forwards, turn left, and then move backwards, use something like this:
--------------------------------------------
    drone.move_forward()
    drone.turn_left()
    drone.move_backward()
--------------------------------------------

The Drone cannot move if it is on the ground (when the Altimeter shows an altitude of 0). To move the Drone off the ground, you need to use:
--------------------------------------------
    drone.takeoff()
--------------------------------------------
Once taken off, the Drone can move around normally.

The Status panel will update to show you the position of your Drone. Every time you click 'Run', the Drone will respawn and start from the beginning of your program. Beware of leaving the map's edges or flying too high, as this will crash the Drone!

Some levels require that you collect one or more items before reaching the finish. To collect an item, move the Drone to the square and altitude of the item, and use the command:
--------------------------------------------
    drone.pick_up()
--------------------------------------------
This will cause the drone to look in its current area for any items. If it finds any, it will add them to its inventory. There is no limit on how many items you can collect, but sometimes there are more items on the map than you need to finish with!

AVAILABLE DRONE FUNCTIONS:
The Drone understands the following commands:
--------------------------------------------
    takeoff()
        - Lift the Drone off the ground.
    land()
        - Land the drone in its current square.
    pick_up()
        - Pick up items in the Drone's current square and altitude.
    move_forward()
        - Move forward one square.
    move_backward()
        - Move backward one square.
    move_left()
        - Move one square to the left.
    move_right()
        - Move one square to the right.
    move_up()
        - Move one altitude level higher.
    move_down()
        - Move one altitude level lower.
    turn_right()
        - Turn right by 90 degrees.
    turn_left()
        - Turn left by 90 degrees
--------------------------------------------

The Drone lets you access the following information:
--------------------------------------------
    x
        - The current X-coordinate.
    y
        - The current Y-coordinate.
    z
        - The current height.
    a
        - The current bearing angle.
    inventory
        - The list of items the Drone is holding.
    status
        - The current status of the Drone (Ready, Landed, Flying, Crashed, etc.).
--------------------------------------------

STANDARD PYTHON PROCEDURES:
You can use any valid Python to control the Drone. Remember to check your indentation when using these Python constructs.

For example, if you want to move many squares forward at a time, you could use a for-loop. The following two lines of code move the Drone forwards by 14 squares:
--------------------------------------------
    for i in range(14):
        drone.move_forward()
--------------------------------------------

If-statements are useful if you want the Drone to perform an action if something has happened. For example, the following two lines of code land the Drone if it is already in the air:
--------------------------------------------
    if drone.z > 0:
        drone.land()
--------------------------------------------

You can, of course, combine multiple Python constructs. The following lines move the drone forward 3 squares if it is already in the air:
--------------------------------------------
    if drone.status == "Flying":
        for i in range(3);
            drone.move_forward()

Functions allow you to bundle many commands into a single, callable, routine. For example, this function moves the drone 3 squares forward and turns right:
--------------------------------------------
    function my_function(drone):
        for i in range(3):
            drone.move_forwards()
        drone.turn_right()
--------------------------------------------
Place functions above your own code (but below the automatically generated code), and then you can run them when you need to:
--------------------------------------------
    my_function(drone)
--------------------------------------------
Now this one line of code executes all of the commands inside the function 'my_function' every time it is called.