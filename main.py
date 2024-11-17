import os
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
import pickle

# Define the scope
SCOPES = ['https://www.googleapis.com/auth/photoslibrary']

def authenticate():
    creds = None
    # Load credentials if available
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If no credentials, log in and save them
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('photosOAuth.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    return creds

def list_photos(service):
    results = service.mediaItems().list(pageSize=10).execute()
    items = results.get('mediaItems', [])
    for item in items:
        print(item['filename'], item['mediaMetadata'])

if __name__ == "__main__":
    creds = authenticate()
    service = build('photoslibrary', 'v1', credentials=creds)
    list_photos(service)
