N = int(input())

def solve(A_rem, B_rem, S):
    if A_rem > 0:
        solve(A_rem-1, B_rem, S+'A')
    if B_rem > 0:
        solve(A_rem, B_rem-1, S+'B')
    if A_rem + B_rem == 0:
        print(S)

solve(2**(N-1)-1, 2**(N-1), 'A')