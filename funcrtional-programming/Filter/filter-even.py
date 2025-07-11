# 1. Filter Even Numbers
# Input: [1, 2, 3, 4, 5, 6]
# Task: Use filter to return a list of even numbers.
# Expected Output: [2, 4, 6]


a=[1,2,3,4,5,6]
b=list(filter(lambda x:x%2==0 ,a))
print(b)
