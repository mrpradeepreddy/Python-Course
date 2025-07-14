import time
import asyncio

start=time.time()

async def get_movie_ticket():
    await asyncio.sleep(7)
    print("Got the movie tickets")

async def insta_like():
    await asyncio.sleep(3)
    print("finished insta")

async def main():
    task1=asyncio.create_task(get_movie_ticket())
    await insta_like()
    await task1
    # task1=asyncio.create_task(get_movie_ticket())
    # task2=asyncio.create_task(insta_like())
    # await asyncio.gather(task1,task2)
    # await (task1(),task2(),..) for multiple tasks

asyncio.run(main())

end=time.time()
print("The time of executin",(end-start))