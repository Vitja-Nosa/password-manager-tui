import curses
import math
from string import printable
from time import sleep

class PasswordInput:
    def __init__(self, stdscr, height, width, y, x, title):
        self.stdscr = stdscr
        self.__password = ''
        self.max_length = width-2
        self.window = curses.newwin(height,width, y-math.floor(height/2),x-math.floor(width/2))
        self.title = title

    def draw(self):
        self.window.clear()
        self.window.border(0)
        self.window.addstr(0, 1, self.title)
        hidden_password = ''
        for i in range(0, len(self.__password)):
            hidden_password += 'x'
        self.window.addstr(1,1, hidden_password)
        self.window.refresh()
    
    def drawWrongKey(self):
        curses.curs_set(0)
        msg = " WRONG KEY "
        empty_str = ""
        for i in range(0, self.max_length):
            empty_str += " "
        self.window.addstr(1,1, empty_str)
        self.window.addstr(1,1, msg, curses.color_pair(1))
        self.window.refresh()
        sleep(0.5)

    def listen(self):
        while 1:
            key = self.window.getch()
            if key == 8 and len(self.__password) > 0:
                self.__password = self.__password[:-1]
            elif key == 10 and len(self.__password) > 0:
                break
            elif chr(key) in "".join(chr(x) for x in range(32,127)) and len(self.__password) < self.max_length:
                self.__password += chr(key)
            self.draw()

    def gather(self):
        return self.__password
            