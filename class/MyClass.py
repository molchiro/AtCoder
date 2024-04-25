from functools import total_ordering
import dataclasses

# 使うやつだけ残して実装する
# total_orderingは10〜30%ほど遅くなる可能性があるので定数倍が気になる時はそれぞれ実装する

@dataclasses.dataclass
@total_ordering
class MyClass:
    value: int

    def __eq__(self, other):
        return 

    def __gt__(self, other):
        return 
    
    def __add__(self,other):
        return self.value + other.value

    def __sub__(self,other):
        return self.value - other.value

    def __mul__(self,other):
        return self.value * other.value

    def __truediv__(self,other):
        return self.value / other.value

    def __floordiv__(self,other):
        return self.value // other.value
    
    def __and__(self,other):
        return self.value & other.value

    def __or__(self,other):
        return self.value | other.value