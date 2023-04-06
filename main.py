import os

def hello_world(request):
    canary = os.environ.get('CANARY')
    if canary == 'true':
        message = 'Hello canary!'
    else:
        message = 'Hello stable!'
    return message
