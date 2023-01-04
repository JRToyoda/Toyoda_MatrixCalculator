class Matrix:
    def __init__(self, size):
        self.rows, self.columns = size.split()
        self.matrix = None
    def create(self):
        self.matrix = [[int(n) for n in input().split()] for _ in range(int(self.rows))]
    def generate(self):
        for row in self.matrix:
            for val in row:
                print(val, end=" ")
            print()
        print()
    def add(self, addend):
        if self.rows == addend.rows and self.columns == addend.columns:
            answer = [[self.matrix[i][j] + addend.matrix[i][j] for j in range(len(self.matrix[0]))]
                      for i in range(len(self.matrix))]
            for row in answer:
                for val in row:
                    print(val, end=" ")
                print()
            print()
        else:
            print("\nNot Possible")
    def subtract(self, subtrahend):
        if self.rows == subtrahend.rows and self.columns == subtrahend.columns:
            answer = [[self.matrix[i][j] - subtrahend.matrix[i][j] for j in range(len(self.matrix[0]))]
                      for i in range(len(self.matrix))]
            for row in answer:
                for val in row:
                    print(val, end=" ")
                print()
            print()
        else:
            print("\nNot Possible")
    def multiply(self, multiplier):
        if self.columns != multiplier.rows:
            print("\nNot Possible")
        else:
            answer = [[sum([self.matrix[i][k] * multiplier.matrix[j][k] for k in range(len(multiplier.matrix[0]))])
                       for j in range(len(multiplier.matrix))] for i in range(len(self.matrix))]
            for row in answer:
                for val in row:
                    print(round(val, 2), end=" ")
                print()
            print()


while True:
    choice = input("1. Generate Matrix\n2. Add Matrices\n3. Subtract Matrices\n4. Multiply Matrices\n"
                   "0. Exit\n\nChoose an operation: ")
    if choice == "1":
        matrix_a = Matrix(input("\nEnter size of Matrix: "))
        print("\nEnter Matrix: ")
        matrix_a.create()
        print()
        matrix_a.generate()
    elif choice == "2":
        matrix_a = Matrix(input("\nEnter size of Matrix A: "))
        print("\nEnter Matrix A: ")
        matrix_a.create()
        matrix_b = Matrix(input("\nEnter size of Matrix B: "))
        print("\nEnter Matrix B: ")
        matrix_b.create()
        print()
        matrix_a.add(matrix_b)
    elif choice == "3":
        matrix_a = Matrix(input("\nEnter size of Matrix A: "))
        print("\nEnter Matrix A: ")
        matrix_a.create()
        matrix_b = Matrix(input("\nEnter size of Matrix B: "))
        print("\nEnter Matrix B: ")
        matrix_b.create()
        print()
        matrix_a.subtract(matrix_b)
    elif choice == "4":
        matrix_a = Matrix(input("\nEnter size of Matrix A: "))
        print("\nEnter Matrix A: ")
        matrix_a.create()
        matrix_b = Matrix(input("\nEnter size of Matrix B: "))
        print("\nEnter Matrix B: ")
        matrix_b.create()
        print()
        matrix_a.multiply(matrix_b)
    elif choice == "0":
        break
    else:
        print("\nERROR\n")
