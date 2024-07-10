
**Step 01** : Start the server
**Step 02** : Enter the start and end date 
**step 03** : Wait until CSV is received 
**step 04** : open sql_connection file and at the top enter the name of csv generated. follow as given below

# -------------- Enter the file name -------------
<!-- file_name = '2024-06-01_to_2024-06-30.json.csv'   -->

**step 05** : Make sure you have database name feedspot and this is the configuration (optional) 

    host='localhost',      # XAMPP runs on localhost
    user='root',           # Default user for XAMPP MySQL
    password='',           # Default password is an empty string
    database='feedspot' 

**step 06** : Once we are sure with the configurations we can now execute the sql_connection file 
**step 07** : enter the name of the month in the given format "february" no space and only small letters are allowed
**step 08** : wait until it shows

<!-- print('-- Data insertion in DataBase is Succesful --') -->

**step 09** : Now the task of extracting data from google search console and converting to csv and inserting it into the DB is done 

some optional steps
In DB 
delete all rows where permalinks have #|@|? using this query

DELETE FROM Table_Name
WHERE url LIKE '%#%' OR url LIKE '%@%' OR url LIKE '%?%';

at Table_Name place your table name.
