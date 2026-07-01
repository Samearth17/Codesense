import json

CloudFormationTemplate = {
  "AWSTemplateFormatVersion": "2010-09-09",
  "Resources": {
    "MySNSTopic": {
      "Type": "AWS::SNS::Topic",
      "Properties": {
        "TopicName": "MySNSTopic"
      }
    }
  }
}

print(json.dumps(CloudFormationTemplate))