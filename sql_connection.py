import pandas as pd
import mysql.connector
import json


# -------------- Enter the file name -------------
file_name = '2024-06-01_to_2024-06-30.json.csv'



# Load the CSV data
input_csv_path = f"Dataset_CSV/{file_name}"
df = pd.read_csv(input_csv_path)

# Prompt the user to enter the month
month = input("Enter the month for the data:->")

# Add the month column to the dataframe
df['month'] = month

# Connect to the MySQL database on XAMPP
conn = mysql.connector.connect(
    host='localhost',      # XAMPP runs on localhost
    user='root',           # Default user for XAMPP MySQL
    password='',           # Default password is an empty string
    database='feedspot' # Name of the database you created
)
cursor = conn.cursor()

# Insert data into the MySQL table
insert_query = """
INSERT INTO podcast_gsc_raw_data (`month`,url,clicks,impressions,query,country,ctr,position)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
ON DUPLICATE KEY UPDATE
url = VALUES(url),
clicks = VALUES(clicks),
impressions = VALUES(impressions),
ctr = VALUES(ctr),
position = VALUES(position),
query = VALUES(query),
country = VALUES(country),
`month` = VALUES(`month`)
"""

for index, row in df.iterrows():
    cursor.execute(insert_query, (
        row['month'],
        row['url'],
        row['clicks'],
        row['impressions'],
        row['query'],
        row['country'],
        row['ctr'],
        row['position']
    ))

# Commit the transaction
conn.commit()

print('-- Data insertion in DataBase is Succesful --')

# Close the cursor and connection
cursor.close()
conn.close()


