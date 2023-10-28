from src.SearchInput import SearchInput
from src.ResultBox import ResultBox

class DashboardScreen:
    def __init__(self, stdscr):
        self.stdscr = stdscr

    def restart(self):
        self.searchInput = SearchInput(self.stdscr, 3, 50, 0,0, 'Search')
        self.ResultBox = ResultBox(self.stdscr, 10, 50, 3,0, 'Result')
        self.hoverComp = self.ResultBox
        self.draw()
        self.listen()
        
    def draw(self):
        self.stdscr.clear()
        self.searchInput.draw()
        self.ResultBox.draw()

    def listen(self):
        while 1:
            key = self.stdscr.getch()
            if key == 10:
                self.hoverComp.focus()
                self.hoverComp.listen()
            elif key == 47:
                self.searchInput.focus()
                query = self.searchInput.listen()
                if query:
                    self.ResultBox.query = query
                    self.ResultBox.draw()