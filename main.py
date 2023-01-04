class Matrix:
    def __init__(self, size):
        self.rows, self.columns = size.split()
        self.matrix = []

    def create(self):
        self.matrix = [[int(n) for n in input().split()] for _ in range(int(self.rows))]

    def generate(self):
        for row in self.matrix:
            for val in row:
                print(val, end=" ")
            print()
        print()

    def answer(self):
        for row in self.matrix:
            for val in row:
                print(val, end=" ")
            print()
        print()

    def add(self, addend):
        if self.rows == addend.rows and self.columns == addend.columns:
            self.matrix = [[self.matrix[i][j] + addend.matrix[i][j] for j in range(len(self.matrix[0]))] for
                           i in range(len(self.matrix))]
        else:
            print("\nNot Possible")

    def subtract(self, subtrahend):
        if self.rows == subtrahend.rows and self.columns == subtrahend.columns:
            self.matrix = [[self.matrix[i][j] - subtrahend.matrix[i][j] for j in range(len(self.matrix[0]))] for
                           i in range(len(self.matrix))]
            self.answer()
        else:
            print("\nNot Possible")

    def multiply(self, multiplier):
        multiplier.matrix = [[multiplier.matrix[i][j] for i in range(len(multiplier.matrix))]
                             for j in range(len(multiplier.matrix[0]))]
        if self.columns != multiplier.rows:
            print("\nNot Possible")
        else:
            self.matrix = [[sum([self.matrix[i][k] * multiplier.matrix[j][k] for k in range(len(multiplier.matrix[0]))])
                            for j in range(len(multiplier.matrix))] for i in range(len(self.matrix))]
            self.answer()
            print()


while True:
    choice = input("1. Generate Matrix\n2. Add Matrices\n3. Subtract Matrices\n4. Multiply Matrices\n"
                   "0. Exit\n\nChoose an operation: ")
    if choice == "1" or choice == "2" or choice == "3" or choice == "4":
        matrix_a = Matrix(input("\nEnter size of Matrix A: "))
        print("\nEnter Matrix A: ")
        matrix_a.create()
        if choice == "1":
            print()
            matrix_a.generate()
        else:
            matrix_b = Matrix(input("\nEnter size of Matrix B: "))
            print("\nEnter Matrix B: ")
            matrix_b.create()
            print()
            if choice == "2":
                matrix_a.add(matrix_b)
            elif choice == "3":
                matrix_a.subtract(matrix_b)
            elif choice == "4":
                matrix_a.multiply(matrix_b)
    elif choice == "0":
        break
    else:
        print("\nERROR\n")
