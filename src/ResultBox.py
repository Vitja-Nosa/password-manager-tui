from src.Component import Component

class ResultBox(Component):
    def __init__(self, stdscr, height, width, y, x, title):
        self.stdscr = stdscr
        self.window = stdscr.subwin(height,width, y,x)
        self.title = title
        self.active = False

    def draw(self):
        self.window.clear()
        self.draw_border()
        self.window.refresh()