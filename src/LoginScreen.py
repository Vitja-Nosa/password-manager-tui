import curses
import math
from curses import textpad
from src.PasswordInput import PasswordInput
from hashlib import sha256 as hashValue
from src.SecretManager import put_in_key

global master_key

class LoginScreen:
    def __init__(self, stdscr):
        self.stdscr = stdscr
        self.margin = 2
        self.sh, self.sw = stdscr.getmaxyx()
        self.rect_left_corner_y, self.rect_left_corner_x = 0, self.margin
        self.rect_right_corner_y, self.rect_right_corner_x = self.sh-2, self.sw-1-self.margin

    def draw(self):
            self.stdscr.clear()
            textpad.rectangle(self.stdscr, self.rect_left_corner_y, self.rect_left_corner_x, self.rect_right_corner_y, self.rect_right_corner_x)
            self.stdscr.refresh()
            self.passwordInput.draw()

    def restart(self):
        curses.curs_set(1)
        self.passwordInput = PasswordInput(self.stdscr, 3,40, math.floor(self.sh/2), math.floor(self.sw/2), "Enter master key")
        self.draw()
        self.passwordInput.listen() # waits until enter is pressed
        self.attempt(self.passwordInput.gather())

    
    def attempt(self, password):
        if self.compareKey(password):
            print('hello')
            self.master_key = password
            self.destroy()
        else:
            self.passwordInput.drawWrongKey()
            self.restart()
    
    def destroy(self):
        self.stdscr.clear()
        self.stdscr.refresh()

    def compareKey(self, key):
        key_hashed = hashValue(str.encode(key)).hexdigest()
        f = open('masterkey', 'r')
        l = f.readline()
        f.close() 
        return l == key_hashed
        # return True