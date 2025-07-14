def check_for_word():
    word="learning"
    with open("Python-Basic-7\problems\sample.txt","r") as f:
        data=f.read()
        if data.find(word) !=-1:
            print("Found")
        else:
            print("Not found")
check_for_word()