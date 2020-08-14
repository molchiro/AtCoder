K = int(input())
rem_set = set()
rem = 7%K
i = 1
while True:
    if rem == 0:
        print(i)
        break
    if rem in rem_set:
        print(-1)
        break
    i += 1
    rem_set.add(rem)
    rem = (rem*10 + 7)%K