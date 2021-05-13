K, N= list(map(int, input().split()))
A = list(map(int, input().split()))
A_dist = [A[i+1] - A[i] for i in range(N-1)]
A_dist.append(K+A[0]-A[-1])
print(K-max(A_dist))