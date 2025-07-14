# f=open("saple.txt","a")
# f.write("Hi everyone\nwe are learning File I/o\n")
# f.write("using java\ni like programming in java")
# f.close()

with open("sample.txt","w") as f:
    f.write("Hi everyone\nwe are learning File I/o\n")
    f.write("using java\ni like programming in java")
