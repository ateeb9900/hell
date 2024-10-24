from flask import Flask, request, render_template
import requests

app = Flask(__name__)

# Replace with your bot token and chat ID
BOT_TOKEN = '7909315658:AAF1SWaP7HXdTAEOqRQf71qfQCfGCfkXVsg'  # Paste the bot token you got from BotFather
CHAT_ID = '7913910795'  # Paste your chat ID here

@app.route('/')
def index():
    return render_template('form.html')  # Create a simple HTML form

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    game_id = request.form['game_id']

    # Format the message you want to send to Telegram
    message = f"New Free Fire Tournament Registration:\n\nName: {name}\nEmail: {email}\nGame ID: {game_id}"

    # Send the message to Telegram using their API
    telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    params = {
        'chat_id': CHAT_ID,
        'text': message
    }
    response = requests.get(telegram_url, params=params)

    if response.status_code == 200:
        return "Form submitted successfully!"
    else:
        return "Failed to send the message."

if __name__ == '__main__':
    app.run(debug=True)
