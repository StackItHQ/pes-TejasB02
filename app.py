from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# Database connection
def connect_to_db():
    return mysql.connector.connect(
        # Use your own database
        # I have created a database called student to store the studens' names, email and phone number
        host="your-db-host", 
        user="your-db-username",
        password="your-db-password",
        database="your-db-name"
    )

@app.route('/update_db', methods=['POST'])
def update_db():
    data = request.json
    # Process data (assumed as JSON sent from Google Sheets)
    sheet_data = data.get('sheet_data')

    # Example: Insert into the database
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO your_table (column1, column2) VALUES (%s, %s)", (sheet_data['col1'], sheet_data['col2']))
    conn.commit()

    return jsonify({"status": "success"}), 200

if __name__ == '__main__':
    app.run(debug=True)
