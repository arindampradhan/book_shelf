from flask import Flask, render_template,request,flash


app = Flask(__name__)

@app.route('/')
def home():
  return render_template('index.html')

@app.route('/book')
def about():
  return render_template('book.html')

  