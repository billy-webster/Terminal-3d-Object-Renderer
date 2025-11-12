import numpy as np
from .base_shape import Shape

class Pyramid(Shape):
    def __init__(self):
        points = [
            np.array([[0],[0],[0]]), np.array([[1],[0],[0]]),
            np.array([[1],[1],[0]]), np.array([[0],[1],[0]]),
            np.array([[0.5],[0.5],[1]])
        ]
        edges = [
            (0,1),(1,2),(2,3),(3,0),
            (0,4),(1,4),(2,4),(3,4)
        ]
        super().__init__(points, edges)