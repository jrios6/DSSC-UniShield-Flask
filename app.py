from flask import (Flask, render_template, redirect,
                   url_for, request, make_response)
from insurance_policies_data import RECOMMENDED_POLICIES, RECOMMENDED_POLICIES1, CURRENT_POLICIES, CURRENT_POLICIES1

app = Flask(__name__)



@app.route('/')
def home():
    return render_template('profile.html',
        n_status=["active", "", "", ""])

@app.route('/start')
def start():
    return render_template('start.html')

@app.route('/profile')
def profile():
    return render_template('profile.html',
        n_status=["active", "", "", ""])

@app.route('/buypolicies')
def buypolicies():
    return render_template('buypolicies.html',
        recommended_items=RECOMMENDED_POLICIES,
        recommended_items1=RECOMMENDED_POLICIES1,
        n_status=["", "", "active", ""])

@app.route('/mypolicies')
def mypolicies():
    return render_template('mypolicies.html',
        current_policies=CURRENT_POLICIES,
        current_policies1=CURRENT_POLICIES1,
        n_status=["", "active", "", ""])

@app.route('/bot')
def bot():
    return render_template('bot.html')

if __name__ == "__main__":
    app.run(debug=True, port=3000, host='0.0.0.0')
