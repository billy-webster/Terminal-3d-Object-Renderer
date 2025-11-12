import curses
import time
from src.shapes.cube import Cube
from src.shapes.pyramid import Pyramid
from src.shapes.house import HouseShape
from src.shapes.cone import ConeShape
from src.rendering.renderer import Renderer


def show_menu(stdscr):
    curses.curs_set(0)
    stdscr.clear()
    stdscr.addstr(1, 2, "Select a shape:")
    stdscr.addstr(3, 4, "1 - Cube")
    stdscr.addstr(4, 4, "2 - Pyramid")
    stdscr.addstr(5, 4, "3 - House")
    stdscr.addstr(6, 4, "4 - Cone")
    stdscr.addstr(8, 2, "Press number to select")

    stdscr.refresh()

    while True:
        key = stdscr.getch()
        if key == ord('1'):
            return Cube()
        if key == ord('2'):
            return Pyramid()
        if key == ord('3'):
            return HouseShape()
        if key == ord('4'):
            return ConeShape()

def main(stdscr):
    curses.curs_set(0)
    curses.mousemask(curses.ALL_MOUSE_EVENTS)
    stdscr.timeout(10)

    selected_shape = show_menu(stdscr)
    shapes = [selected_shape]

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

