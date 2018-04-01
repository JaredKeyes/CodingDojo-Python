from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def Welcome():
  return render_template('welcome.html')

@app.route('/success')
def success():
  return render_template('success.html')


def hello_world():
    return 'Hello World!'
app.run(debug=True)