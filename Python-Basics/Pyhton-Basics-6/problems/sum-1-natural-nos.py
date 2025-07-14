def print_nos(n):
    if n==0:
        return 0
    return print_nos(n-1)+n
print(print_nos(5))