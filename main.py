import os
from flask import Flask, make_response
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET', 'OPTIONS'])
def hello_world():
    if request.method == 'OPTIONS':
        # Handle CORS preflight request
        response = make_response('', 204)
    else:
        canary = os.environ.get('CANARY')
        if canary == 'true':
            message = 'Hello canary!'
        else:
            message = 'Hello stable!'
        response = make_response(message)
    
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    
    return response
