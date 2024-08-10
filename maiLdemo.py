import os.path
import base64
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

# Define the SCOPES
SCOPES = ['https://mail.google.com/']


def print_email_info(msg):
    # Get the subject and sender
    subject = ''
    sender = ''
    for header in msg['payload']['headers']:
        if header['name'].lower() == 'subject':
            subject = header['value']
        elif header['name'].lower() == 'from':
            sender = header['value']
        
        # Break the loop if we've found both subject and sender
        if subject and sender:
            break
    print(f"Subject: {subject}")
    print(f"From: {sender}")
    print()


def build_service():
    creds = None
    # Load credentials from file
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
    return service

def main():
    
    service =  build_service()
    X = 3

    # Query to find emails to delete
    query = "in:inbox"
    
    # Get the list of emails
    results = service.users().messages().list(userId='me', q=query, maxResults=X).execute()
    messages = results.get('messages', [])

    if not messages:
        print("No messages found.")
        return

    # Delete the emails
    for message in messages:  # Loop through the list of emails
        try:
            
            msg = service.users().messages().get(userId='me', id=message['id'], format='full').execute()
        
            print('Deleting email...')
            print_email_info(msg)
            service.users().messages().delete(userId='me', id=message['id']).execute()
        except Exception as e:
            print(f"An error occurred: {e}")
       # print(f" message ID: {message['id']}")

if __name__ == '__main__':
    main()
