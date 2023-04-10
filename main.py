import os

def hello_world(request):
    
     headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
        'Access-Control-Allow-Headers': 'Content-Type'
    }
    
    if request.method == 'OPTIONS':
        # Handle CORS preflight request
        return ('', 204, headers)
    
    canary = os.environ.get('CANARY')
    if canary == 'true':
        message = 'Hello canary!'
    else:
        message = 'Hello stable!'
    return message
