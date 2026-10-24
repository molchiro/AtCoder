H, W = list(map(int, input().split()))

C = [list(input()) for _ in range(H)]
# print(C)
for _ in range(4):
    # print(C[-1])
    while set(C[-1]) == set('.'):
        # print('found')
        C.pop()
    C = C[::-1]
    C = list(map(list, zip(*C)))

for row in C:
    print(''.join(row))