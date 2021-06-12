import boto3
from botocore.exceptions import ClientError
from boto3.dynamodb.conditions import Key
import datetime


class dynamo_comms:
    def __init__(self):
        self.dynamodb = boto3.resource('dynamodb',region_name='ap-southeast-1' )
        self.response_table = 'Auto_response'    
        self.question_table = 'random_questions'    
    
    def add_data_to_response(self,server_id,statement,answers,added_by):
        add_on = datetime.datetime.now()
        added_on = add_on.strftime("%m/%d/%Y, %H:%M:%S")
        table = self.dynamodb.Table(self.response_table)
        statement = statement.upper()
        item_to_add = table.put_item(
            Item={
                'Server_ID' : server_id,
                'Word': statement,
                'Info':[{                   
                    'Response':answers,
                    'Added_on':added_on,
                    'Added_by':added_by
                }]


            }
        )
        return item_to_add
    def read_data_on_database(self,server_id,statement):
        table = self.dynamodb.Table(self.response_table)
        response = table.query(
                KeyConditionExpression=Key('Server_ID').eq(server_id) & Key('Word').eq(statement)
            )
        return response['Items']
        

    
    def add_response_on_word(self,server_id,statement,answers,added_by):
        table = self.dynamodb.Table(self.response_table)
        add_on = datetime.datetime.now()
        added_on = add_on.strftime("%m/%d/%Y, %H:%M:%S")
        statement = statement.upper()
        response = table.query(
                KeyConditionExpression=
                Key('Server_ID').eq(server_id) & Key('Word').eq(statement)
            )
        if response['Items'] == []:
            self.add_data_to_response(server_id, statement, answers, added_by)
            print('response added successfully')
        else:
            data = self.read_data_on_database(server_id, statement)
            to_add = {'Response':answers,'Added_on':added_on,'Added_by':added_by}
            current_info = ((data[0])['Info'])
            current_answers = [x['Response'] for x in current_info]
            current_info.append(to_add)
            if answers not in current_answers:
                response = table.update_item(
                Key={
                    'Server_ID': server_id,
                    'Word': statement
                },
                UpdateExpression="set Info=:newinfo",
                ExpressionAttributeValues={
                    ':newinfo': current_info
                })
                print('Appended successfully')
                print(current_answers)
            else:
                print('Answer to respose Already Exist')
                print(current_answers)
    

