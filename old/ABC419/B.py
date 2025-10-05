Q = int(input())
box = []
for _ in range(Q):
    query = input()
    if query[0] == '1':
        _, x = list(map(int, query.split()))
        box.append(x)
    else:
        box.sort(reverse=True)
        print(box.pop())