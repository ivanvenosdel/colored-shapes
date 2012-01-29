import random
from copy import deepcopy

import pygame

from actors import Head, Tri
from vector2 import Vector2

import globalvars

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
        self.invincible_rate = 800
        self.invincible_timer = self.invincible_rate
        
    def update(self, delta):
        if self.invincible:
            self.invincible_timer -= delta
            if self.invincible_timer <= 0: 
                self.invincible = False
           
    def __get_open_shapes(self):
        open_shape_ids = []
        for shape_id, attached in self.shape_graph.items():
            if len(attached) < self.attached_shapes[shape_id].sides:
                open_shape_ids.append(shape_id)
        return open_shape_ids
        
    def __add_shape(self, shape, leaf_id):
        leaf_shape = self.attached_shapes[leaf_id]
        
        #Create a vector between the two shapes to figure out how to move it to it but without collision
        shape_vector = Vector2.from_points((shape.rect.x, shape.rect.y), (leaf_shape.rect.x, leaf_shape.rect.y))
        shape.rect.move(shape_vector.x - (shape.rect.width + leaf_shape.rect.width), shape_vector.y - (shape.rect.height + leaf_shape.rect.height))
        
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
        if type(dead_shape) is Head or len(self.attached_shapes) <= 1:
            raise globalvars.GameOver
        
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
                #Update anyone referencing it
                for attached_shapes in deepcopy(self.shape_graph[shape_id]):
                    if dead_shape_id in attached_shapes:
                        self.shape_graph[shape_id].remove(dead_shape_id)
                #Delete it's references
                del self.shape_graph[shape_id]
                
                #Tell Graphics
                self.graphics.remove_player_shape(shape) 
                #self.graphics.add_enemy_shape(shape)
                
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
    
