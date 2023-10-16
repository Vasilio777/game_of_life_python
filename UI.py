import turtle
from constants import screensize

class UI(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.screensize = screensize
        self.ht()
        self.up()
        self.step_pos = (-screensize[0] / 2.5, screensize[1] / 2.5)
        self.header_pos = (0, screensize[1] / 2.4)
        self.tip_pos = (0, screensize[1] / 2.7)
        self.step = 0
        self.header_text = ''

    def render(self, paused):
        self.clear()
        self.setpos(self.step_pos)
        self.write(f'{self.step}', align="center", font=('Arial', 20, 'normal'))
        if paused:
            self.header_text = 'Affect Destiny!'
            self.setpos(self.header_pos)
            self.write(self.header_text, align="center", font=('Arial', 28, 'normal'))
            self.setpos(self.tip_pos)
            self.write('LMB to propogate, RMB to start', align="center", font=('Arial', 20, 'normal'))
        else:
            self.header_text = 'Enjoy..'
            self.setpos(self.header_pos)
            self.write(self.header_text, align="center", font=('Arial', 28, 'normal'))
            self.setpos(self.tip_pos)
            self.write('RMB to pause', align="center", font=('Arial', 20, 'normal'))

    def increase_step(self):
        self.step += 1
