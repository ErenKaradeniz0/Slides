from DrawingPanel import *


def worm():
    panel = DrawingPanel(260, 200, background="light gray")
    for i in range(1, 11):
        panel.fill_oval(100+20*i, 5+20*i, 50, 50, "red")


def circles():
    panel = DrawingPanel(260, 200, background="light gray")
    for i in range(1, 11):
        panel.draw_oval(100, 100, 22*i, 22*i, "magenta")


def draw_car(p, x, y, size):
    panel = DrawingPanel(260, 200, background="light gray")
    panel.fill_rect(x, y, size, size/2, "green")
    panel.fill_oval(x+size/10, y+size/10*4, size/5, size/5, "black")
    panel.fill_oval(x+size/10*7, y+size/10*4, size/5, size/5, "black")
    panel.fill_rect(x+size/10*7, y+size/10, size/10*3, size/5, "dark")


def my_function_top():
    panel = DrawingPanel(260, 200, background="light gray")
    for i in range(0, 20):
        panel.draw_rectangle(20, 20+10*i, 200-10*i, 10)


def my_function_left():
    panel = DrawingPanel(260, 200, background="light gray")
    for i in range(0, 10):
        panel.draw_rectangle(20+10*i, 20+10 * i, 100-10*i, 10)


def my_function_bottom():
    panel = DrawingPanel(260, 200, background="light gray")
    for i in range(0, 10):
        panel.draw_rectangle(110-10*i, 20+10 * i, 10+10*i, 10)


def cars():
    panel = DrawingPanel(260, 200, background="light gray")
    for i in range(0, 260, 50):
        draw_car(panel, 10+i, 130, 80)
        panel.sleep(500)


def animate(NUM_CIRCLES):
    panel = DrawingPanel(250, 250)
    for i in range(0, NUM_CIRCLES):
        panel.draw_oval(15*i, 15*i, 40, 40)
        panel.sleep(250)
        panel.draw_oval(250-15*i, 15*i, 40, 40)
        panel.sleep(250)
        panel.draw_oval(15*i, 250 - 15*i, 40, 40)
        panel.sleep(250)
        panel.draw_oval(250-15*i, 250 - 15*i, 40, 40)
        panel.sleep(100)


# animate(14)
# worm()
# circles()
cars()
