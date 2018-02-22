from display import *
from matrix import *


def draw_lines( matrix, screen, color ):
    for c in range(0, len(matrix[0]), 2):
        draw_line(matrix[0][c],matrix[1][c], matrix[0][c+1], matrix[1][c+1], screen, color)

def add_edge( matrix, x0, y0, z0, x1, y1, z1 ):
    add_point(matrix, x0, y0, z0)
    add_point(matrix,x1,y1,z1)

def add_point( matrix, x, y, z=0 ):
    matrix[0].append(x)
    matrix[1].append(y)
    matrix[2].append(z)
    matrix[3].append(1)

def draw_line( x0, y0, x1, y1, screen, color ):
    if (x0 > x1):
        temp = x1
        x1 = x0
        x0 = temp
        temp = y1
        y1 = y0
        y0 = temp
    x, y = x0, y0
    a = y1 - y0 # a = change in y
    b = -(x1 - x0)# change in x

    # check if vertical line
    if (b == 0):
        if (y < y1):
            while(y <= y1):
                plot(screen, color, x, y)
                y = y + 1
        if (y > y1):
            while(y1 <= y):
                plot(screen, color, x, y)
                y = y - 1
        return

    m = float(a) / float(-b) # slope

    # octant 1
    if (m >= 0 and m <= 1):
        d = (2 * a) + b
        while(x <= x1):
            plot(screen, color, x, y)
            if (d > 0):
                y = y + 1
                d += (2 * b)
            x = x + 1
            d += (2 * a)
        plot(screen, color, x, y)
    # octant 2
    if (m > 1):
        d = a + (2 * b)
        while(y <= y1):
            plot(screen, color, x, y)
            if (d < 0):
                x = x + 1
                d += (2 * a)
            y = y + 1
            d += (2 * b)
        plot(screen, color, x, y)
    # octant 8
    if (m < -1):
        d = a - (2 * b)
        while(y > y1):
            plot(screen, color, x, y)
            if (d > 0):
                x = x + 1
                d += (2 * a)
            y = y - 1
            d -= (2 * b)
        plot(screen, color, x, y)
    # octant 7
    if (m < 0 and m >= -1):
        d = (2 * a) - b
        while(x <= x1):
            plot(screen, color, x, y)
            if (d < 0):
                y = y - 1
                d -= (2 * b)
            x = x + 1
            d += (2 * a)
        plot(screen, color, x, y)
