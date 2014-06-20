class Drone:
    def __init__(self, m):
        self.map = m
        self.finish = self.map['finish']
        self.obstacles = self.map['obstacles']
        self.x = self.map['start'][0]
        self.y = self.map['start'][1]
        self.z = self.map['start'][2]
        self.a = self.map['start'][3]
        self.ammo = self.map['ammo'] 
        self.inventory = []
        self.crashed = False
        self.finished = False
        self.status = "Ready"
        self.positions = [(self.x,self.y,self.z,self.a,self.status,self.inventory)]

    def __str__(self):
        return 'Cardiff Drone: ('+str(self.x)+','+str(self.y)+','+str(self.z)+')'

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
            
        self.finished = False
        if self.map['finish'][0] == self.x and self.map['finish'][1] == self.y and self.map['finish'][2] == self.z:
            self.finished = True
            for i in self.map['finish_items']:
                 if i not in self.inventory:
                    self.finished = False
                    break

        if self.finished == True:
            self.status = "Finished"
        elif self.crashed == True:
            self.status = "Crashed"
        elif self.z == 0:
            self.status = "Landed"
        elif self.z > 0:
            self.status = "Flying"

        new_invent = []
        for i in self.inventory:
            new_invent.append(i)
        self.positions.append((self.x,self.y,self.z,self.a,self.status,new_invent))        

    def pick_up(self):
        for i in self.map['items']:
            if i['location'][0] == self.x and i['location'][1] == self.y and i['location'][2] == self.z:
                self.inventory.append(i['name'])
                self.map['items'].remove(i)

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
                self.y-=1
            if self.a == 90:
                self.x+=1
            if self.a==180:
                self.y+=1
            if self.a == 270:
                self.x-=1
            self.get_state()

    def move_backward(self):
        if self.can_move(): 
            if self.a == 0:
                self.y+=1
            if self.a == 90:
                self.x-=1
            if self.a==180:
                self.y-=1
            if self.a == 270:
                self.x+=1
            self.get_state()
    
    def move_right(self):
        if self.can_move(): 
            if self.a == 0:
                self.x+=1
            if self.a == 90:
                self.y+=1
            if self.a==180:
                self.x-=1
            if self.a == 270:
                self.y-=1
            self.get_state()

    def move_left(self):
        if self.can_move(): 
            if self.a == 0:
                self.x-=1
            if self.a == 90:
                self.y-=1
            if self.a==180:
                self.x+=1
            if self.a == 270:
                self.y+=1
            self.get_state()
