import smtplib
import ssl
import os

def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    password = os.getenv('gmailPass')
    receiver = 'cookin32@gmail.com'
    sender = receiver
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(sender, password=password)
        server.sendmail(sender, receiver, message)