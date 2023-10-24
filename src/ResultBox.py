import curses
from src.Component import Component

class ResultBox(Component):
    def __init__(self, stdscr, height, width, y, x, title):
        self.window = stdscr.subwin(height,width, y,x)
        self.query = ""
        self.result_list = ['apex', 'buas_email', 'primary email', 'other stuff']
        self.active_index = 0
        super().__init__(self.window, title, False, True)


    def draw(self):
        self.window.clear()
        self.draw_border()
        self.drawList()
        self.window.refresh()

    def drawList(self):
        rl = self.result_list
        for i in range(0, len(rl)):
            if i == self.active_index:
                self.window.addstr(i+1, 1, rl[i], self.color())
            else:
                self.window.addstr(i+1, 1, rl[i])
