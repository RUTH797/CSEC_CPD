
def find_minimum_moves(matrix):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == 1:
                return abs(i - 2) + abs(j - 2)

matrix = []
for _ in range(5):
    row = list(map(int, raw_input().split()))
    matrix.append(row)

result = find_minimum_moves(matrix)

print(result)
