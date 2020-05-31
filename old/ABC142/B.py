N, K = list(map(int, input().split()))
H = list(map(int, input().split()))
H_ride = [1 for h in H if h >= K]
print(len(H_ride))