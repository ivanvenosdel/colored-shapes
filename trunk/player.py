import random
import pygame

from actors import Head, Tri

class Player:
    
    def __init__(self):
        self.head = Head(64, 0)
        #Graph of each shape id and the ids of the shapes connected to it
        self.shape_graph = {self.head.id: []}
        self.attached_shapes = {self.head.id: self.head}
        
    def __get_open_shapes(self):
        open_shape_ids = []
        for shape_id, attached in self.shape_graph.items():
            if len(attached) < self.attached_shapes[shape_id].sides:
                open_shape_ids.append(shape_id)
        return open_shape_ids
        
    def __add_shape(self, shape, leaf_id):        
        self.attached_shapes[shape.id] = shape
        self.shape_graph[shape.id] = [leaf_id]
        self.shape_graph[leaf_id].append(shape.id)
        
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
        open_shape = random.choice(open_shape_ids)
        self.__add_shape(shape, open_shape.id)
        return
        
    def get_render_list(self):
        render_list = self.attached_shapes.values()
        render_list.append(self.head)
        return render_list
    
