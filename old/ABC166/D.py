def f(X):
    for i in range(1, 120):
        for j in range(-63, 119):
            if i**5 - j**5 == X:
                return i, j
X = int(input())
print(*f(X))