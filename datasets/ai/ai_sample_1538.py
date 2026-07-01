import json

def lambda_handler(event, context):
 # Get the operation and operands from the event
 operation = event['operation']
 operands = event['operands']
 
 # Perform the operation
 if operation == 'add':
 result = sum(operands)
 elif operation == 'subtract':
 result = operands[0] - operands[1]
 elif operation == 'multiply':
 result = operands[0] * operands[1]
 elif operation == 'divide':
 result = operands[0] / operands[1]
 else:
 return {
 'statusCode': 500,
 'body': json.dumps('Unsupported operation')
 }
 
 # Return the response
 return {
 'statusCode': 200,
 'body': json.dumps(result)
 }