list(map(int, input().split()))

grid = grid[::-1]
grid = list(map(list, zip(*grid)))