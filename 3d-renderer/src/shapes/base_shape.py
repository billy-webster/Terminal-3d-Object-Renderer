import numpy as np

class Shape:
    def __init__(self, points, edges):
        self.points = points
        self.edges = edges
        self.center = self.calculate_center()

    def calculate_center(self):
        pts = np.hstack(self.points)
        center = np.mean(pts, axis=1, keepdims=True)
        return center

    def rotate(self, rotation_matrix):
        self.points = [rotation_matrix @ (p - self.center) + self.center for p in self.points]

    def get_projected_points(self, d=5):
        return np.hstack([self._project_point(p, d) for p in self.points])

    @staticmethod
    def _project_point(point, d):
        z = point[2][0] + d
        projected = np.array([
            [point[0][0] / z],
            [point[1][0] / z],
            [0]
        ]) * d
        return projected