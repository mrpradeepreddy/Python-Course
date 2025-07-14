with open("Python-Basic-7\problems\sample.txt","r") as f:
    data=f.read()
new_data=data.replace("java","Python")
print(new_data)