# def two_sums(nums, target):
#     pair = set()

#     for x in range(len(nums)):
#         for y in range(len(nums)):
#             if nums[x] == target - nums[y]:
#                 pair.add(x)
#                 pair.add(y)
#             else:
#                 continue

#     return list(pair)

def two_sums(nums, target):
    hashmap = {}
    for i, curr in enumerate(nums):
        x = target - curr
        
        if x in hashmap:
            return [i, hashmap.get(x)]

        hashmap[curr] = i

    return [] # Zero Solutions

nums = [2, 7, 11, 15]
target = 18
two_sums(nums, target)
