from itertools import combinations_with_replacement

N = int(input())

repunits = [int(str('1')*i) for i in range(1, 15)]
nums = []
for elements in combinations_with_replacement(repunits, 3):
    nums.append(sum(elements))
nums.sort()
# print(len(nums))
print(nums[N-1])