import json
import boto3

def send_email(event, context):
 recipient = event['recipient']
 subject = event['subject']
 message = event['message']

 #send email here

 client = boto3.client('ses')

 response = client.send_email(
 Source='sender@example.com',
 Destination={
   'ToAddresses': [recipient,],
   },
 Message={
   'Subject': {'Data': subject},
   'Body': {'Text': {'Data': message}},
   },
 )

def handler(event, context):
 event = json.loads(event)
 response = send_email(event, context)
 return json.dumps(response)