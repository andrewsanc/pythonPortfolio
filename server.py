from flask import Flask, render_template, request, redirect
import csv
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
  if request.method == 'POST':
    data = request.form.to_dict()
    writeToCSV(data)
    return redirect('/thankyou.html')
  else:
    return 'Something went wrong'

def writeToFile(data):
  with open('database.txt', mode="a") as database:
    email, subject, message = data['email'], data['subject'], data['message']
    file = database.write(f'\n{email}, {subject}, {message}')

def writeToCSV(data):
  with open('database.csv', mode="a") as database2:
    email, subject, message = data['email'], data['subject'], data['message']
    csvWriter = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csvWriter.writerow([{email}, {subject}, {message}])