import json
import boto3
from boto3.dynamodb.conditions import Key

def lambda_handler(event, context):
    """Sample pure Lambda function
    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format
        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format
    context: object, required
        Lambda Context runtime methods and attributes
        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html
    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict
        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """
    # dynamoDBの接続
    # dynamoDb = boto3.client('dynamodb',
    #         aws_access_key_id='accessKeyId',
    #         aws_secret_access_key='secretAccessKey',
    #         region_name='us-west-2'
    # )
    dynamodb = boto3.resource('dynamodb', endpoint_url="http://host.docker.internal:30002")
    table = dynamodb.Table('Movies')
    response = table.query(
        KeyConditionExpression=Key('year').eq(1994)
    )
    print(response)
    response = {"hello": "world"}
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps(response)
    }

def lambda_handler2(event, context):
    dynamodb = boto3.resource('dynamodb', endpoint_url="http://host.docker.internal:30002")
    table = dynamodb.Table('Movies')
    response = table.query(
        KeyConditionExpression=Key('year').eq(2011)
    )
    print(response)
    response = {"hello2": "world"}
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps(response)
    }

