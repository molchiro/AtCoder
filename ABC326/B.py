def judge(n):
    a, b, c = str(n)
    return int(a)*int(b) == int(c)

N = int(input())

for n in range(N, 920):
    if judge(n):
        print(n)
        exit()