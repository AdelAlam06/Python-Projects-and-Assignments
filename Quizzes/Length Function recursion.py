def getLength(items):
    if (bool(items) == False):
        return 0
    else:
        return 1 + getLength(items[:-1])


nums = [1, 2, 3, 4]
print(getLength(nums))
