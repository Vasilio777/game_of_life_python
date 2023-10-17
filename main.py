import turtle
from UI import UI
from BoardDrawer import BoardDrawer
from constants import screensize

screen = turtle.Screen()
paused = True
screen.tracer(0)

def toggle_pause(x, y):
    global paused
    paused = not paused

def init_game():
    screen.setup(screensize[0], screensize[1])
    screen.onscreenclick(handle_LMB, 1)
    screen.onscreenclick(toggle_pause, 3)
    
    screen.update()
    render_tick()

def render_tick():
    global paused

    if not paused:
        board.render()
        ui.increase_step()
        screen.update()

    ui.render(paused)

    turtle.ontimer(render_tick, 50)

def handle_LMB(x, y):
    global paused
    if paused:
        board.toggle_cell_state(x, y)

ui = UI()
board = BoardDrawer()
board.fill_ui(ui)

init_game()

screen.listen()
screen.mainloop()
