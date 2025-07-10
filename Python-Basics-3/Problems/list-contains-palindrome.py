li=list(map(int,input().split()))
li1=li.copy()
li1.reverse()
if li==li1:
    print("palindrome")
else:
    print("no")