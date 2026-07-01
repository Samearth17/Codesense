def validate_user(event, context):
 valid_fields = ["name", "age", "city"]
 valid_values = ["John Smith", 29, "New York"]
 
 event_body = event.get("body")
 if not event_body:
 return {
 "statusCode": 400, 
 "body": "Invalid data"
 }
 
 for key, value in event_body.items():
 if key not in valid_fields:
 return {
 "statusCode": 400, 
 "body": f"Invalid field {key}"
 }
 if value not in valid_values:
 return {
 "statusCode": 400, 
 "body": f"Invalid value for field {key}"
 }
 
 return {
 "statusCode": 200,
 "body": "User has valid configuration"
 }