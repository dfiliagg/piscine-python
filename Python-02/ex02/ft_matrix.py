import sys

def ft_sum_columns(matrix, column):
    i = 0
    sum_column = []
    while i < column:
        sum = 0
        for row in matrix:
            sum += row[i]
        sum_column.append(sum)
        i += 1
    print(sum_column)

def ft_sum_row(matrix):
    sum_row = []
    for row in matrix:
        sum = 0
        for element in row:
            sum += element
        sum_row.append(sum)
    print(sum_row)

def ft_print_m (matrix):
    print("The inserted matrix is:")
    for i in matrix:
        print(i)

if len(sys.argv) != 3:
    print("Error! Usage: python3 ft_matrix.py <n> <m>")
    exit()
row = int(sys.argv[1])
column = int(sys.argv[2])
matrix = []

for i in range(row):
    r = []
    for j in range(column):
        message = "Insert the element in the position ("+str(i)+", "+str(j)+"): "
        r.append(float(input(message)))
    matrix.append(r)
ft_print_m(matrix)
print("The sum over rows is:")
ft_sum_row(matrix)
print("The sum over columns is:")
ft_sum_columns(matrix, column)
