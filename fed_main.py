#!/usr/bin/env python3

import discord #discord.py
from fed_module import *
import datetime
import os
from discord.ext import commands
###DISCORD
discord_token = os.environ['DISCORD_KEY']

client = commands.Bot(command_prefix = 'fd.')
client.remove_command('help')

database = dynamo_comms()
rp = dynamo_comms()

