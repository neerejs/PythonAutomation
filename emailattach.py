import os
import smtplib
import imghdr
from email.message import EmailMessage

EMAIL_ADDRESS = 'youremail@gmail.com'
EMAIL_PASSWORD = 'yourpassword'

contacts = ['list of emails to send to ']

msg = EmailMessage()
msg['Subject'] = 'PDF Sent with Python'
msg['From'] = EMAIL_ADDRESS
msg['To'] = contacts
msg.set_content('PDF sent with python')

files = ['Certificate.pdf']

for file in files:
    with open(file, 'rb') as f:
        file_data = f.read()
        file_name = f.name

    msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename = 'Certificate.pdf')

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    
    smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)

    smtp.send_message(msg)

print('Success')