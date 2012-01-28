import random

from actors.head import Head

class Player():
    
    def __init__(self):
        self.head = Head()
        #Graph of each shape id and the ids of the shapes connected to it
        self.shape_graph = {self.head.id: []}
        self.leaf_ids = []
        self.attached_shapes = {}
        
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
        #(For now) Pick a random leaf
        leaf_id = random.choice(self.leaf_ids)
        
        #Add shape to graph and attach
        self.attached_shapes[shape.id] = shape
        self.shape_graph[shape.id] = []
        self.shape_graph[leaf_id].append(shape.id)
        
    def get_render_list(self):
        render_list = self.attached_shapes.values()
        render_list.append(self.head)
        return render_list
        