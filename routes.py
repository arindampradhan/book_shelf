from flask import Flask, render_template
from glob import iglob
from os.path import basename

app = Flask(__name__)


books = iglob('hold/*')
preview = iglob('hold/*/1.jpg')
pngs = (basename(png) for png in  pngs	)


@app.route('/')
def home():
  return render_template('index.html')

@app.route('/')
def list_images():
	return render_template('list_images.html',books=books)
	
@app.route('/book')
def about():
  return render_template('book.html',pngs=pngs)

if __name__ == "__main__":
	app.run(debug=True)
