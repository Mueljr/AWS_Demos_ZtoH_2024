import json
import boto3
import os

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['TABLE_NAME'])  # Environment variable: TABLE_NAME

def lambda_handler(event, context):
    http_method = event.get("httpMethod")

    if http_method == "POST":
        # Parse request body
        body = json.loads(event.get("body", "{}"))
        message = body.get("message", "No message provided")

        # Always include the partition key
        item = {
            "id": "latest",        # Required key
            "message": message
        }

        table.put_item(Item=item)

        return {
            "statusCode": 200,
            "body": json.dumps({"status": "saved", "message": message})
        }

    elif http_method == "GET":
        response = table.get_item(Key={"id": "latest"})
        item = response.get("Item", {})

        return {
            "statusCode": 200,
            "body": json.dumps(item)
        }

    else:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "Unsupported method"})
        }