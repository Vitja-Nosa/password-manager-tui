import curses
from curses import wrapper
from curses import textpad
import time
import math
from src.PasswordInput import PasswordInput
from src.LoginScreen import LoginScreen
from src.DashboardScreen import DashboardScreen

def main(stdscr):
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_RED)
    sh, sw = stdscr.getmaxyx()
    loginScreen = LoginScreen(stdscr)
    loginScreen.restart()
    dashboardScreen = DashboardScreen(stdscr)
    dashboardScreen.restart()

    

    

    time.sleep(5)
    



wrapper(main)
