# sample test case: array= [1,11,3,0,15,5,2,4,10,7,12,6]
# time complexity=o(n),space complexity=o(n)
def largestRange(array):
    bestRange = []
    largestLength = 0
    nums = {}
    for num in array:  # iterating through the array and adding all elements to the hash table and setting them to True.
        nums[num] = True
    for num in array:  # Again iterating through the array to perform logic
        if not nums[num]:
            continue
        nums[num] = False  # setting current number to false as we are exploring
        currentLength = 1
        left = num - 1
        right = num + 1
        while left in nums:
            nums[left] = False  # setting left of current number to false as we are exploring
            currentLength += 1
            left -= 1
        while right in nums:
            nums[right] = False  # setting right of current number to false as we are exploring
            currentLength += 1
            right += 1
        if currentLength > largestLength:
            largestLength = currentLength
            bestRange = [left + 1, right - 1]
    return bestRange

