
def maximum(val1, val2, val3):
    """Return the maximum of 3 values passed as parameter"""
    max_val = val1
    if val2 > max_val:
        max_val = val2
    if val3 > max_val:
        max_val = val3
    return max_val

def minimum(val1, val2, val3, val4):
    """Return the minimum of 4 values passed as parameter"""
    min_val = val1
    if val2 < min_val:
        min_val = val2
    if val3 < min_val:
        min_val = val3
    if val4 < min_val:
        min_val - val4
    return min_val

print("The maximum of 3 values is " + str(maximum(12, 27, 36)))
print("The maximum of 3 values with max() is " + str(max(12, 27, 36)))
print("The minimum of 4 values is " + str(minimum(15, 9, 27, 14)))
print("The minimum of 4 values with min() is " + str(min(15, 9, 27, 14)))