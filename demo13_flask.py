from flask import Flask
from flask import render_template

app = Flask(__name__, template_folder='template')

@app.route('/index')
def mes():
    return "<h1>Welcome to my site</h1>"

@app.route('/contactUs')
def Contact():
    return "You can contact us on our site"

@app.route('/<name>')
def username(name):
    return "Good afternoon "+name

@app.route('/myfirst')
def des():
    return render_template('myfirst.html')

if (__name__)==('__main__'):
    app.run()
