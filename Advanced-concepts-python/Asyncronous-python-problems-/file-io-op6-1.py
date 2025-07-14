import time
import asyncio
start = time.time()

async def fetch_file():
    print("starting to fecth a file")
    await asyncio.sleep(1)
    print("fetching file completed")

async def main():
    print("starting main")
    await asyncio.gather(
    fetch_file(),
    fetch_file(),
    fetch_file(),
    )
    print("Main Completed")
    # t1 = asyncio.create_task(fetch_file())
    # t2 = asyncio.create_task(fetch_file())
    # t3 = asyncio.create_task(fetch_file())
    # await asyncio.gather(t1, t2, t3)

asyncio.run(main())

end=time.time()
print("The time taken is :",end-start)