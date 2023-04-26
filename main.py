import os
import time  
from featureflags.evaluations.auth_target import Target  
from featureflags.client import CfClient  
from featureflags.util import log  
from featureflags.config import with_base_url  
from featureflags.config import with_events_url  

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
    ff_delay, ff_customer_type = evaluate_ff()
    
    if ff_delay == 'True':
        # increase response time for verification purposes 
        time.sleep(1000)
   
    response = {
        'revision': revision,
        'message': message,
        'ff_delay_enabled': ff_delay,
        'ff_customer_type': ff_customer_type
    }

    # Set CORS headers for the main request
    headers = {
        'Access-Control-Allow-Origin': '*'
    }

    return (response, 200, headers)


def evaluate_ff():
    api_key = os.environ.get('GCF_FF_KEY')  
    client = CfClient(api_key,  
                      with_base_url("https://config.ff.harness.io/api/1.0"),  
                      with_events_url("https://events.ff.harness.io/api/1.0"))  
  
    target = Target(identifier='GCF_Api_Guest') 
    delay = client.bool_variation('GCF_API_Delay', target, False)  
    ff_customer_type = client.string_variation('GCF_API_CustomerType', target, "No Color")
    
    return ff_delay, ff_customer_type
