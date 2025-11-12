import curses
import time
from shapes.cube import Cube
from shapes.pyramid import Pyramid
from shapes.house import HouseShape
from shapes.cone import ConeShape
from rendering.renderer import Renderer

def main(stdscr):
    curses.curs_set(0)
    curses.mousemask(curses.ALL_MOUSE_EVENTS)
    stdscr.timeout(10)

    # You can easily switch between different shapes here
    shapes = [Cube()] 
    # shapes = [Pyramid()]
    # shapes = [HouseShape()]
    # shapes = [ConeShape()]
    
    renderer = Renderer(stdscr, shapes)

    while True:
        evt = stdscr.getch()
        if evt == ord('q'):
            break
        renderer.handle_mouse(evt)
        renderer.render()
        time.sleep(0.01)

if __name__ == "__main__":
    curses.wrapper(main)