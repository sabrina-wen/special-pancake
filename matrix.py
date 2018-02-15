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
    matrix[0][0] = 1
    matrix[1][1] = 1
    matrix[2][2] = 1
    matrix[3][3] = 1

#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    pass




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
print "original matrix --> identity matrix: "
print_matrix(m)
r = new_matrix(2,4)
print "rand matrix"
print_matrix(r)
