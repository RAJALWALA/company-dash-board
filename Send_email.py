import os
import smtplib,ssl


def Send_email(message):
    host = "smtp.gmail.com"
    port = 465
    user_name = "bunnyaluvala@gmail.com"
    password = os.getenv("PASSWORD")
    recevier_email = "bunnyaluvala@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(user_name, password)
        server.sendmail(user_name, recevier_email, message)
