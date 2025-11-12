import numpy as np

class Arcball:
    @staticmethod
    def normalize(v):
        mag = np.linalg.norm(v)
        return v / mag if mag != 0 else v

    @staticmethod
    def vector(x, y, w, h):
        nx = (2*x - w) / w
        ny = (h - 2*y) / h
        v = np.array([nx, ny, 0])
        d = nx*nx + ny*ny
        if d <= 1:
            v[2] = np.sqrt(1 - d)
        return Arcball.normalize(v)

    @staticmethod
    def rotation_matrix(axis, angle):
        axis = Arcball.normalize(axis)
        x, y, z = axis
        c = np.cos(angle)
        s = np.sin(angle)
        C = 1 - c
        return np.array([
            [c + x*x*C,   x*y*C - z*s, x*z*C + y*s],
            [y*x*C + z*s, c + y*y*C,   y*z*C - x*s],
            [z*x*C - y*s, z*y*C + x*s, c + z*z*C]
        ])