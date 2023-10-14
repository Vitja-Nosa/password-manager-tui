import curses

class Component:
    def draw_border(self):
        sh, sw = self.window.getmaxyx()

        color = curses.color_pair(3)
        if self.active:
            color = curses.color_pair(2)
    

        for i in range(1, sw-2):
            self.window.addstr(0, i, "─", color)
            self.window.addstr(sh-1, i, "─", color)

        for i in range(1, sh-1):
            self.window.addstr(i, 0, "│", color)
            self.window.addstr(i, sw-2, "│", color)
        
        self.window.addstr(0,0, "┌", color)
        self.window.addstr(0,sw-2, "┐", color)
        self.window.addstr(sh-1,0, "└", color)
        self.window.addstr(sh-1,sw-2, "┘", color)
        self.window.addstr(0,1, self.title, color)