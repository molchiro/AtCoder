# AtCoder

提出したコードをおいとく

## 忘れがち

### 再帰処理書く時

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

### heapqの次元

なるべく1次元で扱う。  
タプルにする場合も、(a, b, c)よりも(a, (b, c))の方が早い