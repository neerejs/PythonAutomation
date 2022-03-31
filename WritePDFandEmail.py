from fpdf import FPDF
import os
import smtplib
import ssl
import imghdr
from email.message import EmailMessage
import pandas as pd
from datetime import date
from datetime import datetime

df = pd.read_excel('emailexceltest.xlsx')

EMAIL_ADDRESS = 'your email'
EMAIL_PASSWORD = 'your password'

contacts = ['sender email']

count = 1

msg = EmailMessage()
msg['Subject'] = 'PDF Sent with Python'
msg['From'] = EMAIL_ADDRESS
msg['To'] = contacts
msg.set_content('PDF sent with python')

for ind in df.index:
    em = df['Email'][ind]
    num = df['Project Number'][ind]
    stat = df['Status'][ind]
    name = df['Name'][ind]


    pdf = FPDF('P', 'mm', 'Letter')

    pdf.add_page()

    pdf.set_font('helvetica', 'B', 16)
    pdf.set_text_color(0,0,0)


    pdf.cell(120, 100, ' ' + em + ' | ' + num + ' | ' + stat + ' | ' + name + ' ')
    pdfname = 'pdf_'+ str(count) + '.pdf'
    pdf.output(pdfname)

    
    files = [pdfname]
    count = count + 1

    for file in files:
        with open(file, 'rb') as f:
            file_data = f.read()
            file_name = f.name

        msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename = pdfname)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    
    smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)

    smtp.send_message(msg)






print('Success')
