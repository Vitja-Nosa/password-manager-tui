from src.SearchInput import SearchInput
from src.ResultBox import ResultBox

class DashboardScreen:
    def __init__(self, stdscr):
        self.stdscr = stdscr
        self.components = []

    def restart(self):
        self.searchInput = SearchInput(self.stdscr, 3, 50, 0,0, 'Search')
        self.components.append(ResultBox(self.stdscr, 10, 50, 3,0, 'Result'))
        self.hoverComp = self.components[0]
        self.ResultBox = self.components[0]
        self.draw()
        self.listen()
        
    def draw(self):
        self.stdscr.clear()
        self.searchInput.draw()
        for comp in self.components:
            comp.draw()

    def listen(self):
        while 1:
            key = self.stdscr.getch()
            if key == 10:
                self.hoverComp.activate()
                self.hoverComp.listen()
            elif key == 47:
                self.searchInput.activate()
                
                query = self.searchInput.listen()
                if query:
                    self.ResultBox.query = query
                    self.ResultBox.draw()