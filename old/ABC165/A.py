K = int(input())
A, B= list(map(int, input().split()))
M = B//K
print('OK' if K*M >= A else 'NG')