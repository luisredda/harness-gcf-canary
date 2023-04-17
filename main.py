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

    revision = os.environ.get('K_REVISION')
    message = 'Hello Harness!'
    response = {
        'revision': revision,
        'message': message
    }

    # Set CORS headers for the main request
    headers = {
        'Access-Control-Allow-Origin': '*'
    }

    return (response, 200, headers)
