from fed_module import *
import datetime
import os
import boto3
from botocore.exceptions import ClientError
from boto3.dynamodb.conditions import Key



aws_access_key_id = os.environ['AWS_ACCESS_KEY_ID']
aws_secret_access_key = os.environ['AWS_SECRET_ACCESS_KEY']

s3 = boto3.resource('s3',
         aws_access_key_id=aws_access_key_id,
         aws_secret_access_key= aws_secret_access_key)

rp = dynamo_comms()
#print(rp.add_response_on_word('1234', 'test', 'test_responsse2', 'vou'))
print(rp.read_data_on_database('1234', 'test'))