import time

start = time.time()

def fetch_file():
    print("starting to fecth a file")
    time.sleep(1)
    print("fetching file completed")

def main():
    print("starting main")
    fetch_file(),
    fetch_file(),
    fetch_file(),
    print("Main Completed")

main()

end=time.time()
print("The time taken is :",end-start)