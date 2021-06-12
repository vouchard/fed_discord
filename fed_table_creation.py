import boto3

database = boto3.resource('dynamodb',region_name='ap-southeast-1' )
table = database.create_table(
    TableName='Auto_response',
    KeySchema=[
        {
            'AttributeName': 'Server_ID',
            'KeyType': 'HASH'  # Partition key
        },
        {
            'AttributeName': 'Word',
            'KeyType': 'RANGE'  # Sort key
        }

    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'Server_ID',
            'AttributeType': 'S'  
        },
        {
            'AttributeName': 'Word',
            'AttributeType': 'S'
        }
        
    ],
        ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)
