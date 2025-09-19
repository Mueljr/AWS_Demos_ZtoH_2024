import json
import boto3
import uuid
import time

dynamodb = boto3.resource("dynamodb")
import os

table_name = os.environ['TABLE_NAME']
table = dynamodb.Table(table_name)

def lambda_handler(event, context):
    method = event.get("httpMethod", "")

    # CORS preflight
    if method == "OPTIONS":
        return build_response(200, {"message": "CORS preflight OK"})

    # POST a new message
    elif method == "POST":
        body = json.loads(event.get("body", "{}"))
        message = body.get("message", "")

        if not message:
            return build_response(400, {"error": "Message is required"})

        message_id = str(uuid.uuid4())
        timestamp = int(time.time())

        table.put_item(Item={
            "id": message_id,
            "createdAt": timestamp,
            "message": message
        })

        return build_response(200, {
            "message": "Message saved!",
            "id": message_id
        })

    # GET latest message
    elif method == "GET":
        # Query messages sorted by timestamp descending
        response = table.scan()  # For small tables, scan works. For large tables, use GSI.
        items = response.get("Items", [])

        if not items:
            return build_response(200, {"latest_message": None})

        # Find the item with the max timestamp
        latest_item = max(items, key=lambda x: x["createdAt"])

        return build_response(200, {"latest_message": latest_item})

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