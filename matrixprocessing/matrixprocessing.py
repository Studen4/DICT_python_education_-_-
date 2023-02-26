"""Some useful project to calculate matrix"""


class Matrix:
    """Class to work with matrix and calculate them"""

    def __init__(self, rows, cols, matrix=None):
        """Function to initialisation matrices"""
        if rows <= 0 or cols <= 0:
            print("Enter correctly!")
            exit()
        self.rows = rows
        self.cols = cols
        if matrix:
            self.matrix = matrix
        else:
            self.matrix = []

    def input_matrix(self):
        """Function to create some kind of matrix"""
        print("Enter matrix element:")
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                element = input(f"Element in position [{i + 1}][{j + 1}]: ")
                try:
                    element = int(element)
                except ValueError:
                    try:
                        element = float(element)
                    except ValueError:
                        print("Enter correctly!")
                        return self.input_matrix()
                row.append(element)
            self.matrix.append(row)

    def __str__(self):
        """Function to show how matrix view"""
        matrix_string = ""
        for row in self.matrix:
            matrix_string += "\t".join(str(element) for element in row)
            matrix_string += "\n"
        return matrix_string

    def __add__(self, other):
        """Function to add several matrixes"""
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Error, matrices have differences!")

        final_matrix = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(self.matrix[i][j] + other.matrix[i][j])
            final_matrix.matrix.append(row)

        return final_matrix

    def __rmul__(self, multiplier):
        """For multiply matrix with constant"""
        final_matrix = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(self.matrix[i][j] * multiplier)
            final_matrix.matrix.append(row)
        return final_matrix

    def __mul__(self, other):
        """Function for multiply matrix for matrix"""
        if self.cols != other.rows:
            return print("Enter correctly!")
        final_matrix = [[0 for _ in range(other.cols)] for _ in range(self.rows)]
        for i in range(self.rows):
            for j in range(other.cols):
                counter = 0
                new_matrix = 0
                while counter < self.cols:
                    new_matrix += self.matrix[i][counter] * other.matrix[counter][j]
                    counter += 1
                final_matrix[i][j] = new_matrix
        return '\n'.join([' '.join([str(cell) for cell in row]) for row in final_matrix])

    def transpose_main_diagonal(self):
        """Matrix transposition function with respect to the main diagonal"""
        final_matrix = Matrix(self.cols, self.rows)
        for i in range(self.cols):
            row = []
            for j in range(self.rows):
                row.append(self.matrix[j][i])
            final_matrix.matrix.append(row)
        return final_matrix

    def transpose_side_diagonal(self):
        """Matrix transposition function with respect to the side diagonal"""
        final_matrix = Matrix(self.cols, self.rows)
        for i in range(self.cols):
            row = []
            for j in range(self.rows):
                row.append(self.matrix[self.rows - j - 1][self.cols - i - 1])
            final_matrix.matrix.append(row)
        return final_matrix

    def transpose_vertical(self):
        """Matrix transposition function with respect to the vertical"""
        final_matrix = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(self.matrix[i][self.cols - j - 1])
            final_matrix.matrix.append(row)
        return final_matrix

    def transpose_horizontal(self):
        """Matrix transposition function with respect to the horizontal"""
        final_matrix = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(self.matrix[self.rows - i - 1][j])
            final_matrix.matrix.append(row)
        return final_matrix

    def determinant(self):
        """Function to calculate determinant of matrix (Gaussian elimination)"""
        if self.rows != self.cols:
            print("Matrix must be square!")
        tmp_var_matrix = self.matrix
        tmp_var_rows = self.rows
        determinant = 1
        final_result = 0
        for i in range(tmp_var_rows):
            if tmp_var_matrix[i][i] == 0:
                for j in range(i + 1, tmp_var_rows):
                    if tmp_var_matrix[j][i] != 0:
                        tmp_var_matrix[i], tmp_var_matrix[j] = tmp_var_matrix[j], tmp_var_matrix[i]
                        determinant *= -1
                        break
                else:
                    return 0
            determinant *= tmp_var_matrix[i][i]
            for j in range(i + 1, tmp_var_rows):
                booster = tmp_var_matrix[j][i] / tmp_var_matrix[i][i]
                for k in range(i, tmp_var_rows):
                    tmp_var_matrix[j][k] -= booster * tmp_var_matrix[i][k]
            final_result = determinant
        return final_result

    def minor(self, i, j):
        """
        Function to find the minor of the matrix
        Description

        Parameters:
        i (int): needs to check space in picked row-place
        j (list): needs to check space in picked columns-place

        Returns:
        Minor of function after some math develop

        """
        final_minor = []
        minor_rows = 0
        for rows in range(self.rows):
            if rows == i:
                continue
            minor_cols = 0
            row = []
            for cols in range(self.cols):
                if cols == j:
                    continue
                row.append(self.matrix[rows][cols])
                minor_cols += 1
            final_minor.append(row)
            minor_rows += 1
        return Matrix(len(final_minor), len(final_minor[0]), final_minor)

    def inverse(self):
        """Function to find inverse of the matrix"""
        determinant = self.determinant()
        if determinant == 0:
            print("This matrix doesn't have an inverse.")
        if self.rows == 2 and self.cols == 2:
            final_matrix = Matrix(2, 2)
            final_matrix.matrix[0][0] = self.matrix[1][1]
            final_matrix.matrix[0][1] = -self.matrix[0][1]
            final_matrix.matrix[1][0] = -self.matrix[1][0]
            final_matrix.matrix[1][1] = self.matrix[0][0]
            for i in range(final_matrix.rows):
                for j in range(final_matrix.cols):
                    final_matrix.matrix[i][j] /= determinant
            return final_matrix
        else:
            inverse_matrix = Matrix(self.rows, self.cols, [[0] * self.cols for _ in range(self.rows)])
            for i in range(self.rows):
                for j in range(self.cols):
                    minor_symbol = (-1) ** (i + j)
                    minor_matrix = self.minor(i, j)
                    inverse_matrix.matrix[j][i] = minor_matrix.determinant() * minor_symbol / determinant
            return inverse_matrix

    @staticmethod
    def create_matrix():
        matrix_rows = int(input("Input number of rows in matrix >>>"))
        matrix_cols = int(input("Input number of cols in matrix >>>"))
        matrix = Matrix(matrix_rows, matrix_cols)
        matrix.input_matrix()
        return matrix


def main_program():
    """For main program part"""
    while True:
        print("Hi, it's matrix calculator v 0.1")
        print("""Enter command number to start:
        Commands list:
        1) Add matrices
        2) Multiply matrices by constant
        3) Multiply matrices
        4) Transposition of matrices
        5) Calculate a determinant
        6) Inverse matrix
        0) Exit""")
        choice = int(input(">>>"))
        if choice == 0:
            return print("Thanks for watching, goodbye!")
        elif choice == 1:
            print("Enter first matrix!")
            first_matrix = Matrix.create_matrix()
            print("Enter second matrix!")
            second_matrix = Matrix.create_matrix()
            final_matrix = first_matrix + second_matrix
            print("Matrix:")
            print(final_matrix)
        elif choice == 2:
            print("Enter matrix!")
            matrix = Matrix.create_matrix()
            multiplier = int(input("Enter constant to multiply your matrix >>>"))
            final_matrix = multiplier * matrix
            print(final_matrix)
        elif choice == 3:
            print("Enter first matrix!")
            first_matrix = Matrix.create_matrix()
            print("Enter second matrix!")
            second_matrix = Matrix.create_matrix()
            final_matrix = first_matrix * second_matrix
            print("Matrix:")
            print(final_matrix)
        elif choice == 4:
            print("Enter matrix!")
            matrix = Matrix.create_matrix()
            print("Which format of transposition you prefer?")
            print("""
            1. Main diagonal
            2. Side diagonal
            3. Vertical line
            4. Horizontal line
            """)
            transposition_var = int(input(">>>"))
            if transposition_var == 1:
                final_matrix = Matrix.transpose_main_diagonal(matrix)
                print("Matrix:")
                print(final_matrix)
            elif transposition_var == 2:
                final_matrix = Matrix.transpose_side_diagonal(matrix)
                print("Matrix:")
                print(final_matrix)
            elif transposition_var == 3:
                final_matrix = Matrix.transpose_vertical(matrix)
                print("Matrix:")
                print(final_matrix)
            elif transposition_var == 4:
                final_matrix = Matrix.transpose_horizontal(matrix)
                print("Matrix:")
                print(final_matrix)
        elif choice == 5:
            print("Enter matrix!")
            matrix = Matrix.create_matrix()
            final_matrix = Matrix.determinant(matrix)
            print("Matrix:")
            print(final_matrix)
        elif choice == 6:
            print("Enter matrix!")
            matrix = Matrix.create_matrix()
            final_matrix = Matrix.inverse(matrix)
            print("Matrix:")
            print(final_matrix)


main_program()
