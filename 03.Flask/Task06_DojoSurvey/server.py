from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route("/")
def form():
    return render_template("form.html")

@app.route('/results', methods=['POST'])
def result():
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    comment =  request.form['comment']
    return render_template('results.html', Name = name, Location = location, Language = language, Comment = comment)

app.run(debug=True)