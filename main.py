import dhooks
from dhooks import Webhook,Embed
import random
import time 
import sys
link = input("Enter webhook url : ")
title = input('Title for Image sending : ')
print("[+] Trying to send pfps | Made By Phantom.#7777")

def randnum(fname):
	lines=open(fname).read().splitlines()
	return random.choice(lines)

def send_hook():
    while True:
        try:
            embed = Embed(title = title,description = "",color = 00000)
            embed.set_image(url = randnum("scraped.txt"))
            hook = Webhook(link)
            hook.send(embed=embed)
            time.sleep(3)
        except:
            print('scraped text file is empty or not found!! use https://github.com/Envy2222/discord-pfp-scrapper-python to scrap pfps !')
            sys.exit(0)
        

send_hook()










