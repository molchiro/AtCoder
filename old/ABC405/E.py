from atcoder.modint import Modint, ModContext

mod = 998244353

A, B, C, D = list(map(int, input().split()))

with ModContext(mod):
    kaijo = [Modint(1)]
    for i in range(1, 5*(10**6)):
        prev = kaijo[-1]
        kaijo.append(prev*Modint(i))
    
    ans = Modint(0)
    # 一番右にあるりんごの位置
    for i in range(A, A+B+1):
        # りんごより右側にあるオレンジの個数
        b = A+B-i

        # 一番右のりんごより左がわの、りんごとオレンジの並び替え
        # print(B-b+A-1, B-b, A-1)
        # print(kaijo[B-b+A-1].val(), kaijo[B-b].val(), kaijo[A-1].val())
        delta = Modint(kaijo[B-b+A-1].val())
        delta *= kaijo[B-b].inv()
        delta *= kaijo[A-1].inv()
        # 一番右のりんごより右がわの、残りのものが取れる組み合わせ
        delta *= kaijo[b+C+D]
        delta *= kaijo[C].inv()
        delta *= kaijo[b+D].inv()
        ans += delta

    print(ans.val())
