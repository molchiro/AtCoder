N = int(input())

ga, sa, ba = list(map(int, input().split()))
a = {'g': ga, 's': sa, 'b': ba}
gb, sb, bb = list(map(int, input().split()))
b = {'g': gb, 's': sb, 'b': bb}


rate = [['g', ga/gb], ['s', sa/sb], ['b', ba/bb]]
rate.sort(key=lambda x: x[1])

A = {'g': 0, 's': 0, 'b': 0, 'd': N}
for r in rate:
    if r[1] < 1:
        A[r[0]] = A['d']//a[r[0]]
        A['d'] -= A[r[0]]

B = {'g': 0, 's': 0, 'b': 0, 'd': A['d']+A['g']*b['g']+A['s']*b['s']+A['b']*b['b']}
rate.sort(reverse=True ,key=lambda x: x[1])
for r in rate:
    if r[1] > 1:
        A[r[0]] = A['d']//a[r[0]]
        A['d'] -= A[r[0]]

print(B['d']+B['g']*a['g']+B['s']*a['s']+B['b']*a['b'])
