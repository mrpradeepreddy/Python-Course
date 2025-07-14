# 3. Filter Positive Numbers
# Input: [-3, -1, 0, 2, 4, -5]
# Task: Keep only numbers greater than 0.
# Expected Output: [2, 4]

Input=[-3, -1, 0, 2, 4, -5]
a=list(filter(lambda x:x>0,Input))
print(a)