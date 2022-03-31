import smtplib
import ssl
from email.message import EmailMessage
import pandas as pd
from datetime import date
from datetime import datetime

df = pd.read_excel('emailexceltest.xlsx')

for ind in df.index:
    if(df['Status'][ind] == "In Progress" ):
        if((df['End'][ind]).date() < (datetime.now().date())):
            name = df['Name'][ind]
            subject = "Import Project Information"
            body = "Hello " + name + "."
            sender_email = "neerejpython@gmail.com"
            receiver_email = "sgneerej@gmail.com"
            password = "Tharun2001@#"

            message = EmailMessage()
            message["From"] = sender_email
            message["To"] = receiver_email
            message["Subject"] = subject

            html = f"""
            <html>
                <body>
                    <h1>{subject}</h1>
                    <p>{body}</p>
                </body>
            </html>
            """

            message.add_alternative(html, subtype="html")
            context = ssl.create_default_context()

            print("Sending Email!")

            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, message.as_string())

print("Success")


