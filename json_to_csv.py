import os
import pandas as pd
import json

def get_data(url_of_folder):
    with open(url_of_folder, 'r') as file:
        data = json.load(file)

    # Extract data into lists
    df = pd.DataFrame({
        'query': [item['keys'][0] for item in data],
        'url': [item['keys'][1] for item in data],
        'country': [item['keys'][2] for item in data],
        'clicks': [item['clicks'] for item in data],
        'impressions': [item['impressions'] for item in data],
        'ctr': [item['ctr'] for item in data],
        'position': [item['position'] for item in data]
    })

    return df

# comment this all until we get our df 
def JSON_to_CSV(url_of_folder):

    print(url_of_folder)
    
    filtered_df = get_data(url_of_folder)

    # Sort the filtered DataFrame in ascending order based on the 'impressions' column
    filtered_df_sorted = filtered_df.sort_values(by='impressions', ascending=True)

    # Display the filtered and sorted DataFrame
    print(filtered_df_sorted)

    name = url_of_folder.split('/')
    csv_file_path = name[1]

    # Ensure the Dataset_CSV directory exists
    csv_dir = 'Dataset_CSV'
    os.makedirs(csv_dir, exist_ok=True)

    base_name = os.path.basename(csv_file_path).replace('.json', '')

    # to convert to csv from json 
    filtered_df_sorted.to_csv(f"{csv_dir}/{base_name}.csv", index=False)



# JSON_to_CSV('Dataset_JSON/2024-06-01_to_2024-06-30.json')
    

    

