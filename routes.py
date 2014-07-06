from flask import Flask, render_template,request,flash
from glob import iglob
from os.path import basename

app = Flask(__name__)

@app.route('/')
def home():
  return render_template('index.html')

@app.route('/')
def list_images():
	pngs = iglob('hold/temp/*.png')
	pngs = (basename(png) for pnk in  pngs	)
	return render_template('list_images.html',pngs=pngs)
	
@app.route('/book')
def about():
  return render_template('book.html')

