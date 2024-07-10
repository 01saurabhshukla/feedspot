from flask import Flask, render_template, request, redirect, url_for
import os
from auth import authenticate, load_client_secrets
from gsc_utils import fetch_data, save_to_json
from config import CLIENT_SECRETS_FILE, WEBSITE




app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fetch-data', methods=['POST'])
def fetch_data_route():
    start_date = request.form['start_date']
    end_date = request.form['end_date']

    client_secret = load_client_secrets(CLIENT_SECRETS_FILE)
    if not client_secret:
        return "Client secret not loaded. Exiting."

    credentials = authenticate()
    if not credentials:
        return "Authentication failed. Exiting."

    data = fetch_data(credentials, WEBSITE, start_date, end_date)
    if not data:
        return "No data fetched. Exiting."

    save_to_json(data, start_date, end_date)
    return f"Data fetched and saved from {start_date} to {end_date}"


if __name__ == '__main__':
    app.run(debug=True)
