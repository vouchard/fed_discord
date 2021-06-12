import discord #discord.py
from fed_module import *
import datetime
import os
from discord.ext import commands

rp = dynamo_comms()
print(rp.add_response_on_word('1234', 'test', 'test_responsse2', 'vou'))