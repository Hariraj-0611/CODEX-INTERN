import numpy as np

# Function to display matrix nicely
def display_matrix(matrix):
    print(np.array(matrix))

# Function to input a matrix from the user
def input_matrix():
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    print(f"Enter the elements for the matrix ({rows}x{cols}):")
    matrix = []
    for i in range(rows):
        row = list(map(int, input(f"Enter elements of row {i+1} (separated by space): ").split()))
        matrix.append(row)
    return np.array(matrix)

# Function to add two matrices
def add_matrices(matrix1, matrix2):
    if matrix1.shape == matrix2.shape:
        return matrix1 + matrix2
    else:
        print("Error: Matrices must have the same dimensions for addition.")
        return None

# Function to subtract two matrices
def subtract_matrices(matrix1, matrix2):
    if matrix1.shape == matrix2.shape:
        return matrix1 - matrix2
    else:
        print("Error: Matrices must have the same dimensions for subtraction.")
        return None

# Function to multiply two matrices
def multiply_matrices(matrix1, matrix2):
    if matrix1.shape[1] == matrix2.shape[0]:
        return np.dot(matrix1, matrix2)
    else:
        print("Error: The number of columns in the first matrix must equal the number of rows in the second matrix.")
        return None

# Function to transpose a matrix
def transpose_matrix(matrix):
    return matrix.T

# Function to calculate the determinant of a matrix
def determinant_matrix(matrix):
    if matrix.shape[0] == matrix.shape[1]:  # Square matrix
        return np.linalg.det(matrix)
    else:
        print("Error: Determinant can only be calculated for square matrices.")
        return None

# Main program to interact with the user
def matrix_operations_tool():
    print("Welcome to the Matrix Operations Tool!")

    while True:
        print("\nSelect an operation:")
        print("1. Add Matrices")
        print("2. Subtract Matrices")
        print("3. Multiply Matrices")
        print("4. Transpose Matrix")
        print("5. Calculate Determinant")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':  # Add Matrices
            print("\nEnter the first matrix:")
            matrix1 = input_matrix()
            print("\nEnter the second matrix:")
            matrix2 = input_matrix()
            result = add_matrices(matrix1, matrix2)
            if result is not None:
                print("\nResult of Addition:")
                display_matrix(result)

        elif choice == '2':  # Subtract Matrices
            print("\nEnter the first matrix:")
            matrix1 = input_matrix()
            print("\nEnter the second matrix:")
            matrix2 = input_matrix()
            result = subtract_matrices(matrix1, matrix2)
            if result is not None:
                print("\nResult of Subtraction:")
                display_matrix(result)

        elif choice == '3':  # Multiply Matrices
            print("\nEnter the first matrix:")
            matrix1 = input_matrix()
            print("\nEnter the second matrix:")
            matrix2 = input_matrix()
            result = multiply_matrices(matrix1, matrix2)
            if result is not None:
                print("\nResult of Multiplication:")
                display_matrix(result)

        elif choice == '4':  # Transpose Matrix
            print("\nEnter the matrix to transpose:")
            matrix = input_matrix()
            result = transpose_matrix(matrix)
            print("\nTransposed Matrix:")
            display_matrix(result)

        elif choice == '5':  # Calculate Determinant
            print("\nEnter the matrix to calculate the determinant:")
            matrix = input_matrix()
            result = determinant_matrix(matrix)
            if result is not None:
                print(f"\nDeterminant: {result}")

        elif choice == '6':  # Exit
            print("Exiting the Matrix Operations Tool. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

# Run the matrix operations tool
if __name__ == "__main__":
    matrix_operations_tool()
324342