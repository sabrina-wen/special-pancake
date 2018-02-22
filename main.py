from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 255, 255, 0 ]
matrix = new_matrix()

# lightning bolt
add_edge(matrix, 250, 450, 0, 275, 400, 0) # top downward slash
add_edge(matrix, 220, 400, 0, 275, 400, 0) # straight line
add_edge(matrix, 220, 400, 0, 250, 350, 0) # bottom downward slash

# glasses

#box 1, s = 175
add_edge(matrix, 25, 50, 0, 25, 225, 0) # left vertical line
add_edge(matrix, 200, 50, 0, 200, 225, 0) # right vertical line
add_edge(matrix, 25, 50, 0, 200, 50, 0) # bottom horizontal line
add_edge(matrix, 25, 225, 0, 200, 225, 0) # top horizontal line

#box2
add_edge(matrix, 300, 50, 0, 300, 225, 0) # left vertical line
add_edge(matrix, 475, 50, 0, 475, 225, 0) # right vertical line
add_edge(matrix, 300, 50, 0, 475, 50, 0) # bottom horizontal line
add_edge(matrix, 300, 225, 0, 475, 225, 0) # top horizontal line

#line connecting glasses
add_edge(matrix, 200, 50 + 175 / 2, 0, 300, 50 + 175 / 2, 0)

draw_lines( matrix, screen, color )
display(screen)
