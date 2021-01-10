a, b = list(map(int, input().split()))
a_ = str(a)*b
b_ = str(b)*a
print(a_ if a_ < b_ else b_)