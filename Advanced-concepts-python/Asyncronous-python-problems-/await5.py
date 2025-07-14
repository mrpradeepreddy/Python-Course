import asyncio
async def square(num):
    return num*num
async def main():
    x=await square(5)
    print(x)

    y=await square(10)
    print(y)

    z=await square(15)
    print(z)
asyncio.run(main())