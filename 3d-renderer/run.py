#!/usr/bin/env python3
from src.main import main
import curses

if __name__ == "__main__":
    curses.wrapper(main)