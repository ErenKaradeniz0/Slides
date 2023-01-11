import math
from DrawingPanel import *


def math_calc():
    x = 9.5
    print(math.ceil(x))
    print(math.floor(x))

    print(math.log(4, 2))

    print()
    print(math.sin(math.radians(90)))
    print(math.cos(math.radians(0)))
    print(math.tan(math.radians(45)))

    print(math.degrees(3))
    print(math.radians(90))

    print(min(10, 9))
    print(max(9, 10))
    print(round(9.5))

    print()
    # 1.23 -5 6 22 5
    print(abs(-1.23))
    print(math.sqrt(121.0) - math.sqrt(256.0))
    print(round(math.pi) + round(math.e))
    print(math.ceil(6.022) + math.floor(15.9994))
    print(abs(min(-3, -5)))


def f_to_c(degrees_f):
    degrees_c = 5.0 / 9.0 * (degrees_f-32)
    return degrees_c


def hypotenuse(a, b):
    return math.sqrt(a * a + b * b)


print(f_to_c(100))
print(hypotenuse(3, 4))


def displacement(v0, t, a):
    return v0 * t + 0.5 * a * (t ** 2)


print(displacement(3, 4, 5))


def ball():
    panel = DrawingPanel(600, 600)

    ballx = 100
    bally = 0
    v01 = 25
    ball2x = 300
    ball2y = 100
    v02 = 15

    for time in range(60):
        displacement1 = displacement(v01, time, 9.81)
        panel.fill_oval(ballx, bally + displacement1, 100,100)

        displacement2 = displacement(v02, time, 9.81)
        panel.fill_oval(ball2x, ball2y + displacement2, 100, 100)
        panel.sleep(75)
        panel.fill_rect(0, 0, 600, 600, "white")


ball()
