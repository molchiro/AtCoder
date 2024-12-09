
from functools import cache

nums = []

for i in range(2, 10**6):
    if not '0' in str(i):
        nums.append(i)

num_rev = {}
for num in nums:
    rev = int(str(num)[::-1])
    num_rev[num] = num*rev

@cache
def culc(n):
    global nums, num_rev

    # 回文かつ０を含まなければそのまま返す
    if not '0' in str(n) and str(n) == str(n)[::-1]:
        return n
    
    # i*culc(n//(i*rev))*revが回文になっていれば返す
    for i in nums:
        if n%num_rev[i]:
            continue

        tmp = culc(n//num_rev[i])
        if tmp == '':
            continue

        return str(i)+'*'+str(tmp)+'*'+str(i)[::-1]

    # 回文にならなければ空文字を返す
    return ''


N = int(input())
ans = culc(N)
print(-1 if ans=='' else ans)