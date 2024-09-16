from flask import Flask, request, jsonify
import threading
from sheets_sync1 import sync_sheets_to_db, sync_db_to_sheets, clear_and_fill_database
from threading import Lock

app = Flask(__name__)

# Lock for synchronizing threads
sync_lock = Lock()

@app.route('/sync_sheets_to_db', methods=['POST'])
def manual_sync_sheets_to_db():
    """Trigger syncing Google Sheets data to the database."""
    try:
        # Acquire the lock to ensure thread safety
        with sync_lock:
            threading.Thread(target=sync_sheets_to_db).start()
        return jsonify({"status": "success", "message": "Google Sheets data syncing to database started."}), 200
    except Exception as e:
        # Log error and return an error response
        print(f"Error in manual_sync_sheets_to_db: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/sync_db_to_sheets', methods=['POST'])
def manual_sync_db_to_sheets():
    """Trigger syncing database data to Google Sheets."""
    try:
        # Acquire the lock to ensure thread safety
        with sync_lock:
            threading.Thread(target=sync_db_to_sheets).start()
        return jsonify({"status": "success", "message": "Database data syncing to Google Sheets started."}), 200
    except Exception as e:
        # Log error and return an error response
        print(f"Error in manual_sync_db_to_sheets: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/clear_and_fill_database', methods=['POST'])
def clear_and_fill_db():
    """Trigger clearing and filling the database with provided data."""
    try:
        # Get the JSON data from the request
        data = request.get_json()

        if not data or not isinstance(data, list):
            raise ValueError("Invalid JSON data format. Expected a list of dictionaries.")
        
        # Acquire the lock to ensure thread safety
        with sync_lock:
            threading.Thread(target=clear_and_fill_database, args=(data,)).start()
        
        return jsonify({"status": "success", "message": "Database clearing and filling started."}), 200
    except Exception as e:
        # Log error and return an error response
        print(f"Error in clear_and_fill_db: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
