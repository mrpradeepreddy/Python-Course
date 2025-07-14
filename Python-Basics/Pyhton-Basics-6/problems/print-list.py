def print_list(list,idx=0):
    if idx==len(list):
        return
    print(list[idx])
    print_list(list,idx+1)

fruit=[1,2,3,4]
print_list(fruit)