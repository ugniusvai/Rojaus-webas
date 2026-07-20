from flask import Flask, render_template

app = Flask(__name__, template_folder='../templates', static_folder='../public', static_url_path='/')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/catalog')
def catalog():
    return render_template('catalog.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

# Vercel serverless function entrypoint
# Vercel passes the request to the `app` instance.
