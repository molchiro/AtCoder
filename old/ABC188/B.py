from operator import mul

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
inner_product = sum(map(mul, A, B))
print('Yes' if inner_product == 0 else 'No')