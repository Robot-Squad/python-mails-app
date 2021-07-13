from __future__ import print_function
import os.path
from re import sub
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from email.mime.text import MIMEText
import base64
import googleapiclient.errors as errors
SCOPES = ['https://mail.google.com/']



creds = None
# The file token.json stores the user's access and refresh tokens, and is
# created automatically when the authorization flow completes for the first
# time.
if os.path.exists('token.json'):
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)
# If there are no (valid) credentials available, let the user log in.
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open('token.json', 'w') as token:
        token.write(creds.to_json())

service = build('gmail', 'v1', credentials=creds)

# Call the Gmail API
def createmail(to, subject, fro, body):
    msg = MIMEText(body)
    msg["subject"] = subject
    msg["to"] = to
    msg["from"] = fro
    return {'raw': base64.urlsafe_b64encode(msg.as_string().encode()).decode()}
def sendmail(service, rawmail):
    try:
        message = (service.users().messages().send(userId='me', body=rawmail)
               .execute())
        print(message['id'])
        return message
    except errors.HttpError as err:
        print(err)
to = input("to: ")
fro = input("from: ")
subject = input("subject: ")
body = input("mailtext: ")
raw_mail = createmail(to, subject, fro, body)
sendmail(service, raw_mail)