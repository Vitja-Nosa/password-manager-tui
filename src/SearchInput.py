import curses
import math

class SearchInput:
    def __init__(self, stdscr, height, width, y, x, title):
        self.window = stdscr.subwin(height,width, y,x)
        self.query = ""
        self.max_length = width-2
        self.title = title

    def draw(self):
        self.window.clear()
        self.window.border(0) # replace this later with rectangle for color i think
        self.window.addstr(0,1, self.title)
        self.window.addstr(1,1, self.query)
        self.window.refresh()

    def listen(self):
        while 1:
            key = self.window.getch()
            print(key)
            if key == 8 and len(self.query) > 0:
                self.query = self.query[:-1]
            elif key == 10 or key == 27:
                break
            elif chr(key) in "".join(chr(x) for x in range(32,127)) and len(self.query) < self.max_length:
                self.query += chr(key)
            self.draw()

