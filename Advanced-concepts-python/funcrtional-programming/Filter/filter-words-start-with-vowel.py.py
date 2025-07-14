# 4. Filter Words Starting With a Vowel
# Input: ["apple", "banana", "orange", "grape", "avocado"]
# Task: Filter words that start with a vowel (a, e, i, o, u).
# Expected Output: ["apple", "orange", "avocado"]

Input=["apple", "banana", "orange", "grape", "avocado"]
vowels=['a','e','i','o','u']
a=list(filter(lambda x:x[0].lower() in vowels,Input))
print(a)