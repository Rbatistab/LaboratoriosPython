#!/usr/bin/python3

class InvalidDimensionType(Exception):
    pass

class InvalidDimensionSize(Exception):
    pass
    
class Matrix:
    def __init__(self, rows, cols):
        '''
        This class returns a matrix with dimentions rows x cols filled
        with 0s
        '''
        try:
          self.validate_dimensions(rows)
          self.validate_dimensions(cols)
          self.matrix = self.matrix_creation(rows, cols, 0)
        except InvalidDimensionType:
          print("Error: n y m deben ser numeros reales")
        except InvalidDimensionSize:
          print("Error: n y m deben ser enteros positivos")


    def validate_dimensions(self, dimension):
        dimension_class = type(dimension)
        if dimension_class != int and dimension_class != float:
            raise InvalidDimensionType
        else:
            if dimension < 0:
              raise InvalidDimensionSize

    def matrix_creation(self, n, m, desired_object):
        '''
        Creates the matrix
        '''
        matrix = []
        for _ in range(n):
            matrix.append([])

        for a in range(n):
            for _ in range(m):
                matrix[a].append(desired_object)
        return matrix

    def set(self, row, col, value):
        '''
        Sets a single element in the matrix to a desired value
        '''
        self.matrix[row][col] = value

    def get(self, row, col):
        '''
        Gets a single element in the matrix
        '''
        return self.matrix[row][col]

    def get_matrix_dimensions(self):
        '''
        Returns size of the matrix
        '''
        dimensions = {
          'rows' : len(self.matrix),
          'cols' : len(self.matrix[0])

        }
        return dimensions


    def __str__(self):
        '''
        Returns a String representation of the matrix
        '''
        matrix_string = ""
        for rows in self.matrix:
            for element in rows:
                matrix_string += str(element) + " "

            matrix_string += "\n"
        return matrix_string

    def __add__(self, second_matrix):
      '''
      Allows Matrix addition
      '''
      dimensions = self.get_matrix_dimensions()
      added_matrix = Matrix( dimensions['rows'],  dimensions['cols'])
      for row_ind, row in enumerate(self.matrix):
          for col_ind, element in enumerate(row):
              added_element = element + second_matrix.get(row_ind, col_ind)
              added_matrix.set(row_ind, col_ind, added_element)
      return added_matrix
    
    
    def __sub__(self, second_matrix):
      '''
      Allows Matrix substraction
      '''
      dimensions = self.get_matrix_dimensions()
      added_matrix = Matrix( dimensions['rows'],  dimensions['cols'])
      for row_ind, row in enumerate(self.matrix):
          for col_ind, element in enumerate(row):
              added_element = element - second_matrix.get(row_ind, col_ind)
              added_matrix.set(row_ind, col_ind, added_element)
      return added_matrix


    def __iter__(self):
        '''
        Matrix iterator
        '''
        return MatrixIterator(self)


class MatrixIterator:
    '''
    Iterator class for GeneralMatrix
    '''
    def __init__(self, general_matrix):
        self._matrix = general_matrix.matrix
        self._index = 0
        self.row_size = len(self._matrix)

    def __next__(self):
        '''
        Gets next row in the matrix
        '''
        if self._index < self.row_size:
            return_row = self._matrix[self._index]
            self._index += 1
            return return_row
        raise StopIteration



def main():
    # Validations
    print("Matriz invalida por tipo: Matrix(\'1\',3):\n")
    invalid_type_matrix = Matrix('1',3)
    
    print("\nMatriz invalida por rango:\nMatrix(1, -3):\n")
    invalid_size_matrix = Matrix(1,-3)
    
    # Methods
    print("\nMatriz valida: Matrix(4, 5)\n")
    valid_matrix = Matrix(4,5)
    print(valid_matrix)

    print("\nMetodo get(): get(2, 2)\n")
    get_test_1 = valid_matrix.get(2,2)
    print(get_test_1)

    print("\nMetodo set(): set(2, 2, 4)\n")
    valid_matrix.set(2,2, 4)
    print(valid_matrix)

    # Adding and substracting:
    print("\n\nMetodos de adicion y substraccion: \n")

    another_valid_matrix = Matrix(4,5)
    another_valid_matrix.set(2,4, 5)
    print('Otra matriz:')
    print(another_valid_matrix)

    print('\nSumando ambas matrices:')
    added_matrix_test = valid_matrix + another_valid_matrix
    print(added_matrix_test)

    print('\nSumando ambas matrices:')
    substracted_matrix_test = valid_matrix - another_valid_matrix
    print(substracted_matrix_test)


if __name__ == '__main__':
    main()