import random
from copy import deepcopy

import pygame

from actors import Head, Tri
from vector2 import Vector2

import globalvars
import imageutils

class Player:
    
    def __init__(self, graphics):  
        self.graphics = graphics
        
        self.head = Head(32, 0)
        self.graphics.add_player_shape(self.head)
        self.head.rect.move_ip(512, 384)
        self.total_size = 1;
        
        #Graph of each shape id and the ids of the shapes connected to it
        self.shape_graph = {self.head.id: []}
        self.attached_shapes = {self.head.id: self.head}
        
        self.invincible = False
        self.invincible_rate = 1200
        self.invincible_timer = self.invincible_rate
        
    def update(self, delta):
        if self.invincible:
            self.invincible_timer -= delta
            if self.invincible_timer <= 0: 
                self.set_invis(False)
           
    def __get_open_shapes(self):
        open_shape_ids = []
        for shape_id, attached in self.shape_graph.items():
            if len(attached) < self.attached_shapes[shape_id].sides:
                open_shape_ids.append(shape_id)
        return open_shape_ids
        
    def __add_shape(self, shape, leaf_id):
        leaf_shape = self.attached_shapes[leaf_id]
        
        #Create a vector between the two shapes to figure out how to move it to it but without collision
        #shape_vector = Vector2.from_points((shape.rect.x, shape.rect.y), (leaf_shape.rect.x, leaf_shape.rect.y))
        #shape.rect.move(shape_vector.x - (shape.rect.width + leaf_shape.rect.width), shape_vector.y - (shape.rect.height + leaf_shape.rect.height))
        
        shape.rect = leaf_shape.rect.copy()
        shape.rect.move_ip(-globalvars.GLOBAL_DELTA_X * (leaf_shape.rect.width/2 - shape.rect.width/2), -globalvars.GLOBAL_DELTA_Y * (leaf_shape.rect.height/2 - shape.rect.height/2))   
        shape.rotation = leaf_shape.rotation;
        
        
        
        self.attached_shapes[shape.id] = shape
        self.shape_graph[shape.id] = [leaf_id]
        self.shape_graph[leaf_id].append(shape.id)
        
        shape.parent = leaf_shape
        
    def __find_attached_triangles(self, shape_ids):
        triangles = []
        for shape_id in shape_ids:
            shape = self.attached_shapes[shape_id]
            if type(shape) is Tri:
                triangles.append(shape)
        return triangles
        
    def find_shape_path(self, graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if not graph.has_key(start):
            return None
        for node in graph[start]:
            if node not in path:
                newpath = find_path(graph, node, end, path)
                if newpath: return newpath
        return None
    
    def kill_shape(self, dead_shape):

        print 'Kill Shape called. Shape: %s, Invincible: %s' % (dead_shape, self.invincible)

        if type(dead_shape) is Head and len(self.attached_shapes) <= 1:
            globalvars.run_game = False
            globalvars.failed = True
            return dead_shape
        
        while type(dead_shape) is Head:
            dead_shape_id = random.choice(self.attached_shapes.keys())
            dead_shape = self.attached_shapes[dead_shape_id]
        
        shape_ids = deepcopy(self.attached_shapes.keys())
        for shape_id in shape_ids:
            finish_him = False
            shape = self.attached_shapes[shape_id]
            if shape_id == dead_shape.id:
                finish_him = True
            else:
                if shape.parent and shape.parent.id == dead_shape.id:
                    finish_him = True
            if finish_him:
                del self.attached_shapes[shape_id]
                #Delete it's references
                del self.shape_graph[shape_id]
                #Update anyone referencing it
                for referencing_shape_id, attached_shapes in deepcopy(self.shape_graph.items()):
                    if shape_id in attached_shapes:
                        self.shape_graph[referencing_shape_id].remove(shape_id)
                
                #Orphane the little guy :(
                shape.parent = None
                        
                #Tell Graphics
                self.graphics.remove_player_shape(shape) 
                self.graphics.add_enemy_shape(shape)
                
                if shape.size == 20:
                    self.total_size -= 1
                elif shape.size == 40:
                    self.total_size -= 2 
                elif shape.size == 70:
                    self.total_size -= 3  
                elif shape.size == 95:
                    self.total_size -= 4  
                elif shape.size == 128:
                    self.total_size -= 5  
                if self.total_size < 1: self.total_size = 1 #sanity
                return shape
        
    def attach_shape(self, shape):
        open_shape_ids = self.__get_open_shapes()
        triangles = self.__find_attached_triangles(open_shape_ids)
        
        #First try to hook up triangle to a random triangle
        if triangles and type(shape) is Tri:
            random_triangle = random.choice(triangles)
            self.__add_shape(shape, random_triangle.id)
            return
        
        #No go? Try to hook up shape to the first triangle of same color        
        for triangle in triangles:
            if shape.color == triangle.color:
                self.__add_shape(shape, triangle.id)
                return 
            
        #Really? Ok, screw it, just pick an open shape at random
        open_shape_id = random.choice(open_shape_ids)
        self.__add_shape(shape, open_shape_id)
        
        if shape.size == 20:
            self.total_size += 1
        elif shape.size == 40:
            self.total_size += 2 
        elif shape.size == 70:
            self.total_size += 3  
        elif shape.size == 95:
            self.total_size += 4  
        elif shape.size == 128:
            self.total_size += 5           
        
        #Tell Graphics
        self.graphics.add_player_shape(shape) 
        self.graphics.remove_enemy_shape(shape)        

        return
        
    def get_render_list(self):
        render_list = self.attached_shapes.values()
        render_list.append(self.head)
        return render_list
    
    def set_invis(self, is_invis):
        if is_invis:
            self.invincible = True
            self.invincible_timer = self.invincible_rate 
            self.head.image = pygame.transform.scale(self.head.getfile("head_trans.png"), (self.head.size, self.head.size))
            self.head.original = self.head.image;
        else:
            self.invincible = False
            self.invincible_timer = 0
            self.head.image = pygame.transform.scale(self.head.getfile("head.png"), (self.head.size, self.head.size))
            self.head.original = self.head.image;
    
