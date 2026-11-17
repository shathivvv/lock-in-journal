def contains_duplicate(nums):
    for i in range(len(nums)):
        for j in range( i+1, len(nums)):
            if nums[i] == nums[j]:
                return True

    return False
#Time O(n2)
#Space O(1)


def contains_duplicate_fast(nums):
    seen = set()

    for num in nums:
        if num in seen:
            return True
        else:
            seen.add(num)
    return False
#Time O(n)
#Space O(n) because as input grows the space complexity increase say there are 100 unique numbers the set will be 100 but when 1000 it goes to 1000

# Tests: don't change these
assert contains_duplicate([1, 2, 3, 1]) == True
assert contains_duplicate([1, 2, 3, 4]) == False
assert contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) == True
assert contains_duplicate([]) == False
assert contains_duplicate([7]) == False
assert contains_duplicate([-1, -1]) == True
print("All tests passed")


# Tests: don't change these
assert contains_duplicate_fast([1, 2, 3, 1]) == True
assert contains_duplicate_fast([1, 2, 3, 4]) == False
assert contains_duplicate_fast([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) == True
assert contains_duplicate_fast([]) == False
assert contains_duplicate_fast([7]) == False
assert contains_duplicate_fast([-1, -1]) == True
print("All tests passed")