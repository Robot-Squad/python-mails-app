# Written by: Robot Squad
# NOTE:
#   Before running this sketch go to your account settings and allow less secure apps to access mail.
# Please subscribe to Robot Squad.
import smtplib
import ssl
server_smtp = "smtp.gmail.com"
port = 587
userid = input("enter your email address: ")
password = input("enter your password: ")
recipient = input("recipient: ")
msg = input("enter msg: ")
context = ssl.create_default_context()
with smtplib.SMTP(server_smtp, port) as server:
    server.ehlo()
    server.starttls(context=context)
    server.ehlo()
    server.login(userid, password)
    server.sendmail(userid, recipient, msg)
