import boto3

def lambda_handler(event, context):
    phone_number = event["Phone Number"]
    message = event["Message"]

    # Create an SNS client
    sns = boto3.client("sns")

    # Publish a simple message to the specified SNS topic
    response = sns.publish(
        PhoneNumber=phone_number,
        Message=message
    )

    # Response
    return {
        'statusCode': 200,
        'body': response
    }