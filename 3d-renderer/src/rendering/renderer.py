import numpy as np
import curses
import time

class Renderer:
    def __init__(self, stdscr, shapes):
        self.stdscr = stdscr
        self.shapes = shapes
        self.current_rot = np.eye(3)
        self.dragging = False
        self.last_v = None
        self.scale = 10  

    def draw_line(self, grid, x0, y0, x1, y1):
        dx = abs(x1 - x0)
        dy = abs(y1 - y0)
        sx = 1 if x0 < x1 else -1
        sy = 1 if y0 < y1 else -1
        err = dx - dy
        while True:
            if 0 <= x0 < len(grid[0]) and 0 <= y0 < len(grid):
                grid[y0][x0] = "."
            if x0 == x1 and y0 == y1:
                break
            e2 = 2 * err
            if e2 > -dy:
                err -= dy
                x0 += sx
            if e2 < dx:
                err += dx
                y0 += sy

    def render(self):
        rows, cols = self.stdscr.getmaxyx()
        grid = [[" " for _ in range(cols)] for _ in range(rows)]

        for shape in self.shapes:
            projected = shape.get_projected_points()
            scale = self.scale
            xc = (projected[0] * scale).astype(int)
            yc = (projected[1] * scale).astype(int)
            off_x = cols // 2
            off_y = rows // 2 - rows // 4
            for a, b in shape.edges:
                x0, y0 = xc[a] + off_x, yc[a] + off_y
                x1, y1 = xc[b] + off_x, yc[b] + off_y
                self.draw_line(grid, x0, y0, x1, y1)

        self.stdscr.clear()
        for y in range(min(rows, len(grid))):
            try:
                self.stdscr.addstr(y, 0, "".join(grid[y])[:cols-1])
            except curses.error:
                pass
        self.stdscr.refresh()

    def handle_mouse(self, evt):
        rows, cols = self.stdscr.getmaxyx()
        if evt == curses.KEY_MOUSE:
            _, mx, my, _, state = curses.getmouse()
           
            if state & curses.BUTTON1_PRESSED:
                self.dragging = True
                self.last_v = Arcball.vector(mx, my, cols, rows)
            if state & curses.BUTTON1_RELEASED:
                self.dragging = False
            if self.dragging:
                v = Arcball.vector(mx, my, cols, rows)
                if self.last_v is not None:
                    axis = np.cross(self.last_v, v)
                    angle = np.arccos(np.clip(np.dot(self.last_v, v), -1, 1))
                    if np.linalg.norm(axis) > 1e-6:
                        R = Arcball.rotation_matrix(axis, angle)
                        for shape in self.shapes:
                            shape.rotate(R)
                self.last_v = v
            # Zooming
            if state & curses.BUTTON4_PRESSED: 
                self.scale += 1
            if state & curses.BUTTON5_PRESSED:  
                self.scale = max(1, self.scale - 1)