def match_len(target_text: str, search_text: str):
    res = 0
    for x in target_text:
        if x == search_text[res]:
            res += 1
        if res == len(search_text):
            break
    return res

N, T  = input().split()
N = int(N)
T_reversed = T[::-1]
prefix_match_len_list = []
suffix_match_len_list = []
for _ in range(N):
    S = input()
    prefix_match_len_list.append(match_len(S, T))
    suffix_match_len_list.append(match_len(S[::-1], T_reversed))

prefix_match_len_list.sort(reverse=True)
suffix_match_len_list.sort()
# print(heads)
# print(tails)
idx = 0
ans = 0
for l in prefix_match_len_list:
    while idx < N and l + suffix_match_len_list[idx] < len(T):
        idx += 1
    # print(n, idx)
    ans += N-idx
print(ans)