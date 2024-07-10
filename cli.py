import argparse
from auth import authenticate, load_client_secrets
from gsc_utils import fetch_data, save_to_json
from config import CLIENT_SECRETS_FILE, WEBSITE

def main():
    parser = argparse.ArgumentParser(description='Fetch Google Search Console data.')
    # parser.add_argument('--website', type=str, required=True, help='Website URL to fetch data for')
    parser.add_argument('--start-date', type=str, required=True, help='Start date in YYYY-MM-DD format')
    parser.add_argument('--end-date', type=str, required=True, help='End date in YYYY-MM-DD format')
    # parser.add_argument('--output', type=str, required=True, help='Output JSON file path')
    args = parser.parse_args()

    client_secret = load_client_secrets(CLIENT_SECRETS_FILE)
    if not client_secret:
        print("Client secret not loaded. Exiting.")
        return

    credentials = authenticate()
    if not credentials:
        print("Authentication failed. Exiting.")
        return
    
    

    data = fetch_data(credentials, WEBSITE, args.start_date, args.end_date)
    if not data:
        print("No data fetched. Exiting.")
        return

    save_to_json(data, args.start_date, args.end_date)



if __name__ == '__main__':
    main()
