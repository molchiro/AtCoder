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