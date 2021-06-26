#!/usr/bin/env python3
import discord #discord.py
from fed_module import *
import datetime
import os
import platform
from discord.ext import commands
import sys

if platform.system() == 'Windows':
    discord_token = os.environ['DISCORD_KEY']
else:
    f = open('/home/ec2-user/credentials/DISCORD_KEY.env','r')
    discord_token = (f.read())
    f.close()
        
    
client = commands.Bot(command_prefix = 'fd.')
client.remove_command('help')

database = dynamo_comms()
rp = dynamo_comms()
@client.event
async def on_ready():
    print ("bot is ready")

#--------------------RESPONSES-----------------------------------
@client.command()
async def addResponse(ctx,qfiltered_word,response):
    server = str(ctx.message.guild.id)
    filtered_word = qfiltered_word.upper()
    author = ctx.message.author.name
    rp.add_response_on_word(server, qfiltered_word, response, author)
    await ctx.send('Response added')

@client.command()
async def viewResponse(ctx,qword):
    server = ctx.message.guild.id
    await ctx.send(rp.viewResponse(qword,server))

@client.command()
async def removeResponse(ctx,rid):
    rp.removeResponse(rid)
    await ctx.send('Response removed')



@client.event
async def on_message(message):
    if message.author == client.user:
        return
    #print(message.guild)
    if message.guild == None:
        channel = client.get_channel(802779161852772373)
        await channel.send(message.content)


    
    await client.process_commands(message)

print('waiting for client.run. . . ')
client.run(discord_token)

