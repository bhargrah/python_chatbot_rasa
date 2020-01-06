from flask import Response
from flask import Flask, render_template, request, redirect, url_for, send_from_directory,jsonify
from rasa_nlu.model import Metadata, Interpreter
import json

app = Flask(__name__)      

@app.route('/')
def index():
    return render_template('index.html')
    
interpreter = Interpreter.load('./models/current/restaurant_nlu')
@app.route('/nlu_parsing', methods=['POST'])
def transform():
    if request.headers['Content-Type'] == 'application/json':     
        query = request.json.get("utterance")
        results=interpreter.parse(query)
        js = json.dumps(results)
        resp = Response(js, status=200, mimetype='application/json')
        return resp

        
if __name__ == '__main__':
    app.run(debug=True)


### POST Request
# http://127.0.0.1:5000/nlu_parsing

# Body --->  {"utterance" : "find me some chinese restaurants"}