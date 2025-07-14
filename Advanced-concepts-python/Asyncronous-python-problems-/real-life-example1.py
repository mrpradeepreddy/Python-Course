import time 

start=time.time()
def buy_movie_ticket():
    time.sleep(3)
    print("I got the movie ticket")

def insta_like():
    time.sleep(2)
    print("Finished instagram")

def main():
    buy_movie_ticket()
    insta_like()

main()

end=time.time()

print("The time taken is :",end-start)
