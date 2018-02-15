import math


def print_matrix( matrix ):
    col = 0
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            print str(float(matrix[r][c])) + " ",
            col = col+1
            if (col % len(matrix[0]) == 0):
                print ""
    print matrix

def ident( matrix ):
    pass

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

print_matrix(new_matrix())
