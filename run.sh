#!/bin/bash
cd /home/ec2-user/fed_discord
sudo pkill screen
sudo chmod +x fed_main.py
screen -d -m -S fed_bot  ./fed_main.py




