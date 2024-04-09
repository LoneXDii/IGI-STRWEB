import numpy as np


class Matrix:
    def __init__(self, matrix: np.array):
        self.__matrix = matrix

    @property
    def data(self):
        return self.__matrix

    @data.setter
    def data(self, value):
        self.__matrix = value

    def rebuild_matrix(self):
        shape = self.__matrix.shape
        rows = shape[0]
        columns = shape[1]
        for i in range(rows):
            max_in_row = self.__matrix[i][0]
            max_pos = 0
            for j in range(columns):
                if max_in_row < self.__matrix[i][j]:
                    max_in_row = self.__matrix[i][j]
                    max_pos = j
            self.__matrix[i][i], self.__matrix[i][max_pos] = self.__matrix[i][max_pos], self.__matrix[i][i]

    def get_main_diagonal(self):
        diagonal = np.array([])
        shape = self.__matrix.shape
        rows = shape[0]
        columns = shape[1]
        for i in range(rows):
            for j in range(columns):
                if i == j:
                    diagonal = np.append(diagonal, self.__matrix[i][j])
                    break
        return diagonal

    def get_median_numpy(self):
        diagonal = self.get_main_diagonal()
        return np.median(diagonal)

    def get_median(self):
        diagonal = self.get_main_diagonal()
        diagonal.sort()
        size = len(diagonal)
        if size % 2 == 0:
            return (diagonal[int(size/2)] + diagonal[int(size/2 - 1)]) / 2
        else:
            return diagonal[int(size/2)]

    def __str__(self):
        return str(self.__matrix)
