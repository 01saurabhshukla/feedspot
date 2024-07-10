## Steps to Follow

1. **Start the Server**

2. **Enter the Start and End Date**

3. **Wait for the CSV File**

4. **Configure the SQL Connection**
   ```plaintext
   Open sql_connection file and at the top enter the name of the CSV generated. Follow as given below:
   
   # -------------- Enter the file name -------------
   <!-- file_name = '2024-06-01_to_2024-06-30.json.csv' -->
   ```

5. **Database Configuration (Optional)**
   ```plaintext
   Make sure you have a database named 'feedspot' and this is the configuration:
   
   host='localhost',      # XAMPP runs on localhost
   user='root',           # Default user for XAMPP MySQL
   password='',           # Default password is an empty string
   database='feedspot'
   ```

6. **Execute the SQL Connection File**
   ```plaintext
   Once you are sure with the configurations, execute the sql_connection file
   ```

7. **Enter the Name of the Month**
   ```plaintext
   Enter the name of the month in the given format "february" (no space and only lowercase letters are allowed)
   ```

8. **Wait for Completion**
   ```plaintext
   Wait until it shows:

   <!-- print('-- Data insertion in DataBase is Succesful --') -->
   ```

9. **Task Completion**
   ```plaintext
   The task of extracting data from Google Search Console, converting it to CSV, and inserting it into the DB is now done.
   ```

## Optional Steps

- **Delete Specific Rows in DB**
  ```sql
  DELETE FROM Table_Name
  WHERE url LIKE '%#%' OR url LIKE '%@%' OR url LIKE '%?%';
  ```

  At `Table_Name`, place your table name.

