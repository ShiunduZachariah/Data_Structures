# Binary Search
# if similar numbers are in the list

def rotations(nums, n):
    low = 0
    high = len(nums) - 1

    while low <= high:
        if len(nums) == 0:
            print("Zero elements")
            return False
        else:
            midpoint = (low + high) // 2
            prev = midpoint - 1
            next = midpoint + 1

            if nums[midpoint] <= nums[prev] and nums[midpoint] <= nums[next]:
                return midpoint
            elif nums[midpoint] <= nums[high]:
                high = midpoint - 1
            elif nums[midpoint] >= nums[low]:
                low = midpoint + 1
            else:
                return 0


numbers = [343, 232, 3232, 26, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

n = len(numbers)
print(rotations(numbers, n))

nums = [19, 21, 22, 23, 24, 25, 1, 4, 7, 13, 14, 18]
n = len(nums)

print(rotations(nums, n))
