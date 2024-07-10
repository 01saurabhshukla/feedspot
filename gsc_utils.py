import json
import os
import googleapiclient.discovery


from config import API_SERVICE_NAME, API_VERSION
from json_to_csv import JSON_to_CSV


def get_search_console_service(credentials):
    try:
        return googleapiclient.discovery.build(API_SERVICE_NAME, API_VERSION, credentials=credentials)
    except Exception as e:
        print(f"Error creating search console service: {e}")
        return None

def fetch_data(credentials, website, start_date, end_date):
    search_console_service = get_search_console_service(credentials)
    if not search_console_service:
        return None
    
    startRow = 0
    all_responses = []

    while (startRow == 0) or (startRow % 25000 == 0):
        request_body = {
            "startDate": start_date,
            "endDate": end_date,
            "dimensions": ['query', 'page', 'country'],
            "rowLimit": 25000,
            "dataState": "all",
            'startRow': startRow
        }

        try:
            response_data = search_console_service.searchanalytics().query(siteUrl=website, body=request_body).execute()
            startRow += len(response_data.get('rows', []))
            print("fetched up to " + str(startRow) + " rows of data")
            all_responses.extend(response_data.get('rows', []))
        except Exception as e:
            print(f"Error fetching data: {e}")
            break

    return all_responses

def save_to_json(data, start_date, end_date):
    try:
        # Modify the file path to include start_date and end_date
        
        new_file_path = f"Dataset_JSON/{start_date}_to_{end_date}.json"

        # Ensure the Dataset_JSON directory exists
        os.makedirs(os.path.dirname(new_file_path), exist_ok=True)
        
        with open(new_file_path, 'w') as f:
            json.dump(data, f, indent=4)
        print(f"Data saved to {new_file_path}")

        JSON_to_CSV(new_file_path)

        
    except Exception as e:
        print(f"Error saving data to JSON: {e}")

