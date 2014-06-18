import json

class Drone:
    def __init__(self, level=1):
        self.map = self.get_map(level)
        self.finish = self.map['finish']
        self.obstacles = self.map['obstacles']
        self.x = self.map['start'][0]
        self.y = self.map['start'][1]
        self.z = self.map['start'][2]
        self.a = self.map['start'][3]
        self.ammo = 10
        self.inventory = []
        self.crashed = False
        self.finished = False
        self.status = "Ready"
        self.positions = [(self.x,self.y,self.z,self.a,self.status,self.inventory)]

    def __str__(self):
        return 'Drone: ('+str(self.x)+','+str(self.y)+','+str(self.z)+')'

    def get_map(self, map_id):
        f = open("maps.json", "r")
        text = f.read()
        maps = json.loads(text)['maps']
        m = None
        for map in maps:
            if map['id'] == str(map_id):
                m = map
        return m  
    
    def can_move(self):
        if self.crashed == True or self.finished == True or self.z == 0:
            return False
        return True

    def get_stats(self):
        return (self.positions)

    def get_state(self):
        for o in self.obstacles:
            if o[0] == self.x and o[1] == self.y and o[2] == self.z:
                self.crashed = True
        if self.x < 1 or self.y < 1 or self.x > self.map['size'][0] or self.y > self.map['size'][1] or self.z > 9:
            self.crashed = True
            
        finished = False
        if self.map['finish'][0] == self.x and self.map['finish'][1] == self.y and self.map['finish'][2] == self.z:
            finished = True
            for i in self.map['finish_items']:
                 if i not in inventory:
                    finished = False
                    break
        if finished == True:
            self.finished = True

        if self.finished == True:
            self.status = "Finished"
        elif self.crashed == True:
            self.status = "Crashed"
        elif self.z == 0:
            self.status = "Landed"
        elif self.z > 0:
            self.status = "Flying"

        self.positions.append((self.x,self.y,self.z,self.a,self.status,self.inventory))        

    def takeoff(self):
        if self.crashed == False and self.finished == False:
            self.z = 2
            self.get_state()

    def land(self):
        if self.crashed == False and self.finished == False:
            self.z = 0
            self.get_state()

    def move_up(self):
        if self.can_move(): 
            self.z += 1
            self.get_state()
    
    def move_down(self):
        if self.can_move(): 
            self.z -= 1
            self.get_state()

    def turn_right(self):
        if self.can_move(): 
            self.a += 90
            if self.a >= 360:
                diff = self.a-diff
                self.a = diff
            self.get_state()
    
    def turn_left(self):
        if self.can_move(): 
            self.a -= 90
            if self.a < 0:
                diff = 0-self.a
                self.a = diff
            self.get_state()

    def move_forward(self):
        if self.can_move(): 
            if self.a == 0:
                self.y+=1
            if self.a == 90:
                self.x+=1
            if self.a==180:
                self.y-=1
            if self.a == 270:
                self.x-=1
            self.get_state()

    def move_backward(self):
        if self.can_move(): 
            if self.a == 0:
                self.y-=1
            if self.a == 90:
                self.x-=1
            if self.a==180:
                self.y+=1
            if self.a == 270:
                self.x+=1
            self.get_state()
    
    def move_right(self):
        if self.can_move(): 
            if self.a == 0:
                self.x+=1
            if self.a == 90:
                self.y-=1
            if self.a==180:
                self.x-=1
            if self.a == 270:
                self.y+=1
            self.get_state()

    def move_left(self):
        if self.can_move(): 
            if self.a == 0:
                self.x-=1
            if self.a == 90:
                self.y+=1
            if self.a==180:
                self.x+=1
            if self.a == 270:
                self.y-=1
            self.get_state()
