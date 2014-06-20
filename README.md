# Python drone game
## Cardiff University School of Computer Science and Informatics

An introduction to the basics of Python and the simple use of objects. The game involves guiding a UAV through a series of courses to complete particular tasks. The UI is ugly, but encourages basic problem-solving and good Python code-usage in that levels should be completed with the fewest lines of code possible.

Maps can be created and edited through simple alterations to `maps.json`. Instructions on this, and on installing and running the game, are found later in this document.

### Game instructions
- Select a level to play
- Read the Map information for the level
- Take note of the drone's start position and bearing. Bearings are measured from North, so a bearing of 90 means the drone is facing East.
- Take note of the finish position. This is the position the drone must reach to complete the level.
- Your drone can collect items from around the map. Check the information to see if the map needs you to collect any items before finishing.
- Write your Python code to complete the map!

### Drone initialisation 
Your Python code will start with something like this:
    from cardiff_drone import Drone
    drone = Drone(maps[2])
This code is automatically generated for you, so just leave that in. They are responsible for importing the Drone class and instantiating a new Drone object with the current map. Write the rest of your code below these lines.

## Writing your code
All of your code involving Drone control should be done through the 'Drone' object created for you. For example, to move the Drone forwards one square:
    drone.move_forward()

You need to write a series of commands, each on a new line, in order to complete most levels. For example, to move the drone forwards, turn left, and then move backwards, use something like this:
    drone.move_forward()
    drone.turn_left()
    drone.move_backward()

The Drone cannot move if it is on the ground (when the Altimeter shows an altitude of 0). To move the Drone off the ground, you need to use:
    drone.takeoff()
Once taken off, the Drone can move around normally.

The Status panel will update to show you the position of your Drone. Every time you click 'Run', the Drone will respawn and start from the beginning of your program. Beware of leaving the map's edges or flying too high, as this will crash the Drone!

Some levels require that you collect one or more items before reaching the finish. To collect an item, move the Drone to the square and altitude of the item, and use the command:
    drone.pick_up()
This will cause the drone to look in its current area for any items. If it finds any, it will add them to its inventory. There is no limit on how many items you can collect, but sometimes there are more items on the map than you need to finish with!

### Drone API documentation. 
The Drone understands the following commands:
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

### The Drone lets you access the following attributes:
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


### Standard Python routines: 
You can use any valid Python to control the Drone. Remember to check your indentation when using these Python constructs.

For example, if you want to move many squares forward at a time, you could use a for-loop. The following two lines of code move the Drone forwards by 14 squares:
    for i in range(14):
        drone.move_forward()

If-statements are useful if you want the Drone to perform an action if something has happened. For example, the following two lines of code land the Drone if it is already in the air:
    if drone.z > 0:
        drone.land()

You can, of course, combine multiple Python constructs. The following lines move the drone forward 3 squares if it is already in the air:
    if drone.status == "Flying":
        for i in range(3);
            drone.move_forward()

Functions allow you to bundle many commands into a single, callable, routine. For example, this function moves the drone 3 squares forward and turns right:
    function my_function(drone):
        for i in range(3):
            drone.move_forwards()
        drone.turn_right()
Place functions above your own code (but below the automatically generated code), and then you can run them when you need to:
    my_function(drone)
Now this one line of code executes all of the commands inside the function `my_function` every time it is called.

## Installation and usage
First, ensure an installation of Python 2.\* is present on your target system. In many cases, this can be achieved by downloading an installer from [Python's website](https://www.python.org). If under GNU/Linux, Python should be available in your distribution's repositories. For example, under Arch Linux:
    # pacman -S python2

Next, ensure the following Python dependencies are satisfied:
- `flask`
Python dependencies can be installed using `pip` or `easy_install`. See [this page](https://pypi.python.org/pypi/pip) for more information.

Clone this repository:
    $ git clone git@github.com:flyingsparx/comsc_drone.git
Change into the repository's local directory and run the manager:
    $ cd comsc_drone
    $ python manager.py
The manager, by default, runs on port 8080, so navigate to this port on your target host. 

## Creating and editing maps
Maps can be managed directly through the `maps.json` file. Each map is rectangular and consists of a number of squares (or cells). Objects in each cell, including the drone, also have a z-coordinate to represent its relative height above the ground. See the maps file for more information, and things should become clear. Generally, ensure each map object has the following attributes (even if they are empty):
- `name` - "<map name>": string/text
- `obstacles` - []: a list of 3D coordinate lists. e.g. `"obstacles": [[1,1,0],[1,1,1]]` creates two obstacles at x=1,y=1 at different heights.
- `finish` - [x,y,z]: the 3D (x,y,z) coordinate of the finish square.
- `start` - [x,y,z,a]: the 3D coordinate of the start sqaure and the initial direction the Drone faces (90,180,270,0).
- `size` - [w,h]: the width and height of the map.
- `ammo` - int: The initial ammo held by the drone (currently un-used but necessary for construction).
- `items` - [{ }]: List of item objects. Each item should have a `name` (string) and `location` ([x,y,z]) attribute.
- `finish_items` - [<string>]: List of item names required to complete the level. All of the names in this array must be present in the `items` array.
 
Note that the Drone will crash if it leaves the map's bounds or if it flies higher than z=9. Therefore, keep relevant items and the finish and start squares to a lower height.

## Caveats
It should be noted that this game does not prevent its users from running 'dangerous' Python code in its current state. This can be enforced by editing `manager.py` to check for imports of modules, such as `os` and `sys`, which may be used to cause harm to your system. The authors do not accept responsibility for any damage caused as a result of using any of the code in this repository!
