tuple=(1,4,9,16,25,36,49,64,81,100)
i=0
while i<len(tuple)-1:
    print("finding")
    if tuple[i]==64:
        print(i)
        break
    i+=1
print("end loop")  