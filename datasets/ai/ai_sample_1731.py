import json
import boto3
 
def lambda_handler(event, context):
  # Create an SNS Client
  sns_client = boto3.client('sns')
  
  # Send a message to the SNS topic
  topic_arn = 'arn:aws:sns:eu-west-1:123456789012:my-topic'
  message = 'This is a test message'
  response = sns_client.publish(
    TopicArn = topic_arn,
    Message = message
  )
  return {
    'statusCode': 200,
    'body': json.dumps(response)
  }