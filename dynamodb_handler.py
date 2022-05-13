import boto3
import os


AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')


client = boto3.client(
    'dynamodb',
    aws_access_key_id = AWS_ACCESS_KEY_ID,
    aws_secret_access_key = AWS_SECRET_ACCESS_KEY,
)

resource = boto3.resource(
    'dynamodb',
    aws_access_key_id = AWS_ACCESS_KEY_ID,
    aws_secret_access_key = AWS_SECRET_ACCESS_KEY,
)

def create_table():

    client.create_table(
        AttributeDefinitions=[
                        {
                            'AttributeName': 'search_term',
                            'AttributeType': 'S',
                        }
                    ],
                    KeySchema=[
                        {
                            'AttributeName': 'search_term',
                            'KeyType': 'HASH',
                        }
                    ],
                    ProvisionedThroughput={
                        'ReadCapacityUnits': 5,
                        'WriteCapacityUnits': 5,
                    },
                    TableName='top_ten_songs',
    )

def set_item(search_term, item_data):

    table = resource.Table('top_ten_songs')

    try:
        response = table.update_item(
            Key={
                'search_term': search_term
            },
            UpdateExpression="set artist_data=:s",
            ExpressionAttributeValues={
                ":s": item_data
            }
        )

        return response
    except Exception as err:
        print(err)

        return None
