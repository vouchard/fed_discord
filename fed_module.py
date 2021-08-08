import boto3
from botocore.exceptions import ClientError
from boto3.dynamodb.conditions import Key
import datetime
import asyncpraw
import asyncio
import requests
import discord
class dynamo:
    def __init__(self):
        self.dynamodb = boto3.resource('dynamodb',region_name='ap-southeast-1' )
    
    def add_data(self,table_name,content):
        table = self.dynamodb.Table(table_name)
        item = content
        response = table.put_item(
            Item = item
        )
        return response['ResponseMetadata']['HTTPStatusCode']


    def read_data(self,table_name,partition_key):
        table = self.dynamodb.Table(table_name)
        response = table.query(
                KeyConditionExpression=Key('id').eq(partition_key)
            )
        return response['Items'][0]['id']
class class_reddit:
    def __init__(self,client_id,client_secret):
        self.reddit = asyncpraw.Reddit(
        client_id=client_id,
        client_secret=client_secret,
        user_agent="testscript by vou",
        username="weAreNextInLine",
    )
    async def get_top_today(self,subreddit,ndx):
        sub =  await self.reddit.subreddit(subreddit)
        submissions = sub.top(time_filter = 'day',limit = 3)
        ctr = 0

        async for submission in submissions:
            if ctr == ndx:
                return [(submission.url),(submission.title)]
            else:
                ret = None
            ctr += 1
           #print(submission.url)
            #print(submission.title)
            #print(ret   


class scheduled_task:
    def __init__(self,reddit_client_id,reddit_client_secret):
        self.reddit_client_id = reddit_client_id
        self.reddit_client_secret = reddit_client_secret
    async def get_url(self):
        current_hour = today = (datetime.datetime.utcnow() + datetime.timedelta(hours=8)).hour
        reddit = class_reddit(self.reddit_client_id,self.reddit_client_secret)

        #780072679193051168       -MEMEREVIEW
        #802779161852772373       -MAIN

        if int(current_hour) == 6:
            url = await reddit.get_top_today('food',0)
            url = [*url,802779161852772373]

        elif int(current_hour) == 1:
            url = await reddit.get_top_today('wholesomememes',0)
            url = [*url,780072679193051168]

        elif int(current_hour) == 2:
            url = await reddit.get_top_today('aww',0)
            url = [*url,802779161852772373]

        elif int(current_hour) == 3:
            #url = await reddit.get_top_today('holdmybeer',0)
            url = ['','kung ano man ang dahilan bakit puyat ka, kailangan lang yan ng pahinga, umaga na matulog ka na!',802779161852772373]

        elif int(current_hour) == 4:
            url = await reddit.get_top_today('dankmemes',0)
            url = [*url,780072679193051168]

        elif int(current_hour) == 5:
            url = await reddit.get_top_today('memes',0)
            url = [*url,780072679193051168]

        elif int(current_hour) == 6:
            url = await reddit.get_top_today('nonononoyes',0)
            url = [*url,780072679193051168]

        elif int(current_hour) == 7:
            url = await reddit.get_top_today('technicallythetruth',0)
            url = [*url,780072679193051168]

        elif int(current_hour) == 8:
            url = await reddit.get_top_today('Showerthoughts',0)
            url = [*url,802779161852772373]

        #780072679193051168       -MEMEREVIEW
        #802779161852772373       -MAIN

        elif int(current_hour) == 9:
            url = await reddit.get_top_today('aww',1)
            url = [*url,802779161852772373]

        elif int(current_hour) == 10:
            url = await reddit.get_top_today('Showerthoughts',1)
            url = [*url,802779161852772373]

        elif int(current_hour) == 11:
            #url = await reddit.get_top_today('holdmybeer',0)
            url = ['','lunch ka na lods <3',802779161852772373]

        elif int(current_hour) == 12:
            url = await reddit.get_top_today('wholesomememes',1)
            url = [*url,780072679193051168]

        elif int(current_hour) == 13:
            url = await reddit.get_top_today('dankmemes',1)
            url = [*url,780072679193051168]

        elif int(current_hour) == 14:
            url = await reddit.get_top_today('memes',1)
            url = [*url,780072679193051168]

        elif int(current_hour) == 15:
            url = await reddit.get_top_today('nonononoyes',1)
            url = [*url,780072679193051168]

        elif int(current_hour) == 16:
            url = await reddit.get_top_today('technicallythetruth',1)
            url = [*url,780072679193051168]

        elif int(current_hour) == 17:
            url = await reddit.get_top_today('aww',2)
            url = [*url,802779161852772373]

        elif int(current_hour) == 18:
            url = await reddit.get_top_today('Showerthoughts',2)
            url = [*url,802779161852772373]

        elif int(current_hour) == 19:
            #url = await reddit.get_top_today('holdmybeer',0)
            url = ['','ginagawa nyo?',802779161852772373]

        elif int(current_hour) == 20:
            url = await reddit.get_top_today('wholesomememes',2)
            url = [*url,780072679193051168]

        elif int(current_hour) == 21:
            url = await reddit.get_top_today('dankmemes',2)
            url = [*url,780072679193051168]

        elif int(current_hour) == 22:
            url = await reddit.get_top_today('memes',2)
            url = [*url,780072679193051168]

        elif int(current_hour) == 23:
            url = await reddit.get_top_today('nonononoyes',2)
            url = [*url,780072679193051168]

        elif int(current_hour) == 0:
            url = await reddit.get_top_today('technicallythetruth',2)
            url = [*url,780072679193051168]
        else:
            url = None
        await reddit.reddit.close()
        return url   

    