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
        self.figures = []

    def render(self, paused):
        self.clear()
        self.draw_step()

        if paused:
            self.draw_header('Affect Destiny!')
            self.draw_tip('LMB to propogate, RMB to start')
        else:
            self.draw_header('Enjoy.. ')
            self.draw_tip('RMB to pause')

    def draw_step(self):
        self.setpos(self.step_pos)
        self.write(f'step: {self.step}', align="center", font=('Arial', 20, 'normal'))

    def draw_header(self, text):
        self.setpos(self.header_pos)
        self.write(text, align="center", font=('Arial', 28, 'normal'))

    def draw_tip(self, text):
        self.setpos(self.tip_pos)
        self.write(text, align="center", font=('Arial', 20, 'normal'))


    def init_figures(self, figures):
        for figure_name in figures:
            self.figures.append({figure_name: 0})

    def still_lifes_counter(self):
        pass

    def increase_step(self):
        self.step += 1
