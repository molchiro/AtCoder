# AtCoder

提出したコードをおいとく

## ヒント

https://algo-logic.info/how-to-think-cp/
https://qiita.com/DaikiSuyama/items/11f63a94d63fa72e8bf4

## 忘れがち

### ceil

`a+b-1//b`

### スニペット

あんまり使わないので体で覚えられていないやつ

- ２次元配列と三次元配列
- ４近傍と８近傍
- 同じく現在地から近傍への移動
- グラフ構造の入力
- インデックス付きで配列を受け取る

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

### heapqの次元

なるべく1次元で扱う。  
タプルにする場合も、(a, b, c)よりも(a, (b, c))の方が早い

### インタラクティブ問題のテスト

ARC184参照

