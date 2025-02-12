n = int(raw_input())
columns = list(map(int, raw_input().split()))

columns.sort()

print(" ".join(map(str, columns)))
