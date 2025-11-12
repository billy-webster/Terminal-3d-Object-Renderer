import numpy as np
from .base_shape import Shape

class Cube(Shape):
    def __init__(self):
        points = [
            np.array([[0],[0],[0]]), np.array([[1],[0],[0]]),
            np.array([[0],[1],[0]]), np.array([[1],[1],[0]]),
            np.array([[0],[0],[1]]), np.array([[1],[0],[1]]),
            np.array([[0],[1],[1]]), np.array([[1],[1],[1]])
        ]
        edges = [
            (0,1),(1,3),(3,2),(2,0),
            (4,5),(5,7),(7,6),(6,4),
            (0,4),(1,5),(2,6),(3,7)
        ]
        super().__init__(points, edges)