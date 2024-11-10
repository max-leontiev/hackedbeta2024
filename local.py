# Function to create an n x m matrix
def create_matrix(n, m):
    matrix = []
    print(f"Enter the elements of the {n}x{m} matrix:")
    for i in range(n):
        row = []
        for j in range(m):
            # Take input for each element in the row
            element = int(input(f"Element at ({i+1},{j+1}): "))
            row.append(element)
        matrix.append(row)
    return matrix

# Take inputs for n and m
n = int(input("Enter the number of rows (n): "))
m = int(input("Enter the number of columns (m): "))

# Create the matrix
matrix = create_matrix(n, m)

# Print the matrix
print("The created matrix is:")
for row in matrix:
    print(row)
