Q = int(input())
cumsum = [0]
top_idx = 0
for _ in range(Q):
    query = input()
    if query[0] == '1':
        _, l = list(map(int, query.split()))
        cumsum.append(l+cumsum[-1])
    elif query[0] == '3':
        _, k = list(map(int, query.split()))
        print(cumsum[top_idx+k-1]-cumsum[top_idx])
    else:
        top_idx += 1
