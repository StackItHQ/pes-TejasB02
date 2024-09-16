import threading
import time
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
import os
import mysql.connector
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

def authenticate_google_sheets():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        flow = InstalledAppFlow.from_client_secrets_file(
            r'auth\client_secret_765098273427-ldd03ksfn0fa3bdnaq7e5mb4fe3knra4.apps.googleusercontent.com.json', SCOPES)
        creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    service = build('sheets', 'v4', credentials=creds)
    return service

def connect_to_db():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="560095",
            database="student_info"
        )
        return conn
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def fetch_sheet_data():
    service = authenticate_google_sheets()
    spreadsheet_id = '16gOodXlX96_IVp0AhfNSPX1d0hNE2FzzHf3Zw5lQD40'
    range_name = 'Sheet1!A2:D'
    result = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range=range_name).execute()
    data = result.get('values', [])
    
    # Filter out rows with any empty fields
    full_rows = [row for row in data if len(row) == 4 and all(field.strip() for field in row)]
    return full_rows

def fetch_mysql_data():
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("SELECT id, first_name, last_name, email, phone_number FROM students")
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return data

def validate_row(row):
    return len(row) == 4 and all(field.strip() for field in row)

def insert_into_db(student_data):
    conn = connect_to_db()
    if conn is None:
        print("Database connection failed.")
        return
    
    cursor = conn.cursor()
    query = "INSERT INTO students (first_name, last_name, email, phone_number) VALUES (%s, %s, %s, %s)"
    
    try:
        cursor.executemany(query, student_data)
        conn.commit()
        print(f"{cursor.rowcount} rows inserted successfully.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        conn.close()

def update_row_in_db(row):
    conn = connect_to_db()
    if conn is None:
        print("Database connection failed.")
        return
    
    cursor = conn.cursor()
    update_query = "UPDATE students SET first_name = %s, last_name = %s, email = %s, phone_number = %s WHERE email = %s"
    
    try:
        cursor.execute(update_query, (row[0], row[1], row[2], row[3], row[2]))
        conn.commit()
        print(f"Row with email {row[2]} updated successfully.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        conn.close()

def update_sheet_from_db():
    try:
        service = authenticate_google_sheets()
        spreadsheet_id = '16gOodXlX96_IVp0AhfNSPX1d0hNE2FzzHf3Zw5lQD40'
        range_name = 'Sheet1!A2:D'
        
        mysql_data = fetch_mysql_data()
        values = [list(row[1:]) for row in mysql_data]  # Exclude 'id' from the values

        existing_sheet_data = fetch_sheet_data()
        if existing_sheet_data != values:
            # Clear the sheet before updating
            service.spreadsheets().values().clear(spreadsheetId=spreadsheet_id, range=range_name).execute()

            body = {'values': values}
            service.spreadsheets().values().update(
                spreadsheetId=spreadsheet_id, 
                range=range_name, 
                valueInputOption="RAW", 
                body=body
            ).execute()
            print("Google Sheets successfully updated from the database.")
        else:
            print("No changes detected in the database; Google Sheets not updated.")
    except Exception as e:
        print(f"Error in update_sheet_from_db: {e}")

def sync_sheets_to_db():
    try:
        print("Syncing Google Sheets to Database...")
        sheet_data = fetch_sheet_data()
        mysql_data = fetch_mysql_data()

        # Convert data for easier comparison
        sheet_data_dict = {tuple(row): row for row in sheet_data}
        mysql_data_dict = {tuple(row[1:]): row for row in mysql_data}

        # Identify additions and updates
        to_insert = []
        to_update = []
        for row in sheet_data_dict:
            if row not in mysql_data_dict:
                to_insert.append(sheet_data_dict[row])
            elif sheet_data_dict[row] != mysql_data_dict[row][1:]:
                # If the row exists but the data is different, it means the row should be updated
                to_update.append(sheet_data_dict[row])

        # Identify deletions
        to_delete = [row for row in mysql_data_dict if row not in sheet_data_dict]

        conn = connect_to_db()
        if conn is None:
            print("Database connection failed.")
            return

        cursor = conn.cursor()
        
        # Insert new data
        if to_insert:
            insert_into_db(to_insert)
        
        # Update existing data
        if to_update:
            for row in to_update:
                update_row_in_db(row)

        # Delete removed data
        delete_query = "DELETE FROM students WHERE email = %s"
        if to_delete:
            cursor.executemany(delete_query, [(row[2],) for row in to_delete])
            conn.commit()
            print(f"{cursor.rowcount} rows deleted successfully.")

        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Error during sync_sheets_to_db: {e}")

def sync_db_to_sheets():
    update_sheet_from_db()

def real_time_sync():
    while True:
        sync_sheets_to_db()
        sync_db_to_sheets()
        time.sleep(10)  # Sync every 10 seconds (adjust as necessary)

if __name__ == '__main__':
    sync_thread = threading.Thread(target=real_time_sync)
    sync_thread.start()
