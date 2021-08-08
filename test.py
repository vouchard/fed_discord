from fed_module import *
import datetime
import os
import platform
import boto3
from botocore.exceptions import ClientError
from boto3.dynamodb.conditions import Key
import pytest
import asyncpraw
from aiohttp import ClientSession
import asyncio
from asyncio.proactor_events import _ProactorBasePipeTransport
from functools import wraps
from genshin_module import *


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


if platform.system() == 'Windows':
    discord_token = os.environ['DISCORD_KEY']
    reddit_client_secret = os.environ['REDDIT_CLIENT_SECRET']
    reddit_client_id = os.environ['REDDIT_CLIENT_ID']
else:
    f = open('/home/ec2-user/credentials/DISCORD_KEY.env','r')
    discord_token = (f.read())
    f.close()

    f = open('/home/ec2-user/credentials/REDDIT_CLIENT_SECRET.env','r')
    reddit_client_secret = (f.read()).strip()
    f.close()

    f = open('/home/ec2-user/credentials/REDDIT_CLIENT_ID.env','r')
    reddit_client_id = (f.read()).strip()
    f.close()














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
    reddit = class_reddit(reddit_client_id,reddit_client_secret)
    url =  await reddit.get_top_today('Showerthoughts',2)
    await reddit.reddit.close()
    return url



#print(asyncio.run(get_top_today()))
genshin = genshin('solar-pearl')
def test_genshin():
    return genshin.get_info()

def test_genshin_help():
    return genshin.gi_help(kw='weapons')
print(test_genshin_help())