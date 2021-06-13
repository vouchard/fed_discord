#!/bin/bash
sudo pip3 install virtualenv
cd /home/ec2-user/fed_discord
virtualenv environment
source environment/bin/activate
python3 -m pip install discord.py
python3 -m pip install pip install boto3
