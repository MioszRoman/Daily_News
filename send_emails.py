import smtplib, ssl
import os

def send_email(message):
    """Function for sending emails"""
    host = "smtp.gmail.com"
    port = 465

    username = "mioszroman@gmail.com"
    password = os.getenv("PASSWORD")
    receiver = "mioszroman@gmail.com"

    context = ssl.create_default_context()
    my_message = message

    with smtplib.SMTP_SSL(host=host, port=port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, my_message)