import curses

class Component:
    def __init__(self, window, title, active = False, hover = False):
        self.window = window
        self.title = title
        self.active = active
        self.hover = hover
        self.sh, self.sw = self.window.getmaxyx()

    def color(self):
        if self.active:
            # purple
            return curses.color_pair(2)
        elif self.hover:
            # cyan
            return curses.color_pair(4)
        #black and white
        return curses.color_pair(3)
        
    def draw_border(self):
        color = self.color()

        for i in range(1, self.sw-2):
            self.window.addstr(0, i, "─", color)
            self.window.addstr(self.sh-1, i, "─", color)

        for i in range(1, self.sh-1):
            self.window.addstr(i, 0, "│", color)
            self.window.addstr(i, self.sw-2, "│", color)
        
        self.window.addstr(0,0, "┌", color)
        self.window.addstr(0,self.sw-2, "┐", color)
        self.window.addstr(self.sh-1,0, "└", color)
        self.window.addstr(self.sh-1,self.sw-2, "┘", color)
        self.window.addstr(0,1, self.title, color)

    def focus(self):
        self.active = True
        self.draw()
    
    def unfocus(self):
        self.active = False
        self.draw()
