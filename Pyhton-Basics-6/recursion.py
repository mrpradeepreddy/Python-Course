
def show(n):
    if n==0:
        return
    print(n)
    show(n-1)
show(5)


# def show(n,fact=1):
#     if n==0:
#         return
#     fact*=n
#     print(fact)
#     show(n-1,fact)
# show(5)


