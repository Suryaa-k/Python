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
        if i > 0 and j > 0:           # top-left
            total += matrix[i-1][j-1]
        if i > 0 and j < cols - 1:    # top-right
            total += matrix[i-1][j+1]
        if i < rows-1 and j > 0:      # bottom-left
            total += matrix[i+1][j-1]
        if i < rows-1 and j < cols-1: # bottom-right
            total += matrix[i+1][j+1]
        row.append(total)
    result.append(row)

for row in result:
    print(row)