import json

print('Loading function')

def lambda_handler(event, context):
    print('Received event: ' + json.dumps(event,indent=2))
    if 'events' in event:
        name = event['events'][0]['type']
    else:
        name = 'world'
    greetings = 'Hello ' + name + '!'
    print(greetings)
    
    return greetings
