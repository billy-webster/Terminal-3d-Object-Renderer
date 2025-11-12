import numpy as np
from .base_shape import Shape

class ConeShape(Shape):
    def __init__(self):
        scale_factor = 3.0 
        points = [
            np.array([[0.0],[1.0*scale_factor],[0.0]]),    
            np.array([[0.0],[0.0],[0.0]]),                   
            np.array([[0.5*scale_factor],[0.0],[0.0]]),
            np.array([[0.475528*scale_factor],[0.0],[0.154508*scale_factor]]),
            np.array([[0.404508*scale_factor],[0.0],[0.293893*scale_factor]]),
            np.array([[0.293893*scale_factor],[0.0],[0.404508*scale_factor]]),
            np.array([[0.154508*scale_factor],[0.0],[0.475528*scale_factor]]),
            np.array([[0.0],[0.0],[0.5*scale_factor]]),
            np.array([[-0.154508*scale_factor],[0.0],[0.475528*scale_factor]]),
            np.array([[-0.293893*scale_factor],[0.0],[0.404508*scale_factor]]),
            np.array([[-0.404508*scale_factor],[0.0],[0.293893*scale_factor]]),
            np.array([[-0.475528*scale_factor],[0.0],[0.154508*scale_factor]]),
            np.array([[-0.5*scale_factor],[0.0],[0.0]]),
            np.array([[-0.475528*scale_factor],[0.0],[-0.154508*scale_factor]]),
            np.array([[-0.404508*scale_factor],[0.0],[-0.293893*scale_factor]]),
            np.array([[-0.293893*scale_factor],[0.0],[-0.404508*scale_factor]]),
            np.array([[-0.154508*scale_factor],[0.0],[-0.475528*scale_factor]]),
            np.array([[0.0],[0.0],[-0.5*scale_factor]]),
            np.array([[0.154508*scale_factor],[0.0],[-0.475528*scale_factor]]),
            np.array([[0.293893*scale_factor],[0.0],[-0.404508*scale_factor]]),
            np.array([[0.404508*scale_factor],[0.0],[-0.293893*scale_factor]]),
            np.array([[0.475528*scale_factor],[0.0],[-0.154508*scale_factor]])
        ]
        faces = [
            [2,3,0], [3,2,1], [3,4,0], [4,3,1], [4,5,0], [5,4,1],
            [5,6,0], [6,5,1], [6,7,0], [7,6,1], [7,8,0], [8,7,1],
            [8,9,0], [9,8,1], [9,10,0], [10,9,1], [10,11,0], [11,10,1],
            [11,12,0], [12,11,1], [12,13,0], [13,12,1], [13,14,0], [14,13,1],
            [14,15,0], [15,14,1], [15,16,0], [16,15,1], [16,17,0], [17,16,1],
            [17,18,0], [18,17,1], [18,19,0], [19,18,1], [19,20,0], [20,19,1],
            [20,21,0], [21,20,1], [21,2,0], [2,21,1]
        ]
        edges_set = set()
        for face in faces:
            n = len(face)
            for i in range(n):
                a = face[i]
                b = face[(i+1)%n]
                edges_set.add(tuple(sorted((a,b))))
        edges = list(edges_set)
        super().__init__(points, edges)