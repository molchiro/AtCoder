A, B, C = list(map(int, input().split()))
print(max([0, C-max([0, A-B])]))