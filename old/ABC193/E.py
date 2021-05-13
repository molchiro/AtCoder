def euclid( a, b ):
  u1, u = 1, 0
  v1, v = 0, 1
  while b:
    q = a // b
    a, b = b, a-q*b
    u1, u = u, u1-q*u
    v1, v = v, v1-q*v
  return u1, v1

def solve_equation( mlist, alist ):
  m0 = mlist[0]
  x0 = alist[0]
  i = 1
  while i < len(mlist):
    m1 = mlist[i]
    x1 = alist[i]
    

    u, v = euclid(m0, m1)
    x0 = x1 * m0 * u + x0 * m1 * v
    m0 *= m1
    x0 %= m0
    i += 1
  return x0, m0

T = int(input())
for _ in range(T):
    X, Y, P, Q = list(map(int, input().split()))
    ans = float('inf')
    for t1 in range(X, X+Y):
        for t2 in range(P, P+Q):
            b, m = solve_equation([2*(X+Y), P+Q], [t1, t2])
            # print(b, m)
            if m == 0:
                continue
            ans = min(b, ans)
    if ans == float('inf'):
        ans = 'infinity'
    print(ans)