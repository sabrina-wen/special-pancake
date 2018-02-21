import math


def print_matrix( matrix ):
    col = 0
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            print str(float(matrix[r][c])) + " ",
            col = col+1
            if (col % len(matrix[0]) == 0):
                print ""

#identity matrix
def ident( matrix ):
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if (r != c):
                matrix[r][c] = 0
            else:
                matrix[r][c] = 1

#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    m2_copy = new_matrix(len(m2), len(m2[0]))
    # make a copy of m2
    for i in range(len(m2)):
        for j in range(len(m2[0])):
            m2_copy[i][j] = m2[i][j]
    # init variables
    curr_col = 0
    curr_row = 0
    # convert each col in m2 into a 1d array, dot product w/ each row in m1
    while (curr_col < len(m2[0])) and curr_row < len(m2):
        #print "current coordinate is: (" + str(curr_row) + ", " + str(curr_col) + ")"
        sum = 0
        temp = []
        for r in range(len(m2_copy)):
            for c in range(len(m2_copy[0])):
                if (c == curr_col):
                    temp.append(m2_copy[r][c])
        for i in range(len(temp)):
            sum += m1[curr_row][i] * temp[i]
        m2[curr_row][curr_col] = sum
        #print "curr_col: " + str(curr_col)
        #print curr_col % len(m2[0])
        if (curr_col != len(m2[0]) - 1):
            #print "lol"
            curr_col = curr_col + 1
        else:
            curr_col = 0
            curr_row = curr_row + 1

    return m2

def new_matrix(rows = 4, cols = 4):
    m = []
    for r in range( rows ):
        m.append( [] )
        for c in range( cols ):
            m[r].append( 0 )
    return m


m = new_matrix()
print "original matrix: "
print_matrix(m)
ident(m)
m[0][3] = 2
m[1][3] = 3
m[2][3] = 4
print "original matrix --> identity matrix: "
print_matrix(m)
r = new_matrix(4,5)
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
