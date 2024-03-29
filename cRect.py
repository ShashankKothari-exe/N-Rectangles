def countRectangles(i, j):
    return (i * j * (i + 1) * (j + 1)) // 4

i = input("Enter no. of Rows:")
j = input("Enter no. of Columns:")
print(countRectangles(i, j))  
