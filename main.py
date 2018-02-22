from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 255, 255, 0 ]
matrix = new_matrix()

m = new_matrix()
print "original matrix: "
print_matrix(m)
ident(m)
m[0][3] = 2
m[1][3] = 3
m[2][3] = 4
print "original matrix --> identity matrix: "
print_matrix(m)
r = new_matrix(4,8)
incr = 0
for i in range(len(r)):
    for j in range(len(r[0])):
        if (i != len(r) - 1):
            r[i][j] = incr
            incr = incr + 1
        else:
            r[i][j] = 1
print "m2 matrix:"
print_matrix(r)

print "multiply m1 x m2"
print_matrix(matrix_mult(m,r))

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
