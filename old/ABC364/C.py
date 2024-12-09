N, X, Y = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))

def solve(input_list, limit):
    c = 0
    accum = 0
    for x in sorted(input_list, reverse=True):
        c += 1
        accum += x
        if accum > limit:
            break
    return c
    
print(min(solve(A, X), solve(B, Y)))