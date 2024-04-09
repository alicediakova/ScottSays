from flask import Flask, request, redirect, render_template, url_for, flash
import json

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
        # flash('Quote updated successfully!', 'success')

        return redirect(url_for('home'))
    else:
        flash('Incorrect Scott-code. Please try again.', 'error')

        return redirect(url_for('edit'))
    


@app.route('/')
def home():
    # Read the current quote from 'quote.json'
    try:
        with open('quote.json', 'r') as file:
            quote_data = json.load(file)
            current_quote = quote_data.get("quote", "No quote today.")  # Provide a default in case the file is empty
    except FileNotFoundError:
        current_quote = "No quote today."  # Default message if 'quote.json' does not exist

    # Render 'home.html' with the current quote
    return render_template('home.html', quote=current_quote)

@app.route('/edit')
def edit():
    return render_template('edit.html')

if __name__ == "__main__":
    app.run(debug=True)