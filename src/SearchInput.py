import curses
import math
from curses import textpad
from src.Component import Component

class SearchInput(Component):
    def __init__(self, stdscr, height, width, y, x, title):
        self.window = stdscr.subwin(height,width, y,x)
        self.wh, self.ww = self.window.getmaxyx()
        self.query = ""
        self.max_length = width-4
        super().__init__(self.window, title, False, False)

    def draw(self):
        self.window.clear()
        self.draw_border()
        self.window.addstr(1,1, self.query)
        self.window.refresh()

    def listen(self):
        while 1:
            key = self.window.getch()
            print(key)
            if key == 8 and len(self.query) > 0:
                self.query = self.query[:-1]
            elif key == 10 or key == 27:
                curses.curs_set(0)
                self.active = False
                self.draw()
                if key == 27:
                    return False
                else:
                    return self.query
            elif chr(key) in "".join(chr(x) for x in range(32,127)) and len(self.query) < self.max_length:
                self.query += chr(key)
            self.draw()

