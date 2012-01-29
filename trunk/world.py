import random
from actors import *
from ui import Scoreboard

class World:
    def __init__(self, graphics, player):
        self.graphics = graphics;
        self.player = player
        self.enemies = {}
        self.spawn_rate = 3000
        self.spawn_timer = self.spawn_rate

    def update(self, delta):
        # Generate new enemies
        self.spawn_timer -= delta
        if self.spawn_timer <= 0:
            self.spawn_timer = self.spawn_rate
            # Chance for a new enemy
            #if random.randint(0, 8) == 0:
            self.add_enemy(self.__get_random_shape(), self.__get_random_size(), self.__get_random_rot(), self.__get_random_color(), self.__get_random_pos())
        
        pass   
            
    def create_shape(self, shape_type, size, rotation, color):
        if shape_type == "hexagon":
            return Hexagon(size, rotation, color)
        elif shape_type == "octagon":
            return Octagon(size, rotation, color)
        elif shape_type == "pentagon":
            return Pentagon(size, rotation, color)
        elif shape_type == "square":
            return Square(size, rotation, color)
        else: #tri
            return Tri(size, rotation, color)
        
    def add_enemy(self, shape_type, size, rotation, color, pos = (0,0)):
        shape = self.create_shape(shape_type, size, rotation, color)
        shape.rect.move_ip(pos)
        self.enemies[shape.id] = shape
        self.graphics.add_player_shape(shape)

    def remove_enemy(self, shapeid):
        if shapeid in self.enemies:
            self.graphics.remove_player_shape(self.enemies[shapeid])
            del self.enemies[shapeid]

    def __get_random_color(self):
        x = random.randint(0, 3)
        if x == 0:
            return "yellow"
        elif x == 1:
            return "white"
        elif x == 2:
            return "green"
        else:
            return "purple"
           
    def __get_random_shape(self):
        x = random.randint(0, 4)
        if x == 0:
            return "hexagon"
        elif x == 1:
            return "octagon"
        elif x == 2:
            return "pentagon"
        elif x == 3:
            return "square"
        else:
            return "tri"       
        
    def __get_random_size(self):
        x = random.randint(0, 2)
        if x == 0:
            return 32
        elif x == 1:
            return 64
        else:
            return 128  
        
    def __get_random_rot(self):
        x = random.randint(0, 6) 
        if x == 0:
            return 0
        elif x == 1:
            return 40
        elif x == 2:
            return 70
        elif x == 3:
            return 150
        elif x == 4:
            return 220
        elif x == 5:
            return 270
        else:
            return 310   
        
    def __get_random_pos(self):
        r = random.randint(0, 6) 
        
        #if (
        
        x = random.randint(-150, 150) 
        y = random.randint(-150, 150)
        return (x,y)