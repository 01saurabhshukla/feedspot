import google.oauth2.credentials
import google_auth_oauthlib.flow
from google_auth_oauthlib.flow import InstalledAppFlow
import json

from config import CLIENT_SECRETS_FILE, SCOPES

def load_client_secrets(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except Exception as e:
        print(f"Error loading client secrets: {e}")
        return None

def authenticate():
    try:
        # flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(CLIENT_SECRETS_FILE, scopes=SCOPES)
        flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, scopes=SCOPES)
        flow.run_local_server(port=0)
        credentials = flow.credentials
        return credentials
    except Exception as e:
        print(f"Error during authentication: {e}")
        return None
