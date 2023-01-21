import pyttsx3
import speech_recognition as sr
import webbrowser
from pywikihow import search_wikihow
from bs4 import BeautifulSoup
import pywhatkit
import wikipedia
from googletrans import Translator
import os
import subprocess as sp
import pyautogui
import psutil
from tkinter import Label
from tkinter import Entry
from tkinter import Button
import requests
import time as t
from tkinter import Tk
from gtts import gTTS
from tkinter import StringVar
import PyPDF2
from pytube import YouTube
import datetime
from playsound import playsound
import keyboard as kb
import pyjokes

Assistant = pyttsx3.init('sapi5')
voices = Assistant.getProperty('voices')
print(voices)
Assistant.setProperty('voices', voices[1].id)

def Speak(audio):
    print("  ")
    Assistant.say(audio)
    print(f"[+] {audio}")
    print("   ")
    Assistant.runAndWait()

def screenshot():
       Speak("Ok Boss, What Should I Name That File ?")
       path = takecommand()
       path1name = path + ".png"
       path1 = "C:\\Users\\abc\\Desktop\\Grafics_python"+ path1name
       kk = pyautogui.screenshot()
       kk.save(path1) 

def takecommand():
    command = sr.Recognizer()
    with sr.Microphone() as source:
           print("listening")
           command.pause_threshold = 1
           audio = command.listen(source)

           try:
                  print("Recognizing .....")
                  query = command.recognize_google(audio,language='en-in')
                  print(f"[+] You Said : {query}")

           except Exception as Error:
                  return "none"

           return query.lower()

def Music():
       Speak("Tell Me the Name of The Song !")
       musicName = takecommand()
       if 'under influence' in musicName:
              os.startfile('C:\\Users\\abc\\Music\\Under Influence.mp3')

       else:
              pywhatkit.playonyt(musicName)
              Speak("Your Song Has Been Send To Youtube")

def OpenApps():
       Speak("OK Sir, Wait A Second!")
       
       if 'VS code' in query:
              os.startfile("E:\\Microsoft VS Code\\Code.exe")

       elif 'telegram' in query:
              os.startfile("D:\\Telegram Desktop\\Telegram.exe")

       elif 'spotify' in query:
              os.startfile("C:\\Users\\abc\\Desktop\\Grafics_python\\New folder\spotify-1-1-99-878.exe")


       elif 'code' in query:
              os.startfile("E:\\Applications\\Microsoft VS Code\\Microsoft VS Code\\Code.exe")

       elif 'chrome' in query:
              os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")

       elif 'instagram' in query:
              webbrowser.open('https://www.instagram.com/')

       elif 'maps' in query:
              webbrowser.open('https://www.google.com/maps/@28.7091225,77.2749958,15z')

       elif 'youtube' in query:
              webbrowser.open('https://www.youtube.com')
       Speak("Your Command Has Been Succesfully Opened")

def CloseApps():
       Speak("OK Sir, Wait A Second")



       if 'youtube' in query:
            os.system("TASKKILL /F /im Chrome.exe")

       elif 'chrome' in query:
            os.system("TASKKILL /f /im Chrome.exe")

       elif 'telegram' in query:
            os.system("TASKKILL /F /im Telegram.exe")

       elif 'code' in query:
            os.system("TASKKILL /F /im code.exe")

       elif 'VS code' in query:
            os.system("TASKKILL /F /im code.exe")

       elif 'instagram' in query:
            os.system("TASKKILL /F /im chrome.exe")

       elif 'music' in query:
            os.system("TASKKILL /F /im groove music")
            
       Speak("Your Command Has Been Succesfully Completed!")

def Temp():
       search = "temperature in rajasthan"
       url = f"https://www.google.com/search?q={search}"
       r = requests.get(url)
       data = BeautifulSoup(r.text,"html.parser")
       temperature = data.find("div",class_ = "BNeawe").text
       Speak(f"The Temperature Outside is{temperature}")

def Reader():
       Speak("Tell Me The Name Of The Book!")

       name = takecommand()

       if 'india' in name:

            os.startfile('E:\\Hacking Learning\\india.pdf')
            book = open('E:\\Hacking Learning\\india.pdf','rb')
            pdfreader = PyPDF2.PdfReader(book)

            Speak("From Which Page I Have To Start Reading ?")
            page_number = int(input("Enter The Page Number :"))
            page = pdfreader._get_num_pages(page_number)
            text = page.extractText()
            Speak(text)

def StudyAuto():
       Speak("Study Mode Is On")
       Speak("Do You Want To Read Books Today")
       Dicision = takecommand()

       if 'yes'in Dicision:
              Speak("Well we Will Start With A Book Today")
              Reader()
       elif'no' in Dicision:
              Speak("Ok Sir, What You Want To Do Fo Today!")
              testMaker = takecommand()
              if'Take a Test' in testMaker:
                     Speak("Ok Sir, Of Which Subject You Want To Take A Test!")
                     test = str(input("Enter The Name Of Subject >>> "))
                     if test == 'english':
                            Speak("Wite The Name Of Chapter")
                            NameOfChapter = str(input("Enter The Name Of Chapter >>> "))
                            if NameOfChapter == 'A Dog Named Duke':
                                   Speak("Ok Sir, Searching Test For A Dog Name Duke on internet")
              elif'take a test' in testMaker:
                     Speak("Ok Sir, Of Which Subject You Want To Take A Test!")
                     test = str(input("Enter The Name Of Subject >>> "))
                     if test == 'english':
                            Speak("Write The Name Of Chapter")
                            NameOfChapter = str(input("Enter The Name Of Chapter >>> "))
                            if NameOfChapter == 'A Dog Named Duke':
                                   Speak("Ok Sir, Searching Test For A Dog Name Duke On Internet")
                            
def YoutubeAuto():
       Speak("Whats Your Command ?")
       while True:
              comm = takecommand()

              if 'pause' in comm:
                     kb.press('space bar')

              elif 'search' in comm:
                     kb.send("/")

              elif 'scrool up'in comm:
                     kb.press("up")
                     kb.press("up")
                     kb.press("up")
                     kb.press("up")
                     kb.press("up")
                     kb.press("up")
                     kb.press("up")
                     kb.press("up")
                     kb.press("up")
                     kb.press("up")
                     kb.press("up")
                     kb.press("up")
                     kb.press("up")

              elif 'scrool down' in comm:
                     kb.press("down")
                     kb.press("down")
                     kb.press("down")
                     kb.press("down")
                     kb.press("down")
                     kb.press("down")
                     kb.press("down")
                     kb.press("down")
                     kb.press("down")
                     kb.press("down")
                     kb.press("down")
                     kb.press("down")
                     kb.press("down")

              elif 'restart' in comm:
                     kb.press('0')

              elif 'mute' in comm:
                     kb.press('m')

              elif 'skip' in comm:
                     kb.press('l')

              elif 'back' in comm:
                     kb.press('j')

              elif 'full screen' in comm:
                     kb.press('f')

              elif 'film mode' in comm:
                     kb.press('t')

              elif 'search' in comm:
                     kb.send("/")

              elif'exit youtube auto' in query:
                     Speak("exiting YouTube Auto!")
                     break

def ChromeAuto():
       Speak("Chrome Automation started!")
       while True:

              command = takecommand()

              if 'close this tab' in command:
                     kb.press_and_release('ctrl + w')

              elif 'open new tab' in command:
                     kb.press_and_release('ctrl + t')

              elif 'open new window' in command:
                     kb.press_and_release('ctrl + n')

              elif 'history' in command:
                     kb.press_and_release('ctrl +h')

              elif'exit youtube auto' in query:
                     Speak("exiting YouTube Auto!")
                     break


Speak("Hello Sir, I Am Jarvis")
Speak("Your Personal AI Assistant!")
Speak("How Can I Help You ?")

while True:

       query = takecommand()

#jarvis/me intro tool start
       if 'hello' in query :
         Speak("hello sir, how can i help you ")
       elif 'How are you jarvis' in query:
              Speak("I Am Fine Sir")
              Speak("What About You Sir")
              takecommand()
              Speak("That's Great")
       elif'hey Jarvis' in query:
              Speak("yes! Sir")
       elif'hi jarvis' in query:
              Speak("Hi Sir I Am Jarvis Always There For You!")
       elif 'jarvis take a break' in query:
              Speak("ok Sir,")
              Speak("For How Much Time Should I Take Break")
              time = int(takecommand())
              t.sleep(time)
#hello tool end
#------------------------------------------------------------------------------------------
#show stored wifi tool start
       elif 'hack internet' in query :

              kb.send("windows+r")

              t.sleep(1)

              kb.write("cmd", delay=0.050)

              kb.send("enter")

              t.sleep(1)

              kb.write("netsh wlan show profile", delay=0.050)

              kb.send("enter")

              Speak("select a network in ten seconds")

              t.sleep(10)

              kb.send("alt+shift+f4")

              t.sleep(2)

              Speak("write the name of the selected wifi network, in terminal ")

              wifi = str(input("Enter the name of wifi you selected"))

              Speak("hacking, wifi in process")
              kb.send("windows+shift+down")
              kb.send("windows+shift+down")
              kb.send("windows+shift+down")
              kb.send("windows+shift+down")
              kb.send("windows+shift+down")
              kb.send("windows+shift+down")

              kb.send("windows+r")

              t.sleep(1)

              kb.write("cmd", delay=0.050)

              kb.send("enter")
              
              t.sleep(2)
              
              kb.write('netsh wlan show profile name="')
              kb.write(wifi)
              kb.write('" key=clear')

              t.sleep(2)

              kb.send("enter")

              t.sleep(2)

              kb.send("ctrl+a")

              t.sleep(1)

              kb.send("ctrl+c")

              t.sleep(0.5)

              kb.write("exit", delay=0.050)

              kb.send("enter")

              t.sleep(1)

              kb.send("windows+r")

              t.sleep(1)

              kb.write("notepad.exe", delay=0.1)

              kb.send("enter")

              t.sleep(1)

              kb.send("ctrl+v")

              kb.send("enter")

              kb.send("enter")
              
              kb.send("alt+shift+f4")

              t.sleep
               
              kb.send("enter")
              
              kb.write("wifipassword.txt")

              kb.send("enter")

              Speak("the file was, saved in documents folder.")

              Speak("just copy the key content, it is the wifi password.")
       elif 'show stored wifi' in query :

              kb.send("windows+r")

              t.sleep(1)

              kb.write("cmd", delay=0.050)

              kb.send("enter")

              t.sleep(1)

              kb.write("netsh wlan show profile", delay=0.050)

              kb.send("enter")

              Speak("select a network in ten seconds")

              t.sleep(10)

              kb.send("alt+shift+f4")

              t.sleep(2)

              Speak("write the name of the selected wifi network, in terminal ")

              wifi = str(input("Enter the name of wifi you selected"))

              Speak("hacking, wifi in process")
              kb.send("windows+shift+down")
              kb.send("windows+shift+down")
              kb.send("windows+shift+down")
              kb.send("windows+shift+down")
              kb.send("windows+shift+down")
              kb.send("windows+shift+down")

              kb.send("windows+r")

              t.sleep(1)

              kb.write("cmd", delay=0.050)

              kb.send("enter")
              
              t.sleep(2)
              
              kb.write('netsh wlan show profile name="')
              kb.write(wifi)
              kb.write('" key=clear')

              t.sleep(2)

              kb.send("enter")

              t.sleep(2)

              kb.send("ctrl+a")

              t.sleep(1)

              kb.send("ctrl+c")

              t.sleep(0.5)

              kb.write("exit", delay=0.050)

              kb.send("enter")

              t.sleep(1)

              kb.send("windows+r")

              t.sleep(1)

              kb.write("notepad.exe", delay=0.1)

              kb.send("enter")

              t.sleep(1)

              kb.send("ctrl+v")

              kb.send("enter")

              kb.send("enter")
              
              kb.send("alt+shift+f4")

              t.sleep
               
              kb.send("enter")
              
              kb.write("wifipassword.txt")

              kb.send("enter")

              Speak("the file was, saved in documents folder.")

              Speak("just copy the key content, it is the wifi password.")
#show wifi password tool end
#------------------------------------------------------------------------------------------
#music start
       elif 'open spotify' in query:
              OpenApps()
       elif 'play music' in query:
              Music() 
       elif 'music' in query:
              Music() 
       elif 'play song' in query:
              Music() 
       elif 'song' in query:
              Music() 
#music end
#------------------------------------------------------------------------------------------
#delete,write program start    
       elif 'delete a word' in query:
              kb.send("ctrl+backspace")
       elif'backspace' in query:
              kb.send("backspace")
       elif'erase all'in query:
              kb.send("ctrl+a")
              t.sleep(0.05)
              kb.send("backspace")
       elif 'likho' in query:
              Speak("What You Want To Write")
              listen = takecommand()
              t.sleep(1)
              kb.write(listen,delay=0.050)

              Speak("Pressing Backspace")
              kb.send("ctrl+backspace")
       elif 'jarvis write' in query:
              Speak("What You Want To Write")
              listen = takecommand()
              t.sleep(1)
              kb.write(listen,delay=0.050)

              Speak("Pressing Backspace")
              kb.send("ctrl+backspace")
       elif'undo' in query:
              kb.send("ctrl+z")
       elif'redu'in query:
              kb.send("ctrl+y")
       elif'space' in query:
              kb.send("spacebar")
       elif'press spacebar'in query:
              kb.send("spacebar")
       elif'press space'in query:
              kb.send("spacebar")
       elif'bracket open'in query:
              kb.send("shift+9")
       elif'bracket close'in query:
              kb.send("shift+0")
       elif'attherate'in query:
              kb.send("shift+2")
       elif'hashtag'in query:
              kb.send("shift+3")
       elif'doller'in query:
              kb.send("shift+4")
       elif'persentage'in query:
              kb.send("shift+5")
       elif'star'in query:
              kb.send("shift+8")
       elif'multiply'in query:
              kb.send("shift+8")
       elif'underscore'in query:
              kb.send("shift+-")
       elif'subtract'in query:
              kb.send("-")
       elif'minus'in query:
              kb.send("-")
       elif'add'in query:
              kb.send("shift+=")
       elif'plus'in query:
              kb.send("shift+=")
       elif'equal'in query:
              kb.send("=")
       elif'addition sign'in query:
              kb.send("shift+=")
       elif'subtraction sign'in query:
              kb.send("-")

#delete,write program end
#------------------------------------------------------------------------------------------
#open query start 
       elif 'open kali linux' in query:

              Speak("Opening Kali Linux")

              kb.send("windows+s")
              t.sleep(1)
              kb.write("kali linux")
              kb.send("enter")
       elif 'open ubuntu' in query:
              Speak("Opening Kali Linux")

              kb.send("windows+s")
              t.sleep(1)
              kb.write("ubuntu")
              kb.send("enter")              
       elif 'open telegram' in query:
              OpenApps()
       elif 'open VS code' in query:

              OpenApps()       
       elif 'open notepad' in query:
              Speak("Opening NOTEPAD ")
              t.sleep(2)
              sp.Popen("notepad.exe")
       elif 'open facebook' in query:
            OpenApps()
       elif 'open instagram' in query:
            OpenApps()
       elif 'open maps' in query:
            OpenApps()
#open query end
#------------------------------------------------------------------------------------------
#close query start
       elif 'close telegram' in query:
              CloseApps()
       elif 'close' in query:
              Speak("Closing Current Tab")

              kb.send("alt+shift+f4")
#close query end
#------------------------------------------------------------------------------------------
#how to comand start
       elif'search'in query:
              Speak("Getting Data From The internet !")
              op = query.replace("jarvis","")
              
              max_result = 1
              how_to_func = search_wikihow(op,max_result)
              assert len(how_to_func) == 1
              how_to_func[0].print()
              Speak(how_to_func[0].summary)
#how to command end
#------------------------------------------------------------------------------------------
#today's temperature start
       elif"temperature" in query:
              Temp()
       elif"today's temperature" in query:
              Temp()
#today's temperature tool end
#------------------------------------------------------------------------------------------
#youtube tool start
       elif 'youtube pause' in query:
              kb.press('spacebar')
       elif 'youtube search' in query:
              Speak("Ok sir, This is what i found for your search!")
              query = query.replace("jarvis", "")
              query = query.replace("youtube search", "")
              web = 'https://www.youtube.com/results?search_query='+query
              webbrowser.open(web)
              Speak("Done Sir")
       elif 'yutube restart' in query:
              kb.press('0')
       elif 'youtube resume' in query:
              kb.send("space")
              Speak("Done Sir.")
       elif 'youtube mute' in query:
              kb.press("m")
              Speak("Done Sir.")
       elif 'youtube skip' in query:
              kb.press('1')
              Speak("Done Sir.")
       elif 'youtube back' in query:
              kb.press('j')
              Speak("Done Sir.")
       elif 'youtube full screen' in query:
              kb.press('f')
              Speak("Done Sir.")
       elif 'youtube film mode' in query:
              kb.press("t")
              Speak("Done Sir.")
       elif'youtube scrool up' in query:
              kb.send("up")
              kb.send("up")
              kb.send("up")
              kb.send("up")
              kb.send("up")
              kb.send("up")
              kb.send("up")
              kb.send("up")
              kb.send("up")
              kb.send("up")
              kb.send("up")
              kb.send("up")
              kb.send("up")
              Speak("Done Sir.")
       elif'youtube scrool down' in query:
              kb.send("down")
              kb.send("down")
              kb.send("down")
              kb.send("down")
              kb.send("down")
              kb.send("down")
              kb.send("down")
              kb.send("down")
              kb.send("down")
              kb.send("down")
              kb.send("down")
              kb.send("down")
              kb.send("down")
              Speak("Done Sir.")
       elif'youtube click search' in query:
              kb.send("/")
              Speak("Done Sir.")
#youtube automation tool end
#------------------------------------------------------------------------------------------
#read book start
       elif 'read book' in query:
              Reader()
       elif 'read me a book' in query:
              Reader()
       elif 'read book for me' in query:
              Reader()
#read book end
#------------------------------------------------------------------------------------------
#chrome tool start
       elif 'close the tab' in query:
            kb.press_and_release('ctrl + w')
       elif 'google search' in query:
              import wikipedia as googleScrap

              query = query.replace("jarvis","")
              query = query.replace("google search","")
              query = query.replace("google","")
              Speak("This is What I Found For You Search On The Web")
              pywhatkit.search(query)
              try:
                    
                    result = googleScrap.summary(query,2)
                    Speak(result)
              
              except:
                     Speak("No Speakable Data Available")
       elif 'launch a web page' in query:


              Speak("Tell Me the name of The Website!")
              name = takecommand()
              web = 'https://www.' + name +'.com'
              webbrowser.open(web)
              Speak("Done Sir!")
       elif 'open new tab' in query:
            kb.press_and_release('ctrl + t')
       elif 'open new window' in query:
            kb.press_and_release('ctrl + n')
       elif 'chrome history' in query:
            kb.press_and_release('ctrl +h')
       elif 'chrome search' in query:
              Speak("This is What I Found For Your Serch Sir!")
              query = query.replace("jarvis","")
              query = query.replace("google  search","")
              pywhatkit.search(query)
              Speak("Done Sir!")
       elif 'website' in query:
              Speak("Ok, Sir, Launching......")
              query = query.replace("jarvis","")
              query = query.replace("website","")
              web1  = query.replace(" ","")
              web1  = query.replace("open","")
              web2  = 'https://www.'+web1 + '.com'
              webbrowser.open(web2)
              Speak("Launched")
       elif 'chrome automation' in query:
            ChromeAuto()
       elif 'wikipedia' in query:
            Speak("Searching Wikipedia.....")
            query = query.replace("jarvis","")
            query = query.replace("wikipedia","")
            wiki = wikipedia.summary(query,2)
            Speak(f"According To Wikipedia : {wiki}")
       elif 'tell me' in query:
            Speak("Searching Wikipedia.....")
            query = query.replace("jarvis","")
            query = query.replace("tell","")
            query = query.replace("me","")
            wiki = wikipedia.summary(query,2)
            Speak(f"According To Me : {wiki}")
       elif'chrome scrool up' in query:
              kb.send("up")
              kb.send("up")
              kb.send("up")
              kb.send("up")
#chrome tool stop 
#------------------------------------------------------------------------------------------
#open whatsapp send message tool start

#open whatsapp send message tool end
#------------------------------------------------------------------------------------------
#take a screen shot tool start
       elif 'take a screenshot' in query:
            screenshot()
       elif 'screenshot my screen' in query:
            screenshot()
       elif 'jarvis take a screenshot' in query:
            screenshot()
       elif 'screenshot lo jarvis' in query:
            screenshot()
#take a screen shot tool start 
#------------------------------------------------------------------------------------------
#jarvis remember program start
       elif 'jarvis remember that i will say' in query:
            remeberMsg = query.replace("remember that i will say","")
            remeberMsg = remeberMsg.replace("jarvis","")
            Speak("You Tell Me To Remind You That :"+remeberMsg)
            remeber = open('data.txt','w')
            remeber.write(remeberMsg)
            remeber.close()
       elif 'remember that' in query:
            remeberMsg = query.replace("remember that","")
            remeberMsg = remeberMsg.replace("jarvis","")
            Speak("You Tell Me To Remind You That :"+remeberMsg)
            remeber = open('data.txt','w')
            remeber.write(remeberMsg)
            remeber.close()
       elif 'what do you remember' in query:
            remeber = open('data.txt','r')
            Speak("You Tell Me That To" + remeber.read())
       elif 'what i say you to remember' in query:
            remeber = open('data.txt','r')
            Speak("You Tell Me That To" + remeber.read())
       elif 'do you remember anything' in query:
            remeber = open('data.txt','r')
            Speak("You Tell Me That To" + remeber.read())
#jarvis remember program start
#------------------------------------------------------------------------------------------
#alarm start
       elif 'set alarm' in query:
            Speak("Enter The Time !")
            time = input(": Enter The Time :")

            while True:
                Time_Ac = datetime.datetime.now()
                now = Time_Ac.strftime("%H:%M:%S")

                if now == time:
                    Speak("Time To Wake Up Sir!")
                    playsound('iron.mp3')
                    Speak("Alarm Closed!")

                elif now>time:
                    break
#alarm end
#------------------------------------------------------------------------------------------
#joke start
       elif 'jarvis tell me a joke' in query:
            get = pyjokes.get_joke()
            Speak(get)
       elif 'jarvis ek joke sunao' in query:
            get = pyjokes.get_joke()
            Speak(get)
#joke end
#------------------------------------------------------------------------------------------
#time telling start
       elif 'tell me time' in query:

              strTime = datetime.datetime.now().strftime("%H:%M:%S")
              Speak(f"Sir, The Time is{strTime}")
       elif "what's the time" in query:

              strTime = datetime.datetime.now().strftime("%H:%M:%S")
              Speak(f"Sir, The Time is{strTime}")
       elif "what's the time jarvis" in query:

              strTime = datetime.datetime.now().strftime("%H %M %S")
              Speak(f"Sir, The Time is{strTime}")
#time telling end
#------------------------------------------------------------------------------------------
#Study tool start
       elif 'study time' in query:
              StudyAuto()
#Study tool end
#------------------------------------------------------------------------------------------
#Instagram tool start
       elif'scrool up' in query:
              kb.send("up")
       elif'scrool down'in query:
              kb.send("down")
       elif'press up' in query:
              kb.send("up")
       elif'press down' in query:
              kb.send("down")
       elif'next post' in query:
              kb.send("up")
       elif'previous post'in query:
              kb.send("down")
       elif'upar karo'in query:
              kb.send("up")
       elif'neecha karo' in query:
              kb.send("down")
       elif'next reel' in query:
              kb.send("up")
       elif'previous reel'in query:
              kb.send("down")
#Instagram tool end
#------------------------------------------------------------------------------------------
#Spotify automation start
       elif'next song' in query:
              kb.send("ctrl+right")
       elif'previous song'in query:
              kb.send("ctrl+left")
       elif'increase volume' in query:
              kb.send("ctrl+up")
       elif'decrease volume' in query:
              kb.send("ctrl+down")
#Spotify automation end
#------------------------------------------------------------------------------------------
#video downloader start
       elif 'video downloader' in query:
            root = Tk()
            root.geometry('500x300')
            root.resizable(0,0)
            root.title("Youtube Video Downloader")
            Speak("Enter Video Url Here !")
            Label(root,text = "Youtube Video Downloader",font = 'arial 15 bold').pack()
            link = StringVar()
            Label(root,text = "Paste Yt Video URL Here",font = 'arial 15 bold').place(x=160,y=60)
            Entry(root,width = 70,textvariable = link).place(x=32,y=90)

            def VideoDownloader():
                url = YouTube(str(link.get()))
                video = url.streams.first()
                video.download()
                Label(root,text = "Downloaded",font = 'arial 15').place(x= 180,y=210)

            Button(root,text = "Download",font = 'arial 15 bold',bg = 'pale violet red',padx = 2 , command = VideoDownloader).place(x=180,y=150)

            root.mainloop()
            Speak("Video Downloaded")
#video downloader end
#------------------------------------------------------------------------------------------
#running apps informer






