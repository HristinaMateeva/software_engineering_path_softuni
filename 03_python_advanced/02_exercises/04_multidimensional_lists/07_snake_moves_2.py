rows, columns = [int(el) for el in input().split()]
word = list(input())

idx = 0
matrix = []

for row in range(rows):
    row_elements = []
    for col in range(columns):
        row_elements.append(word[idx % len(word)])
        idx += 1
    if row % 2 == 0:
        print(*row_elements, sep="")
    else:
        print(*reversed(row_elements), sep="")
