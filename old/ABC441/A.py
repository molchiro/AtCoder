P, Q = list(map(int, input().split()))
X, Y = list(map(int, input().split()))

print('Yes' if P <= X < P+100 and Q <= Y < Q+100 else 'No')