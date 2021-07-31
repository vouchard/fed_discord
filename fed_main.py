#!/usr/bin/env python3
import discord #discord.py
from fed_module import *
import datetime
import os
import platform
from discord.ext import commands
from discord.ext import tasks #doing task in evey x hour/sec/min
import io #needed in dicord for uploading imgs
import aiohttp #needed in dicord for uploading imgs
import sys
import random
from urllib.parse import urlparse #pars URL



intents = discord.Intents().all()

if platform.system() == 'Windows':
    discord_token = os.environ['DISCORD_KEY']
    reddit_client_secret = os.environ['REDDIT_CLIENT_SECRET']
    reddit_client_id = os.environ['REDDIT_CLIENT_ID']
else:
    f = open('/home/ec2-user/credentials/DISCORD_KEY.env','r')
    discord_token = (f.read())
    f.close()

    f = open('/home/ec2-user/credentials/REDDIT_CLIENT_SECRET.env','r')
    reddit_client_secret = (f.read())
    f.close()

    f = open('/home/ec2-user/credentials/REDDIT_CLIENT_ID.env','r')
    reddit_client_id = (f.read())
    f.close()




        

client = commands.Bot(command_prefix = 'fd.',intents = intents)
client.remove_command('help')



#reddit = class_reddit(reddit_client_id,reddit_client_secret)
sched = scheduled_task(reddit_client_id,reddit_client_secret)
# database = dynamo_comms()
# rp = dynamo_comms()
@client.event
async def on_ready():
    print ("bot is ready")
    myLoop.start()

@tasks.loop(seconds = 3605) # repeat after every 10 seconds
async def myLoop():
    channel = client.get_channel(803989637558304781)
    current_hour = (datetime.datetime.now()).hour
    url = ''
    #try:
    url = await sched.get_url()
    if url != None:
        embed=discord.Embed(title=url[1])
        embed.set_image(url=url[0])
        #await ctx.send(embed=embed)
        await channel.send(embed=embed)
    #except:
        #print('Unable to connect to reddit')


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    #print(message.guild)
    if message.guild == None:
        channel = client.get_channel(802779161852772373)
        await channel.send(message.content)

    if 'fed sino' in message.content:
        members = message.channel.members
        max_members = len(members)
        #print(guild_members)
        member = members[random.randint(0, max_members - 1)]
        while member.bot:
            member = members[random.randint(0, max_members - 1)]
        if member.nick == None:
            msg = f"si {member.name}"
        else:
            msg = f"si {member.nick}"    
        
        await message.reply(msg)
    
    if 'ay ma' in message.content:
        fl = open('ma_db.tmp','r')
        wrds = [w for w in fl]
        tosend = wrds[random.randint(0, len(wrds) - 1)]
        fl.close()

        if 'si voo ay ma' in message.content:
            tosend = 'si voo? my daddy?'

        await message.reply(tosend)

    if 'sino si Este' in message.content:
        await message.reply('ang magandang dilag ng solar')

    future = datetime.datetime(2022,6,30,12,0,0)
    today = datetime.datetime.utcnow() + datetime.timedelta(hours=8)
    my_time = future - today
    my_time = my_time.days
    time_message = f"| {my_time} days na lang at papalitan na si duterte"
    await client.change_presence(activity=discord.Game(name=time_message))
    await client.process_commands(message)




print('waiting for client.run. . . ')
client.run(discord_token)

