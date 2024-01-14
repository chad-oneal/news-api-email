import smtplib, ssl
import os

def send_email(subject, body, receiver="chadoneal3@gmail.com"):
    host = "smtp.gmail.com"
    port = 465

    username = "chadoneal3@gmail.com"
    password = os.getenv("PASSWORD")

    # Set the email headers and body
    message = f"From: {username}\nTo: {receiver}\nSubject: {subject}\n\n{body}"

    # Encode the message in UTF-8
    message = message.encode('utf-8')

    # Create a secure SSL context
    context = ssl.create_default_context()

    # Send the email
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
