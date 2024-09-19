# app.py
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('indexa.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        # You could process the contact form data here (e.g., send email, store in DB)
        return f'Thank you, {name}. We will contact you at {email}.'
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)

