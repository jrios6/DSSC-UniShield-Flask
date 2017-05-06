from flask import (Flask, render_template, redirect,
                   url_for, request, make_response)
from insurance_policies_data import POLICIES

app = Flask(__name__)


@app.route('/')
def start():
    return render_template('start.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/buypolicies')
def buypolicies():
    return render_template('buypolicies.html',
        recommended_items=POLICIES)

@app.route('/mypolicies')
def mypolicies():
    return render_template('mypolicies.html')

@app.route('/bot')
def bot():
    return render_template('bot.html')


if __name__ == "__main__":
    app.run(debug=True, port=3000, host='0.0.0.0')
