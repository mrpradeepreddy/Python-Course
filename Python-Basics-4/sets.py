#unodered sets
#unique,immuatble
s={}   #dictionary
se=set()
print(type(se))
sep={1,2,3,4,2,2,3,4}

print(sep)
print(len(sep))
sep.add(5)
sep.add((1,2,3))
print(sep)
sep.remove(2)
print(sep)
# sep.clear()
# print(sep)

sep.pop()
print(sep)

set1={2,3,4}
set2={4,5,6}
print(set1.union(set2))
print(set1.intersection(set2))