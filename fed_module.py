import boto3
from botocore.exceptions import ClientError
from boto3.dynamodb.conditions import Key
import datetime
import asyncpraw
import asyncio
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
    async def get_top_today(self,subreddit):
        sub =  await self.reddit.subreddit(subreddit)
        submissions = sub.top(time_filter = 'day',limit = 1)
        
        async for submission in submissions:
#            return submission.url
            ret = []
            ret = [*ret,(submission.url)]
            ret = [*ret,(submission.title)]
           #print(submission.url)
            #print(submission.title)
            #print(ret)
        return ret
        
class scheduled_task:
    def __init__(self,reddit_client_id,reddit_client_secret):
        self.current_hour = (datetime.datetime.now()).hour
        self.reddit_client_id = reddit_client_id
        self.reddit_client_secret = reddit_client_secret
    async def get_url(self):
        reddit = class_reddit(self.reddit_client_id,self.reddit_client_secret)
        if int(self.current_hour) == 15:
            url = await reddit.get_top_today('food')

        if int(self.current_hour) == 16:
            url = await reddit.get_top_today('aww')
        
        if int(self.current_hour) == 17:
            url = await reddit.get_top_today('Showerthoughts')
            
        if int(self.current_hour) == 18:
            url = await reddit.get_top_today('holdmybeer')
            
        if int(self.current_hour) == 19:
            url = await reddit.get_top_today('wholesomememes')
            
        if int(self.current_hour) == 20:
            url = await reddit.get_top_today('dankmemes')
            
        if int(self.current_hour) == 21:
            url = await reddit.get_top_today('memes')
            
        if int(self.current_hour) == 22:
            url = await reddit.get_top_today('nonononoyes')
            
        if int(self.current_hour) == 14:
            url = await reddit.get_top_today('PerfectTiming')
        await reddit.reddit.close()
        return url   

    