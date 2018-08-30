# Imports
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/config')
def config():
    return render_template('config.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8888)

