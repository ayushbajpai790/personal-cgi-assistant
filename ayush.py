#!/usr/bin/python3
print("content-type:text/html")
print()
import cgi
import subprocess
import datetime
hour=datetime.datetime.now().hour
if hour>=0 and hour<12:
        print("Hello,Good Morning")
elif hour>=12 and hour<16:
        print("Hello,Good Afternoon")
elif hour>=16 and hour<20:
        print("Hello,Good Evening")
else :
        print("Hello,Good night")
print()
y=cgi.FieldStorage()
p=y.getvalue("form")
if ("what can you do"in p):
        print("I am your personal, virtual assistant ,I can do simple tasks like open a program for you,open a website for you,shutdown your computer,clean your screen ,can tell which files are stored in your current folder,predict time and tell top headlines for times of india newspaper and much more ")
        print("so let's start what task i can perform for you first ,If you get bored simply text exit or quit")
elif(("open"in p) or ("launch" in p )or("start"in p) or"run" in p or "execute"in p)and("chrome"in p or "web browser"in p or "browser"in p):
        
        print("loading sir....")
        subprocess.getoutput(p)
elif(("open"in p) or ("launch" in p )or("start"in p) or"run" in p or "execute"in p)and("notepad"in p or "text editor"in p):
        print("loading sir....")
        subprocess.getoutput("gedit")
