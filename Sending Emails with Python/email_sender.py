import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(
    Path('c:\Python\Sending Emails with Python\index.html').read_text())
email = EmailMessage()
email['from'] = 'Sendler'
email['to'] = 'SendlerEmail@gmail.com'
email['subject'] = 'You won 1000000 dollars'

email.set_content(html.substitute({'name': 'TinTin'}), 'html')

with smtplib.SMTP_SSL(host='smtp.gmail.com', port=465) as connection:
    server_email = 'email@gmail.com'
    server_pw = 'pasword'
    connection.login(server_email, server_pw)
    connection.send_message(email)


"""
IF GOOGLE ISN'T allowing you to send emails, there is a solution to this problem 
as well https://stackoverflow.com/questions/72480454/sending-email-with-python-google-disables-less-secure-apps
(you will have to navigate to https://myaccount.google.com/apppasswords).
"""
