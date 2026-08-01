# AtCoder

提出したコードをおいとく

## ヒント

https://algo-logic.info/how-to-think-cp/
https://qiita.com/DaikiSuyama/items/11f63a94d63fa72e8bf4

## 忘れがち

### ceil

`(a+b-1)//b`

### スニペット

あんまり使わないので体で覚えられていないやつ

- ２次元配列と三次元配列
- ４近傍と８近傍
- 同じく現在地から近傍への移動

```
'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
```


### 再帰処理書く時

set rec でスニペット作ってある
```
import sys

sys.setrecursionlimit(10**9)
```

### modint

```
from atcoder.modint import Modint, ModContext

mod = 998244353
with ModContext(mod):
```

`[Modint(0) for _ in range(L)]` と `[Modint(0)]*L` は等価でないことに注意（後者はNG）


### 逆元
Modintを使うほどではない場面では逆元を掛け算

```
mod = 998244353
inv_a = pow(a, mod - 2, mod)

# inv_2 = pow(2, mod - 2, mod)
```

### メモ化再帰

```
from functools import cache

@cache
def solve():
    return
```

## メモ

### グリッド系の問題のコーナーケース

H=1, W=1が危ない

### グリッド系の問題の制約

`H, W <= 4*10^5` かと思いきや `H*W <= 4*10^5` でした

### 直線と線分をちゃんと読む

特に円の問題でミスりがち

### heapqの次元

なるべく1次元で扱う。  
タプルにする場合も、(a, b, c)よりも(a, (b, c))の方が早い

### インタラクティブ問題のテスト

ARC184参照

### 木のエッジケース

- ノードが1つのみ
- パスグラフ

### セグ木の取り扱い

更新クエリが無いものをsetで構築しない。前処理で捌いてから構築する。  
例えば上位2つの要素を持つseg木を構築したければ、各indexの上位2要素を持ってから構築する。  
opが重い場合は要注意
ex. https://atcoder.jp/contests/abc457/tasks/abc457_e

### bisectのやらかし

落ち着いて以下の図を見ながら頭を整理しながら使うこと。
https://qiita.com/manuo/items/e0bdbc5974800b7bd382
indexエラーを潰すために雑にindexを-1して爆死すること多し。番兵を入れるか例外処理を書くかする。

## 身についてない


### グリッド問題Tips

- 二次元の問題でH*Wに制約があるとき、短い方で全探索することがある。回転すれば場合分けしなくていい。
- グリッド系の問題で、片方の軸の問題をO(1)に落としてもう片方の軸で全探索


### サイクル検出

SCCにかけて、グループの要素数が1でないものは自己ループしている

### 狭義短調増加の変換

`Ai`​を`Ai​ − i`に置き換えることで、Aを狭義単調増加にする問題からAを広義単調増加にする問題に帰着させる
この形になると、

違反したらブロックをマージする
ブロックごとに代表値を決める
L1 なら中央値
L2 なら平均値
最大誤差最小化なら区間の上下限を見る

### 桁DPが苦手

- N以下をdpテーブルで表現してもいいが、dpテーブルは未満確定だけにして、Nピッタリのやつは管理するstateだけ持つ手もある
- leading-0も苦手。これもテーブルに載せない方が性にあっているかもしれない

NちょうどとN未満を分離した例
https://atcoder.jp/contests/abc465/submissions/77217203
そこからさらにリファクタした例
https://atcoder.jp/contests/abc465/submissions/77221242

## 意外と危ない

### INF

`float('inf')`を使うと上限のことを考えなくて良くなって便利だが、整数を扱う場合は速度に注意が必要。キャストに時間を食うっぽい。
`INF = 10**18`としておけば大抵大丈夫。
