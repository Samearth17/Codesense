import json
from twilio.rest import Client

def lambda_handler(event, context):
    account_sid = event['AccountSID']
    auth_token = event['AuthToken']
    from_number = event['FromNumber']
    to_number = event['ToNumber']
    message_body = event['MessageBody']

    client = Client(account_sid, auth_token)
    client.messages.create(
        body=message_body,
        from_=from_number,
        to=to_number
    )

    return json.dumps({
        "message": "Successfully sent sms"
    })