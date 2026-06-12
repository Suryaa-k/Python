matrix = [
    [9, 3, 2, 6, 1],
    [2, 3, 4, 8, 2],
    [7, 3, 2, 9, 3],
    [1, 2, 3, 4, 4]
]

rows = len(matrix)
cols = len(matrix[0])

result = []
for i in range(rows):
    row = []
    for j in range(cols):
        total = 0
        if i > 0:          # up
            total += matrix[i-1][j]
        if i < rows - 1:   # down
            total += matrix[i+1][j]
        if j > 0:          # left
            total += matrix[i][j-1]
        if j < cols - 1:   # right
            total += matrix[i][j+1]
        row.append(total)
    result.append(row)

for row in result:
    print(row)