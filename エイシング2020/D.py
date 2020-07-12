N = int(input())
X = input()
fn = {0: 0}
fn_keys = {0}

def culc_fn(n, fn, fn_keys):
    # fn_keysに入る値がバカでかくて低速なのが敗因？
    if not n in fn_keys:
        popcount = bin(n).count('1')
        tmp = n%popcount
        fn[n] = culc_fn(tmp, fn, fn_keys) + 1
        fn_keys.add(n)
    return fn[n]

for i in range(N):
    tmp = int(X[:i] + ('0' if X[i] == '1' else '1') + X[i+1:], 2)
    print(culc_fn(tmp, fn, fn_keys))