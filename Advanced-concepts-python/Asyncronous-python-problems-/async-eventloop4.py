import asyncio
#create and access a new asyncio event loop
loop=asyncio.new_event_loop()
#define Task
task1=asyncio.sleep(2)
#run / execute task
loop.run_until_complete(task1)
#report message
print("done")