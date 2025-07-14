import asyncio
import smtplib

async def send_email(subject,body,to):
    pass

async def main():
    asyncio.create_task(send_email("email","this is an email","abc@gmail.com"))
    
    
    print("Doing other tasks")
 
 
asyncio.run(main())

