from src.SearchInput import SearchInput
from src.ResultBox import ResultBox

class DashboardScreen:
    def __init__(self, stdscr):
        self.stdscr = stdscr

    def restart(self):
        self.searchInput = SearchInput(self.stdscr, 3, 50, 0,0, 'Search')
        self.ResultBox = ResultBox(self.stdscr, 100, 50, 0,0, 'Result')
        self.draw()
        self.listen()
        
    def draw(self):
        self.stdscr.clear()
        self.searchInput.draw()

    def listen(self):
        while 1:
            key = self.stdscr.getch()
            if key == 47:
                self.searchInput.active = True
                self.searchInput.draw()
                self.searchInput.listen()