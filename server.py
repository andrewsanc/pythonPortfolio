from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
  return render_template('index.html')

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/works')
def works():
  return render_template('works.html')

@app.route('/work')
def work():
  return render_template('work.html')  

@app.route('/contact')
def contact():
  return render_template('contact.html') 

@app.route('/components')
def components():
  return render_template('components.html')

@app.route('/<string:pageName>')
def htmlPage(pageName):
  return render_template(pageName)

@app.route('/blog')
def blog():
  return 'My Blog!'

@app.route('/submitForm', methods=['POST', 'GET'])
def submitForm():
  return 'form submitted hoooorayyy'