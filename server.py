from flask import Flask, request, redirect, render_template, url_for, flash
import json
from datetime import datetime

app = Flask(__name__)

# This secret key is necessary for session management and flash messaging
app.secret_key = 'golions_'

@app.route('/update-quote', methods=['POST'])
def update_quote():
    scott_code = request.form['scottCode']
    new_quote = request.form['newQuote']
    correct_password = 'golions_'  # Replace with the actual password

    if scott_code == correct_password:
        # Assuming the quote is stored in a file named 'quote.json'
        with open('quote.json', 'w') as file:
            json.dump({"quote": new_quote}, file)

        return redirect(url_for('home'))
    else:
        flash('Incorrect Scott-code. Please try again.', 'error')

        return redirect(url_for('edit'))



@app.route('/', methods=['GET'])
def home():
    # Load the quote from 'quote.json'
    try:
        with open('quote.json', 'r') as file:
            quote_data = json.load(file)
            quote = quote_data.get('quote', '')
    except FileNotFoundError:
        quote = ''

    # Render the home page with the quote
    return render_template('index.html', quote=quote)



@app.route('/edit')
def edit():
    return render_template('edit.html')


if __name__ == "__main__":
    app.run(debug=True)