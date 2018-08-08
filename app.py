from flask import Flask, render_template
app = Flask(__name__)

DEBUG = True
HOST = '0.0.0.0'
PORT = '8080'



@app.route('/')
@app.route('/index')
@app.route('/index.html')
@app.route('/portfolio')
def portfolio():
	return render_template('portfolio.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/contact')
def contact():
	return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=DEBUG, host=HOST, port=PORT)
