def count_ones_by_shift_2(num):
    num = (num & 0x55555555) + (num >> 1 & 0x55555555) 
    num = (num & 0x33333333) + (num >> 2 & 0x33333333)
    num = (num & 0x0F0F0F0F) + (num >> 4 & 0x0F0F0F0F)
    num = (num & 0x00FF00FF) + (num >> 8 & 0x00FF00FF)
    num = (num & 0x0000FFFF) + (num >>16 & 0x0000FFFF)
    return num

S = input()
T = input()
# S = '1'*10**6
# T = '1'*10**3
size = len(T)
ans = float('inf')
for i in range(len(S)-size+1):
    ST = int(S[i:i+size], 2)^int(T, 2)
    # print(ST)
    ans = min(ans, count_ones_by_shift_2(ST))

print(ans)


