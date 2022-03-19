import os
import time
from pushbullet import Pushbullet
import configparser
from tkinter import Tk
from tkinter.filedialog import askdirectory
 

config = configparser.ConfigParser()
config.read('poe.cfg')
fileName = ''


def write():
    with open('poe.cfg', 'w') as configfile:
        config.write(configfile)

if os.path.exists('./poe.cfg') == False:
    config['poe'] = {'api': '', 'location': ''}
    write()

if os.path.isfile('./Client.txt') == False and os.path.isfile(config['poe']['location']) == False:
    print('Could not find PoE files. Please select your PoE folder')
    os.system("PAUSE")
    fileName = askdirectory(title='Select  ...\Grinding Gear Games\Path of Exile ') + '/logs/Client.txt'
    print(f"Selected | {fileName}")
    config['poe']['location'] = fileName
else: fileName = config['poe']['location']



originalTime = os.path.getmtime(fileName)
api_key = ''

if not config['poe']['api']:
    print("How to find api key instructions step by step: \n")
    print("Please input yours API key here:")
    while not api_key:
        api_key = input()
    print("Thank you!\n")
    config['poe']['api'] = api_key
    write()

api_key = config['poe']['api']
pb = Pushbullet(api_key)
time.sleep(1)
os.system("CLS")
print("\tThis product isn't affiliated with or endorsed by Grinding Gear Games in any way.\n")
print(f'Your API key: {api_key[0:15]+12*"*"+api_key[-6:]}')
print(f'Your game folder: {fileName[:-16]}')
print(f"\nIf u want to change something please check the poe.cfg file or delete it.")
print("\n\n( Running )")

while(True):
    if(os.path.getmtime(fileName) > originalTime):
        with open(fileName, 'r') as f:
            msg = f.readlines()[-1]
            if "@From" in msg:
                msg = msg[msg.find("@From"):]
                push = pb.push_note("POE | New message received!", msg)
                print(f"Push sent!\t{msg}")
        originalTime = os.path.getmtime(fileName)
    time.sleep(0.1)
    
    
    
    


    



