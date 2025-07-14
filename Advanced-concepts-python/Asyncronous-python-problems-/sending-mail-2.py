import asyncio
from email.message import EmailMessage
import aiosmtplib

async def send_email(subject, body, to):
    message = EmailMessage()
    message["From"] = "mr.dpureddy@gmail.com"
    message["To"] = "mrppradeepreddy@gmail.com"
    message["Subject"] = "good morning"
    message.set_content(body)

    await aiosmtplib.send(
        message,
        hostname="smtp.gmail.com",
        port=587,
        start_tls=True,
        username="mr.dpureddy@gmail.com",
        password=""
    )
    print("Email sent!")

async def main():
    asyncio.create_task(send_email("Hello", "This is async email", "abc@gmail.com"))
    print("Doing other tasks while email is being sent...")
    await asyncio.sleep(3)  # Give time for background task to complete

asyncio.run(main())