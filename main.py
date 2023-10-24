import curses
from curses import wrapper
from curses import textpad
import time
import math
from src.PasswordInput import PasswordInput
from src.LoginScreen import LoginScreen
from src.DashboardScreen import DashboardScreen

def main(stdscr):
    curses.curs_set(1)
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_RED)
    curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    sh, sw = stdscr.getmaxyx()
    loginScreen = LoginScreen(stdscr)
    loginScreen.restart()
    curses.curs_set(0)
    dashboardScreen = DashboardScreen(stdscr)
    dashboardScreen.restart()

    

    

    time.sleep(5)
    



wrapper(main)
