N, A, B = list(map(int, input().split()))
AB = A+B
D = list(map(int, input().split()))
Dmod = set([d%AB for d in D])
Dmod_sorted = sorted(list(Dmod))
# print(Dmod_sorted)
l = Dmod_sorted[0]
r = Dmod_sorted[-1]
continuous_work_days = l + (AB-r-1)
prev = l
for i in range(len(Dmod_sorted)-1):
    continuous_work_days = max(continuous_work_days, Dmod_sorted[i+1]-Dmod_sorted[i]-1)
    # print(continuous_work_days)
print('Yes' if continuous_work_days >= B else 'No')