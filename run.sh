#!/bin/bash
cd /home/ec2-user/credentials
DISCORD_KEY=$(cat DISCORD_KEY.env)
cd /home/ec2-user/fed_discord
source environment/bin/activate
sudo chmod +x fed_main.py
./fed_main.py $DISCORD_KEY

