import json
import boto3
import uuid
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("Messages")  # change to your DynamoDB table name


def lambda_handler(event, context):
    method = event.get("httpMethod", "")

    if method == "OPTIONS":
        return build_response(200, {"message": "CORS preflight OK"})

    elif method == "POST":
        body = json.loads(event.get("body", "{}"))
        message = body.get("message", "")

        if not message:
            return build_response(400, {"error": "Message is required"})

        message_id = str(uuid.uuid4())
        table.put_item(Item={"id": message_id, "message": message})

        return build_response(200, {
            "message": "Message saved!",
            "id": message_id
        })

    elif method == "GET":
        # fetch latest message (assuming 'id' is your partition key)
        response = table.scan(Limit=1)  # quick demo, not production-efficient
        items = response.get("Items", [])

        if not items:
            return build_response(200, {"latest_message": None})

        return build_response(200, {"latest_message": items[-1]})

    else:
        return build_response(400, {"error": "Unsupported method"})


def build_response(status_code, body):
    return {
        "statusCode": status_code,
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Headers": "Content-Type",
            "Access-Control-Allow-Methods": "OPTIONS,POST,GET"
        },
        "body": json.dumps(body)
    }
