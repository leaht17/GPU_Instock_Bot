#Scratch work, ignore
#*******************

from abc import ABC, ABCMeta, abstractmethod

#Scraping Module Abstraction
class Notifier(ABC):

    #Sends an email to every email in the list
    #Param: EmailList - list of strings '...@....com/net/etc'
    @abstractmethod
    def sendEmail(EmailList):
        pass

    #Sends a text to every phone number in the list
    #Param: PhoneNumList - list of strings with length 10
    @abstractmethod
    def sendText(PhoneNumList):
        pass

class EmailSender(ABC):
    @abstractmethod
    def __init__(self):
        pass

    #message - string used for message
    @abstractmethod
    def create_message(self, sender, to, subject, message_text):
        pass

    #frm - string of from sender
    #to - recipient email
    #msg - msg created from create_message()
    #subj - subject title
    @abstractmethod
    def send_message(self, message):
        pass

from __future__ import print_function
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

class GmailSender(EmailSender, metaclass=ABCMeta):

    def __init__(self):
        """ basic usage of the Gmail API.
        """
        SCOPES = ['https://www.googleapis.com/auth/gmail.send']
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
                    'client_secret.json', SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.json', 'w') as token:
                token.write(creds.to_json())
        service = build('gmail', 'v1', credentials=creds)
        print('hi')

    #Encode in base64url strings
    def create_message(self, sender, to, subject, message_text):
      """Create a message for an email.

      Args:
        sender: Email address of the sender.
        to: Email address of the receiver.
        subject: The subject of the email message.
        message_text: The text of the email message.

      Returns:
        An object containing a base64url encoded email object.
      """
      message = MIMEText(message_text)
      message['to'] = to
      message['from'] = sender
      message['subject'] = subject
      return {'raw': base64.urlsafe_b64encode(message.as_string().encode()).decode()}

    def send_message(self, message):
      """Send an email message.

      Args:
        service: Authorized Gmail API service instance.
        user_id: User's email address. The special value "me"
        can be used to indicate the authenticated user.
        message: Message to be sent.

      Returns:
        Sent Message.
      """
      try:
        message = (service.users().messages().send(userId='me', body=message).execute())
        msgID = 'Message Id: %s' % message['id']
        print(msgID)
        return message
      except errors.HttpError or error:
        print('An error occurred: %s' % error)

msg = create_message("gpuinstockbot@gmail.com", "gpuinstockbot@gmail.com", "Test", "Hello")
send_message(service, 'me', msg)

emails = GmailSender()



# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/gmail.send']

def main():
    """ basic usage of the Gmail API.
    """
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
                'client_secret.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('gmail', 'v1', credentials=creds)




#if __name__ == '__main__':
#    main()
