import math


def print_matrix( matrix ):
    row_len = len(matrix[0])
    print row_len
    for r in range(0,len(matrix)):
        print str(float(matrix[r][0]))
    print matrix

def ident( matrix ):
    pass

#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    pass




def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m

print_matrix(new_matrix())
