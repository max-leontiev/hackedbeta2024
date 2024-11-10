import numpy as np
from flask import render_template
from matrix import Matrix
from abc import abstractmethod, ABC

class UOperator:
    def __init__(self, matrix: Matrix):
        self.matrix = matrix

    def determinant(matrixA: Matrix):
        A = matrixA.np_array
        return np.linalg.det(A)

    def inverse(matrixA: Matrix):
        A = matrixA.np_array
        return np.linalg.inv(A)


class BOperator:
    def __init__(self, matrix_a, matrix_b):
        self.matrix_a = matrix_a
        self.matrix_b = matrix_b

    def directSum(self, matrix_a, matrix_b):  # pass in numpy arrays
        # assuming A and B are not yet numpy arrays. Comment out the following two lines after testing.
        A = matrix_a.np_array()
        B = matrix_b.np_array()
        # returns the dimensions of A and B where shape is a tuple with index 0 having x rows and index 1 having y columns
        dimA = A.shape
        dimB = B.shape
        result = np.zeros(
            (dimA[0] + dimB[0], dimA[1] + dimB[1])
        )  # creates a new array with dimensions rowsA+rowsB by columns+columnsB and populates it with zeroes
        result[: dimA[0], : dimA[1]] = (
            A  # places MatrixA in the top-left corner of result.
        )
        result[dimA[0] :, dimA[1] :] = (
            B  # places MatrixB in the bottom-right corner of result.
        )
        return result

    def multiplication(self, matrix_a, matrix_b):
        A = matrix_a.np_array()
        B = matrix_b.np_array()
        result = np.matmul(A, B)
        return result

    def add(self, matrix_a, matrix_b):
        A = matrix_a.np_array()
        B = matrix_b.np_array()
        result = A + B
        return result


def determinant(matrix):
    A = matrix.np_array
    return 0


def inverse(matrix):
    return 0

class BinaryOperator(ABC):
    def __init__(self, ind):
        self.ind = ind
        super().__init__()
    
    @abstractmethod
    def name(): pass

    @abstractmethod
    def symbols(): return 
    
    @abstractmethod
    def compute(matrix_A, matrix_B): pass

    def as_form(self):
        return render_template("binary_operation.html", operation=self)
    
    def as_static_markup(self): 
        return render_template("binary_operation.html", operation=self, disabled=True)


class Multiplication(BinaryOperator):
    def __init__(self, ind: int):
        super().__init__(ind)

    @staticmethod
    def name():
        return "multiplication"
    
    @staticmethod
    def symbols():
        return ["×", "*"] # symbols, in order of preference (first one is used for display)
    
    @staticmethod
    def compute(matrix_A, matrix_B):
        A = matrix_A.np_array()
        B = matrix_B.np_array()
        result = np.matmul(A, B)
        return result

BINARY_OPERATOR_SYMBOLS_TO_CLASSES = {}
BINARY_OPERATOR_NAMES_TO_CLASSES = {}
for bin_op in BinaryOperator.__subclasses__():
    for symbol in bin_op.symbols():
        BINARY_OPERATOR_SYMBOLS_TO_CLASSES[symbol] = bin_op
    BINARY_OPERATOR_NAMES_TO_CLASSES[bin_op.name()] = bin_op

BinaryOperator.from_symbol = lambda symbol : BINARY_OPERATOR_SYMBOLS_TO_CLASSES[symbol] if symbol in BINARY_OPERATOR_SYMBOLS_TO_CLASSES else None
BinaryOperator.from_name = lambda symbol : BINARY_OPERATOR_NAMES_TO_CLASSES[symbol] if symbol in BINARY_OPERATOR_NAMES_TO_CLASSES else None
