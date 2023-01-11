from DrawingPanel import *


def nested_loops():
    for i in range(1, 10):
        for j in range(1, 10):
            print(j*i, end="\t")
        print()


panel = DrawingPanel(500, 500)


def draw_circles(x, y, size, r):

    for i in range(1, r+1):
        for j in range(1, r+1):
            panel.fill_oval(x+j*size, y, size, size, "red")
        y += size


draw_circles(100, 100, 20, 5)
draw_circles(300, 300, 40, 2)
