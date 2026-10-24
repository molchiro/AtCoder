X, Y, L, R, A, B = list(map(int, input().split()))

if A <= L < R <= B:
    print((L-A)*Y + (R-L)*X + (B-R)*Y)
elif A <= L <= B <= R:
    print((L-A)*Y + (B-L)*X)
    
elif A < B <= L < R:
    print((B-A)*Y)
elif L <= A < B <= R:
    print((B-A)*X)
elif L <= A < R <= B:
    print((R-A)*X + (B-R)*Y)
elif L < R <= A < B:
    print((B-A)*Y)
