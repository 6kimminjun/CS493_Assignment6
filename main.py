from google.cloud import datastore
from flask import Flask, request, render_template
import json2html
import json
import Oauth2

app = Flask(__name__)
app.register_blueprint(Oauth2.bp)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)