import os
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# If modifying these SCOPES, delete the file token.json
SCOPES = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']

def authenticate_google_sheets():
    creds = None
    token_path = 'token.json'  # Path to store the token
    credentials_path = 'auth/client_secret_765098273427-ldd03ksfn0fa3bdnaq7e5mb4fe3knra4.apps.googleusercontent.com.json'  # Updated path to your credentials.json

    # Check if token.json exists and load stored credentials
    if os.path.exists(token_path):
        try:
            creds = Credentials.from_authorized_user_file(token_path, SCOPES)
        except Exception as e:
            print(f"Error loading token.json: {e}")

    # If there are no valid credentials or they're expired, re-authenticate
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            try:
                creds.refresh(Request())
            except Exception as e:
                print(f"Error refreshing credentials: {e}")
        else:
            if not os.path.exists(credentials_path):
                raise FileNotFoundError(f"Credentials file not found: {credentials_path}")
            
            # Run OAuth flow and get new credentials
            flow = InstalledAppFlow.from_client_secrets_file(credentials_path, SCOPES)
            creds = flow.run_local_server(port=0)

        # Save the new credentials for future use
        try:
            with open(token_path, 'w') as token:
                token.write(creds.to_json())
        except Exception as e:
            print(f"Error saving token.json: {e}")

    # Build the Google Sheets service
    try:
        service = build('sheets', 'v4', credentials=creds)
    except Exception as e:
        print(f"Error creating Google Sheets service: {e}")
        return None

    return service
