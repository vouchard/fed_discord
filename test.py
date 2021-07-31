from fed_module import *
import datetime
import os
import boto3
from botocore.exceptions import ClientError
from boto3.dynamodb.conditions import Key
import pytest
import asyncpraw
from aiohttp import ClientSession
import asyncio
from asyncio.proactor_events import _ProactorBasePipeTransport
from functools import wraps

def silence_event_loop_closed(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        try:
            return func(self, *args, **kwargs)
        except RuntimeError as e:
            if str(e) != 'Event loop is closed':
                raise
    return wrapper

_ProactorBasePipeTransport.__del__ = silence_event_loop_closed(_ProactorBasePipeTransport.__del__)

aws_access_key_id = os.environ['AWS_ACCESS_KEY_ID']
aws_secret_access_key = os.environ['AWS_SECRET_ACCESS_KEY']

s3 = boto3.resource('s3',
         aws_access_key_id=aws_access_key_id,
         aws_secret_access_key= aws_secret_access_key)

#print(rp.add_response_on_word('1234', 'test', 'test_responsse2', 'vou'))
#print(rp.read_data_on_database('1234', 'test'))

def test_dynamo_write():
    test = dynamo()
    content = {
        'id':'12345678'
    }
    return test.add_data('id_logs', content)
def test_dynamo_read():
    test = dynamo()
    return test.read_data('id_logs', '12345678')

#assert test_dynamo_write() == 200
#assert test_dynamo_read() == '12345678'

#url = "https://www.reddit.com/r/funny/comments/3g1jfi/buttons/"
#submission = reddit.reddit.submission(url=url)
#print(submission)
async def get_top_today():
    reddit = class_reddit()
    url =  await reddit.get_top_today('gifs')
    await reddit.reddit.close()
    return url



print(asyncio.run(get_top_today()))