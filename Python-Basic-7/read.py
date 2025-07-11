#read write operations on file
f=open("Python-Basic-7\data.txt","rt")

#read
data=f.read(5)
print(data)

#readline means single line
line1=f.readline()
print(line1)

#write
f=open("Python-Basic-7\data.txt","w")

f.write("I want to leatn javascript.123")

f.close()
