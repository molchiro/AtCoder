from functools import cache

N = int(input())
cards = [list(map(int, input().split())) for _ in range(N)]

@cache
def solve(S):
    global cards, N
    local_cards = []
    n = 0
    for i, s in enumerate(S):
        if s == '1':
            local_cards.append((*cards[i], i))
            n += 1
    if n == 0:
        return False
    pairs = []
    for i in range(n-1):
        for j in range(i+1, n):
            if local_cards[i][0] == local_cards[j][0] or local_cards[i][1] == local_cards[j][1]:
                pairs.append((local_cards[i][2], local_cards[j][2]))
    if len(pairs) == 0:
        return False
    # print(S, local_cards, pairs)
    # input()
    for i, j in pairs:
        new_S = ''.join([s if k!= i and k != j else '0' for k, s in enumerate(S)])
        if not solve(new_S):
            return True
    return False

print('Takahashi' if solve('1'*N) else 'Aoki')