# 2. Remove Empty Strings
# Input: ["apple", "", "banana", "", "cherry"]
# Task: Filter out empty strings.
# Expected Output: ["apple", "banana", "cherry"]

Input=["apple", "", "banana", "", "cherry"]
b=list(filter(lambda x :x!="",Input))
print(b)