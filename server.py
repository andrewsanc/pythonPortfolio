from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def helloWorld():
  return render_template('index.html')

@app.route('/about')
def about():
  return 'About me!'

@app.route('/blog')
def blog():
  return 'My Blog!'