from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def helloWorld():
  return render_template('index.html')

@app.route('/blog')
def blog():
  return 'this is my blog'

@app.route('/blog/2020/dogs')
def blog2():
  return 'this is my dog'