import numpy as np;
from matrix import Matrix;




class UOperator:
    def __init__(self,matrix):
        self.matrix = matrix;
    

    def determinant(matrixA):
        A = matrixA.np_array;
        return np.linalg.det(A);

    def inverse(matrixA):
        A = matrixA.np_array;   
        return np.linalg.inv(A);
    


class BOperator:
    def __init__(self,matrix_a,matrix_b):
        self.matrix_a = matrix_a;
        self.matrix_b = matrix_b;
    
    



    
    

    


def directSum(matrixA, matrixB): #pass in numpy arrays
    #assuming A and B are not yet numpy arrays. Comment out the following two lines after testing. 
    A = matrixA.np_array;
    B = matrixB.np_array;
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


