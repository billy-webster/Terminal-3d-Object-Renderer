import numpy as np
from .base_shape import Shape

class HouseShape(Shape):
    def __init__(self):
        points = [
            np.array([[0],[0],[0]]), 
            np.array([[1],[0],[0]]), 
            np.array([[1],[1],[0]]), 
            np.array([[0],[1],[0]]),
            np.array([[0],[0],[1]]), 
            np.array([[1],[0],[1]]), 
            np.array([[1],[1],[1]]), 
            np.array([[0],[1],[1]]),  
            np.array([[0.5],[0.5],[1.5]])  
        ]
        edges = [
            (0,1),(1,2),(2,3),(3,0),
            (4,5),(5,6),(6,7),(7,4),  
            (0,4),(1,5),(2,6),(3,7),  
            (4,8),(5,8),(6,8),(7,8)
        ]
        super().__init__(points, edges)