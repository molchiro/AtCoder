N = int(input())

def check_kaibun(S):
    for i in range(len(S)//2):
        if S[i] != S[-i-1]:
            return False
    return True

assert check_kaibun('121')
assert check_kaibun('12') == False
assert check_kaibun('22')

ans = 1
x = 1
x3 = 1
while x3 <= N:
    if check_kaibun(str(x3)):
        ans = x3
    x += 1
    x3 = x**3
print(ans)