import numpy as np;
from matrix import Matrix;

class UOperator:
    def __init__(self,matrix):
        self.matrix = matrix;

class BOperator:
    def __init__(self,matrix_a,matrix_b):
        self.matrix_a = matrix_a;
        self.matrix_b = matrix_b;

class directSum:
    def __init__(self,matrix_a,matrix_b):
        super().__init__(matrix_a,matrix_b);



    
    

    


def directSum(A, B): #pass in numpy arrays
    #assuming A and B are not yet numpy arrays. Comment out the following two lines after testing.
    A = np.array(A)
    B = np.array(B)
    # returns the dimensions of A and B where shape is a tuple with index 0 having x rows and index 1 having y columns
    dimA = A.shape 
    dimB = B.shape
    result = np.zeros((dimA[0] + dimB[0], dimA[1] + dimB[1])) # creates a new array with dimensions rowsA+rowsB by columns+columnsB and populates it with zeroes
    result[:dimA[0], :dimA[1]] = A #places MatrixA in the top-left corner of result.
    result[dimA[0]:, dimA[1]:] = B # places MatrixB in the bottom-right corner of result.
    return result;




def determinant(matrix):
    A = matrix.np_array;
    return 0;
def inverse(matrix):  
    return 0;


