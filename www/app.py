# Imports
from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
from database import Database

app = Flask(__name__)
db = Database()

@app.route('/config')
def leo_config():
    f= request.args.get('frec')
    if not f:
        return 15
    else:
        return render_template('config.html',frec = f)
@app.route('/config', methods = [ 'POST'])
def escribo_config():
    f= request.args.get('frec')
    if not f:
        return render_template('index.html',frec=15)
    else:
        return render_template('index.html',frec = f)

@app.route('/', methods = ['GET'])
def start_sampling():
    data = db.start_sampling()
    return render_template('index.html',samples=data)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8888)

