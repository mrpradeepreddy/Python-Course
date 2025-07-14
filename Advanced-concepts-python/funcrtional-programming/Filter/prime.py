# 5. Filter Prime Numbers
# Input: [2, 3, 4, 5, 6, 7, 8, 9, 10]
# Task: Write a helper function is_prime(n) and use it with filter.
# Expected Output: [2, 3, 5, 7]

def is_prime(n):
    if n<2:
        return False
    for i in range(2,int(n*0.5)+1):
        if n%i==0:
            return False
    return True
numbers= [2, 3, 4, 5, 6, 7, 8, 9, 10]
a=list(filter(is_prime()))
print(a)