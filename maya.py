import pyttsx3
import requests
import time 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import ctypes
import shutil
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib.request
import urllib.parse
import pyjokes
import folium
import winshell
import os, subprocess
import requests
from pprint import pprint
import win32com.shell.shell as shell
import winsound
import pyglet
import sys
import warnings
from datetime import date
from pynput.keyboard import Key, Controller
from pynput import keyboard
import keyboard
import numpy as np 
import cv2 
import pyautogui
import subprocess as sp
from datetime import datetime
import PyPDF2
from PyPDF2 import PdfFileReader
import psutil
import platform
import wmi
from twilio.rest import Client
import datetime
import speedtest
import pygame
import random
import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
import tkinter as tk
from tkinter import simpledialog
from PIL import Image
import pyqrcode
from pyzbar.pyzbar import decode
from tkinter import *
from tkinter.messagebox import *
import pyqrcode
from pyzbar.pyzbar import decode
from pyzbar import pyzbar
import pyperclip
#ls.lsHotword_loop()
    #time.sleep(10)
warnings.filterwarnings("ignore")
music = pyglet.resource.media('file.wav')
music.play()
time.sleep(1)

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

        
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def start():
    from datetime import datetime
    current_hour = int(datetime.now().strftime('%H'))
    if current_hour<12:
        print('Good morning')
        speak('Good morning')
    elif 12<=current_hour<18:
        print('Good afternoon')
        speak('Good afternoon')
    else:
        print('Good Evening')
        speak('Good Evening')

def timefn():
    strTime = datetime.datetime.now().strftime("%I:%M %p") 
    print(strTime)   
    speak(f"{strTime}")
    speak("I am Maya")



def NewsFromBBC():
     
    query_params = {
      "source": "bbc-news",
      "sortBy": "top",
      "apiKey": "4dbc17e007ab436fb66416009dfb59a8"
    }
    main_url = " https://newsapi.org/v1/articles"
 
    res = requests.get(main_url, params=query_params)
    open_bbc_page = res.json()
 
    article = open_bbc_page["articles"]
 
    results = []
     
    for ar in article:
        results.append(ar["title"])
         
    for i in range(len(results)):
         
        print(i + 1, results[i])
        dc=(i + 1, results[i])
        speak(dc)


def randommusic():
    path ="D:\\Song"
    file = os.path.join(path,random.choice(os.listdir(path)))
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()


def command():
    music = pyglet.resource.media('sky.wav')
    music.play()
    time.sleep(1)

    r = sr.Recognizer()
    r.energy_threshold = 50000
    with sr.Microphone(device_index=0) as source:
        r.adjust_for_ambient_noise(source)
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"Abhishek Patel: {query}\n")
    except Exception as e:
        time.sleep(1)   
        print("Say that again please...")
        speak("I'm sorry, but I can't help with that.")  
        return "None"
    return query

def commandhotword():

    r = sr.Recognizer()
    r.energy_threshold = 5000
    with sr.Microphone(device_index=0) as source:
        r.adjust_for_ambient_noise(source)
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        hotword = r.recognize_google(audio, language='en-in')
        print(f"Abhishek Patel: {hotword}\n")
    except Exception as e:
        #time.sleep(1)   
        print("Not Activated...")
        return "None"
    return hotword


if __name__ == "__main__":
    start()
    timefn()
    while True:
        hotword = commandhotword().lower()
        if re.search('maya', hotword):
            speak("Activated")
            query = command().lower()
        #time.sleep(10) 
            if 'wikipedia' in query:
                #a='king'
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia",'google')
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)


            elif 'open stackoverflow maya' in query:
                speak("Opening Stackoverflow")
                webbrowser.open("stackoverflow.com")

            elif 'lock maya' in query or 'lock' in query:
                speak("Locking Windows")
                ctypes.windll.user32.LockWorkStation()

            elif 'exit' in query or 'close maya' in query:
                speak("Good bye see you soon")
                exit()
            
            elif 'sleep' in query:
                commandhotword()
            elif 'how are you' in query:
                speak("i am good")

            elif 'play music maya' in query or 'play music for me' in query:
                music_dir = 'D:\\Song'
                songs = os.listdir(music_dir)
                print(songs)    
                os.startfile(os.path.join(music_dir, songs[0]))

            elif 'time maya' in query or 'time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S") 
                print(strTime)   
                speak(f"the time is {strTime}")

            elif 'open code maya' in query or 'open code' in query:
                codePath = "C:\\Users\\abhishekpatel\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(codePath)

            elif 'start' in query:
                speak("ye ham hai")
                speak("ye hamara vs code hai")
                speak("aur yahan hamari ")
                speak("coding  ho  rahi hai")

            #elif 'clear' in query:
                #speak("clearing screen")
                #os.system('cls' if os.name == 'nt' else 'clear')

            elif 'shutdown maya' in query or 'shutdown this pc' in query:
                speak("shutingdown your laptop see you soon")
                sd=command()
                try:

                    if 'yes' in sd:
                        time.sleep(2)
                        os.system('shutdown /s /t 1')
                    else:
                        speak("ok well !")
                except:
                    speak("something went wrong")

            elif 'shutdown' in query or 'shutdown this pc' in query:
                speak("shutingdown your laptop see you soon")
                sd=command()
                try:

                    if 'yes' in sd:
                        time.sleep(2)
                        os.system('shutdown /s /t 1')
                    else:
                        speak("ok well !")
                except:
                    speak("something went wrong")
                
            
            elif 'open google and search' in query:
                try:
                    a=query[22:]
                    reg_ex = re.search('open google and search (.*)', query)
                    search_for = query.split("search",1)[1]
                    url = 'https://www.google.com/'
                    if reg_ex:
                        subgoogle = reg_ex.group(1)
                        url = url + 'r/' + subgoogle
                    speak("Well i am fetching on google"+a)
                    driver = webdriver.Firefox()
                    time.sleep(2) 
                    driver.get('http://www.google.com')
                    search = driver.find_element_by_name('q') 
                    search.send_keys(str(search_for)) 
                    search.send_keys(Keys.RETURN)
                
                except :
                    speak("i think You colse the window ! before of the execuation")
            
            elif 'maya open google and search' in query:
                try:

                    a=query[27:]
                    reg_ex = re.search('open google and search (.*)', query)
                    search_for = query.split("search",1)[1]
                    url = 'https://www.google.com/'
                    if reg_ex:
                        subgoogle = reg_ex.group(1)
                        url = url + 'r/' + subgoogle
                    speak("Well i am fetching on google"+a)
                    driver = webdriver.Firefox() 
                    driver.get('http://www.google.com')
                    search = driver.find_element_by_name('q') 
                    search.send_keys(str(search_for)) 
                    search.send_keys(Keys.RETURN)
                except :
                    speak("i think You colse the window ! before of the execuation")

            elif 'what is' in query:
                try:

                    a=query
                    search_for = a
                    url = 'https://www.google.com/'
                    if search_for:
                        subgoogle = a
                        url = url + 'r/' + subgoogle
                    speak("Well i am fetching on google"+a)
                    driver = webdriver.Firefox() 
                    driver.get('http://www.google.com')
                    search = driver.find_element_by_name('q') 
                    search.send_keys(str(search_for)) 
                    search.send_keys(Keys.RETURN)
                except :
                    speak("i think You colse the window ! before of the execuation")
            
            elif 'how to use' in query:
                try:

                    a=query
                    search_for = a
                    url = 'https://www.google.com/'
                    if search_for:
                        subgoogle = a
                        url = url + 'r/' + subgoogle
                    speak("Well i am fetching on google"+a)
                    driver = webdriver.Firefox() 
                    driver.get('http://www.google.com')
                    search = driver.find_element_by_name('q') 
                    search.send_keys(str(search_for)) 
                    search.send_keys(Keys.RETURN)
                except :
                    speak("i think You colse the window ! before of the execuation")

            elif 'how to make' in query:
                try:

                    a=query
                    search_for = a
                    url = 'https://www.google.com/'
                    if search_for:
                        subgoogle = a
                        url = url + 'r/' + subgoogle
                    speak("Well i am fetching on google"+a)
                    driver = webdriver.Firefox() 
                    driver.get('http://www.google.com')
                    search = driver.find_element_by_name('q') 
                    search.send_keys(str(search_for)) 
                    search.send_keys(Keys.RETURN)
                except :
                    speak("i think You colse the window ! before of the execuation")


            elif "open youtube and play" in query:
                try:

                    x=query[21:]
                    def remove(string): 
                        return string.replace(" ", "") 
            
                    string = x
                    v=(remove(string))
                    speak("Well i am fetching "+v)
                    print(v)
                    html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + v)
                    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
                    print("https://www.youtube.com/watch?v=" + video_ids[0])
                    webbrowser.open("https://www.youtube.com/watch?v=" + video_ids[0])
                except :
                    speak("i think You colse the window ! before of the execuation")


            
            elif "hold 30 second" in query:
                speak("Well i am going to sleep for 30 seconds")
                time.sleep(0)
                speak("Now i am Activated")

            elif "hold 1 minute" in query:
                speak("Well i am going to sleep for 1 minute")
                time.sleep(0)
                speak("Now i am Activated")

            
            elif 'tell me joke' in query:
                print(pyjokes.get_joke())
                speak(pyjokes.get_joke())
                time.sleep(1)
                speak("ha ha ha")

            
            elif 'map of india' in query:
                speak('wait i am fatching india map')
                time.sleep(3)
                india = folium.Map(location = [20.5937, 78.9629]).save("india.html")
                webbrowser.open("india.html")
            
            elif  'bin' in query:
                try:

                    speak("i am trying to clear recycle bin")
                    time.sleep(3)
                    winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=False)
                    speak("Sucessfully clear recycle bin")
                except :
                    speak("Sorry! nothing in recycle bin")
            
            elif 'clear recycle bin' in query:
                try:

                    speak("i am trying to clear recycle bin")
                    time.sleep(3)
                    winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=False)
                    speak("successfully clear recycle bin")
                except :
                    speak("Sorry! nothing in recycle bin")

            elif 'clear bin' in query:
                try:

                    speak("i am trying to clear recycle bin")
                    time.sleep(3)
                    winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=False)
                    speak("successfully clear recycle bin")
                except :
                    speak("Sorry! nothing in recycle bin")



            elif  'who are you' in query:


                url = 'F:\Raw\Maya\JSNamemaya/index.html'
                webbrowser.open(url, new=2)

                speak("i am Maya human interaction program Develop By Abhishek Patel and i am work with Python")

            elif 'who created you' in query:
                speak("i am very interested to tell you i am develop by Abhishek Patel ")
                url = 'F:\Raw\Maya\JSName/index.html'
                webbrowser.open(url, new=2)
                speak("wait ! i am connecting with by developer Abhishek Patel")
                time.sleep(2)
                webbrowser.open("https://in.linkedin.com/in/abhishek-verma-2578411bb")
                speak("For more query build touch with him : thank you")

            
            elif 'who develop you' in query:
                speak("i am very interested to tell you i am develop by Abhishek Patel ")
                url = 'F:\Raw\Maya\JSName/index.html'
                webbrowser.open(url, new=2)
                speak("wait ! i am connecting with by developer Abhishek Patel")
                time.sleep(2)
                webbrowser.open("https://in.linkedin.com/in/abhishek-verma-2578411bb")
                speak("For more query build touch with him : thank you")

            
            elif 'who is your developer' in query:
                speak("i am very interested to tell you i am develop by Abhishek Patel ")

                url = 'F:\Raw\Maya\JSName/index.html'
                webbrowser.open(url, new=2)
                speak("wait ! i am connecting with by developer Abhishek Patel")
                time.sleep(2)
                webbrowser.open("https://in.linkedin.com/in/abhishek-verma-2578411bb")
                speak("For more query build touch with him : thank you")

            
            elif 'where am i' in query:
                speak('wait ! i am fatching')
                time.sleep(3)
                india = folium.Map(location = ['26.90173', '80.97416']).save("india1.html")
                webbrowser.open("india1.html")
            
            elif 'jay hind' in query:
                speak("jay bharat")

                
            elif 'thank you' in query:
                d = 'welcome','my pleasure' , 'see you soon'
                speak(random.choice(d))
            elif 'ok thank you' in query:
                d = 'welcome','my pleasure' , 'see you soon'
                speak(random.choice(d))
            elif 'ok' in query:
                speak("well !")
            elif 'hello maya' in query or 'hello' in query:
                d = 'hello','hii there' , 'heyy there'
                speak(random.choice(d))
            
            elif re.search('open browser', query):
                speak("opening chrome browser")
                webbrowser.open("chrome.exe")
            elif re.search('open webbrowser', query):
                speak("opening chrome browser")
                webbrowser.open("chrome.exe")
            elif re.search('open chrome', query):
                speak("opening chrome browser")
                webbrowser.open("chrome.exe")
            
            elif re.search('close browser', query):
                speak("closing chrome browser")
                browserExe = "chrome.exe" 
                os.system("taskkill /f /im "+browserExe)
            elif re.search('close webbrowser', query):
                speak("closing chrome browser")
                browserExe = "chrome.exe" 
                os.system("taskkill /f /im "+browserExe)
            elif re.search('close chrome', query):
                speak("closing chrome browser")
                browserExe = "chrome.exe" 
                os.system("taskkill /f /im "+browserExe)
            
            elif re.search('close youtube', query):
                speak("closing youtube")
                browserExe = "chrome.exe" 
                os.system("taskkill /f /im "+browserExe)


            elif re.search('open Command prompt', query) or re.search('open cmd', query):
                speak("opening Command prompt")
                webbrowser.open("cmd.exe")
            

            elif re.search('close cmd', query) or re.search('close Command prompt', query):
                speak("closing Command prompt")
                browserExe = "cmd.exe" 
                os.system("taskkill /f /im "+browserExe)

            elif re.search('open powershell', query) or re.search('open shell', query):
                speak("opening powershell")
                webbrowser.open("powershell.exe")
            

            elif re.search('close shell', query) or re.search('close powershell', query):
                speak("closing powershell")
                browserExe = "powershell.exe" 
                os.system("taskkill /f /im "+browserExe)

            

            
            
            elif 'delete temporary files' in query:
                speak("wait i am fatching data")
                time.sleep(3)
                del_dir = r'C:\\Users\\abhishekpatel\\AppData\\Local\\Temp'
                del_dir2 = r'C:\\Windows\\Temp'
                del_dir3 = r'C:\\Windows\\SoftwareDistribution\\Download'
                obj = subprocess.Popen('rmdir /S /Q %s' % del_dir, shell=True, stdout = subprocess.PIPE, stderr= subprocess.PIPE)
                obj2 = subprocess.Popen('rmdir /S /Q %s' % del_dir2, shell=True, stdout = subprocess.PIPE, stderr= subprocess.PIPE)
                obj3 = subprocess.Popen('rmdir /S /Q %s' % del_dir3, shell=True, stdout = subprocess.PIPE, stderr= subprocess.PIPE)
                trp = obj.communicate()
                trp2= obj2.communicate()
                trp3= obj3.communicate()
                rCod = obj.returncode
                rCod2 = obj2.returncode
                rCod3 = obj3.returncode
                if rCod == 0:
                    print('Success: Cleaned Windows Temp Folder')
                    speak("Sucessfully Cleaned Windows Temporary files")
                else:
                    print('Fail: Unable to Clean Windows Temp Folder')
                    speak("Fail Unable to  Cleaned Windows Temporary files")

            elif 'delete temporary file' in query:
                speak("wait i am fatching data")
                time.sleep(3)
                del_dir = r'C:\\Users\\abhishekpatel\\AppData\\Local\\Temp'
                del_dir2 = r'C:\\Windows\\Temp'
                del_dir3 = r'C:\\Windows\\SoftwareDistribution\\Download'
                obj = subprocess.Popen('rmdir /S /Q %s' % del_dir, shell=True, stdout = subprocess.PIPE, stderr= subprocess.PIPE)
                obj2 = subprocess.Popen('rmdir /S /Q %s' % del_dir2, shell=True, stdout = subprocess.PIPE, stderr= subprocess.PIPE)
                obj3 = subprocess.Popen('rmdir /S /Q %s' % del_dir3, shell=True, stdout = subprocess.PIPE, stderr= subprocess.PIPE)
                trp = obj.communicate()
                trp2= obj2.communicate()
                trp3= obj3.communicate()
                rCod = obj.returncode
                rCod2 = obj2.returncode
                rCod3 = obj3.returncode
                if rCod == 0:
                    print('Success: Cleaned Windows Temp Folder')
                    speak("Sucessfully Cleaned Windows Temporary files")
                else:
                    print('Fail: Unable to Clean Windows Temp Folder')
                    speak("Fail Unable to  Cleaned Windows Temporary files")

            elif  'weather of ' in query:
                speak("wait i am fatching weather forecast data")
                a=query[11:]
                def weather_data(query):
                    res=requests.get('http://api.openweathermap.org/data/2.5/weather?'+query+'&APPID=b35975e18dc93725acb092f7272cc6b8&units=metric');
                    return res.json();
                def print_weather(result,city):
                    print("{}'s temperature: {}°C ".format(city,result['main']['temp']))
                    speak("{}'s temperature: {}°C ".format(city,result['main']['temp']))
                    print("Wind speed: {} meterpersecond".format(result['wind']['speed']))
                    speak("Wind speed: {} meter per second".format(result['wind']['speed']))
                    print("Description: {}".format(result['weather'][0]['description']))
                    speak("Description: {}".format(result['weather'][0]['description']))
                    print("Weather: {}".format(result['weather'][0]['main']))
                    speak("Weather: {}".format(result['weather'][0]['main']))
                def main():
                    city= a
                    print()
                    try:
                        query='q='+city;
                        w_data=weather_data(query);
                        print_weather(w_data, city)
                        print()
                    except:
                        print('City name not found...')
                        speak("City name not found")
                if __name__=='__main__':
                    main()

            elif 'open task manager' in query:
                commands = 'taskmgr'
                shell.ShellExecuteEx(lpVerb='runas', lpFile='cmd.exe', lpParameters='/c '+commands)
                speak("sucessfully open task manager")
                time.sleep(5)


            elif 'help' in query:
                speak("opening help page")
                webbrowser.open("help.pdf")
                speak("you can check it now i am going to sleep for 20 seconds")
                time.sleep(5)
                speak("now i am activated")

            elif re.search("connect with your developer", query) or re.search("call your developer", query):
                speak("wait ! i am connecting with by developer Abhishek Patel")
                url = 'F:\Raw\Maya\JSName/index.html'
                webbrowser.open(url, new=2)
                time.sleep(2)
                webbrowser.open("https://in.linkedin.com/in/abhishek-verma-2578411bb")
                speak("For more query build touch with him : thank you")

            
            elif 'wait' in query:
                speak("how much minute")
                speak("tell me in !only minutes")
                try :
                    tym=command()
                    intym=int(tym)
                    cc=intym*60
                    print(cc)
                    speak("well ! i am going to sleep")
                    time.sleep(cc)
                    speak("hey there now i am activated")
                except:
                        speak("something went wrong")
                
            elif 'create application mode maya' in query: 
                speak("wait i am createting Application mode on desktop")
                time.sleep(1)
                directory = "Applications.{4234d49b-0245-4df3-b780-3893943456e1}"


                parent_dir = "C:\\Users\\abhishekpatel\\Desktop"


                path = os.path.join(parent_dir, directory) 

                try : 
                    os.makedirs(path, exist_ok = True) 
                    print("Directory '%s' created successfully" % directory)
                    speak("application mode activate successfully")
                except OSError as error:
                    speak("i am trouble to activating application mode")
                
            elif 'create application mode' in query: 
                speak("wait i am creating Application mode on desktop")
                time.sleep(1)
                directory = "Applications.{4234d49b-0245-4df3-b780-3893943456e1}"


                parent_dir = "C:\\Users\\abhishekpatel\\Desktop"


                path = os.path.join(parent_dir, directory) 

                try : 
                    os.makedirs(path, exist_ok = True) 
                    print("Directory '%s' created successfully" % directory)
                    speak("application mode created successfully")
                except OSError as error:
                    speak("i am trouble to creating application mode")


            elif 'create god mode' in query: 
                speak("wait i am creating god mode on desktop")
                time.sleep(1)
                directory = "God Mode.{ED7BA470-8E54-465E-825C-99712043E01C}"


                parent_dir = "C:\\Users\\abhishekpatel\\Desktop"


                path = os.path.join(parent_dir, directory) 

                try : 
                    os.makedirs(path, exist_ok = True) 
                    print("Directory '%s' created successfully" % directory)
                    speak("god mode created successfully")
                except OSError as error:
                    speak("i am trouble to creating application mode")

            elif 'create god mode maya' in query: 
                speak("wait i am creating god mode on desktop")
                time.sleep(1)
                directory = "God Mode.{ED7BA470-8E54-465E-825C-99712043E01C}"


                parent_dir = "C:\\Users\\abhishekpatel\\Desktop"


                path = os.path.join(parent_dir, directory) 

                try : 
                    os.makedirs(path, exist_ok = True) 
                    print("Directory '%s' created successfully" % directory)
                    speak("god mode created successfully")
                except OSError as error:
                    speak("i am trouble to creating application mode")
                
            
            elif 'delete application mode maya' in query:

                location=("C:\\Users\\abhishekpatel\\Desktop")
                dir = "Applications.{4234d49b-0245-4df3-b780-3893943456e1}"
                path = os.path.join(location, dir) 
                try:
                    shutil.rmtree(path)
                    speak("application mode deleted successfully")

                except OSError as e:
                    print ("Error: %s - %s." % (e.filename, e.strerror))
                    speak("application mode nothing is there")

            elif 'delete application mode' in query:

                location=("C:\\Users\\abhishekpatel\\Desktop")
                dir = "Applications.{4234d49b-0245-4df3-b780-3893943456e1}"
                path = os.path.join(location, dir) 
                try:
                    shutil.rmtree(path)
                    speak("application mode deleted successfully")

                except OSError as e:
                    print ("Error: %s - %s." % (e.filename, e.strerror))
                    speak("application mode nothing is there")
                
            elif 'delete god mode maya' in query:

                location=("C:\\Users\\abhishekpatel\\Desktop")
                dir = "God Mode.{ED7BA470-8E54-465E-825C-99712043E01C}"
                path = os.path.join(location, dir) 
                try:
                    shutil.rmtree(path)
                    speak("god mode deleted successfully")

                except OSError as e:
                    print ("Error: %s - %s." % (e.filename, e.strerror))
                    speak("god mode nothing is there")

            elif 'delete god mode' in query:

                location=("C:\\Users\\abhishekpatel\\Desktop")
                dir = "God Mode.{ED7BA470-8E54-465E-825C-99712043E01C}"
                path = os.path.join(location, dir) 
                try:
                    shutil.rmtree(path)
                    speak("god mode deleted successfully")

                except OSError as e:
                    print ("Error: %s - %s." % (e.filename, e.strerror))
                    speak("god mode nothing is there")

            elif re.search('date maya', query) or re.search('date', query):
                today = date.today()
                d2 = today.strftime("%B %d, %Y")
                speak(d2)

            elif re.search('todays date', query) or re.search('today date', query):
                today = date.today()
                d2 = today.strftime("%B %d, %Y")
                speak(d2)

            elif "go to" in query:
                try:
                    cmd=""
                    query=query.replace("go to ", "")
                    for i in query:
                        cmd=cmd+i+"+"
                    cmd = cmd[:-1]
                    print(cmd)
                    keyboard.press_and_release(cmd)
                    keyboard.press_and_release("Enter")
                    command()
                except :
                    speak("Troble to open this")
            
            elif "open this pc" in query:
                try:

                    keyboard.press_and_release("windows+E")
                    command()
                except :
                    speak("for openning this pc please tell open this pc")

            elif re.search('take screenshot', query) or re.search('take a screenshot', query):
                image = pyautogui.screenshot()
                speak("ok i am taking screenshot")
                print("1")
                speak("1")
                time.sleep(2)
                print("2")
                speak(2)
                time.sleep(2)
                print("3")
                speak("3")
                time.sleep(2)
                image = cv2.cvtColor(np.array(image), 
                                    cv2.COLOR_RGB2BGR) 
                cv2.imwrite("C:\\Users\\abhishekpatel\\Desktop\\image.png", image)
                speak("screenshot done wait i will show you")
                img = cv2.imread("C:\\Users\\abhishekpatel\\Desktop\\image.png", cv2.IMREAD_COLOR)
                cv2.imshow("C:\\Users\\abhishekpatel\\Desktop\\image.png", img)
                cv2.waitKey(0)
                cv2.destroyAllWindows()

            elif re.search('open notepad', query):
                speak("opening notepad")
                programName = "notepad.exe"
                fileName = "Abhishek Patel.txt"
                sp.Popen([programName, fileName])

            elif re.search('close notepad', query):
                speak("closing notepad")
                subprocess.call(["taskkill","/F","/IM","notepad.exe"])


            elif re.search('read pdf', query):
                speak("i am trying to access pdf and read")
                time.sleep(1)
                try:
                    pdf_document = "read.pdf"
                    with open(pdf_document, "rb") as filehandle:
                        pdf = PdfFileReader(filehandle)
                        info = pdf.getDocumentInfo()
                        pages = pdf.getNumPages()
                        print(pages)
                        speak("total number of pages is ")
                        speak(pages)

                        print (info)
                        speak(info)
                        print ("number of pages: %i" % pages)

                        page1 = pdf.getPage(0)
                        print(page1)
                        text=page1.extractText()
                        print(text)
                        speak(text)

                
                except :
                    speak("Something went wrong or pdf not found please copy you pdf paste on my working disractory and rename this to read.pdf")


            elif re.search('open camera',query):
                speak("i am trying to start camera")
                time.sleep(1)
                speak("Note : camera exit manualy with small e key")
                vid_capture = cv2.VideoCapture(0)
                vid_cod = cv2.VideoWriter_fourcc(*'XVID')
                output = cv2.VideoWriter("videos/cam_video.mp4", vid_cod, 20.0, (640,480))
                while(True):
                    ret,frame = vid_capture.read()
                    cv2.imshow("Abhishek Patel @imdarkcoder", frame)
                    output.write(frame)
                    if cv2.waitKey(1) &0XFF == ord("e"):
                        break
                vid_capture.release()
                output.release()
                command()
                
            elif re.search("all system information", query) or re.search("all hardware information", query):
                speak("i am fatching all system information")
                time.sleep(1)
                import time
                import datetime
                from time import mktime
                from datetime import datetime
                mysys = platform.uname()
                c = wmi.WMI()    
                my_system = c.Win32_ComputerSystem()[0]
                psutil.cpu_percent()
                psutil.virtual_memory()
                dict(psutil.virtual_memory()._asdict())
                pid = os.getpid()
                boot_time_timestamp = psutil.boot_time()
                bt = datetime.fromtimestamp(boot_time_timestamp)
                cpufreq = psutil.cpu_freq()
                
                print(f"Manufacturer: {my_system.Manufacturer}")
                print(f"Model: {my_system. Model}")
                print(f"Name: {my_system.Name}")
                print(f"NumberOfProcessors: {my_system.NumberOfProcessors}")
                print(f"SystemType: {my_system.SystemType}")
                print(f"SystemFamily: {my_system.SystemFamily}")
                print(f"System: {mysys.system}")
                print(f"Node Name: {mysys.node}")
                print(f"Release: {mysys.release}")
                print(f"Version: {mysys.version}")
                print(f"Machine: {mysys.machine}")
                print(f"Processor: {mysys.processor}")
                print("My Working language: Python 3")
                print("Speech API: Google Speech recognation api")
                print("Develop by: Abhishek Patel")
                print(f"Operating System Version: {mysys.release}")
                t=psutil.virtual_memory().percent
                at=psutil.virtual_memory().available * 100 / psutil.virtual_memory().total
                print(t)
                print(at)
                print("Process ID:",pid)

                print(f"Boot Time: {bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}")


                print("Physical cores:", psutil.cpu_count(logical=False))
                ph=psutil.cpu_count(logical=False)
                print("Total cores:", psutil.cpu_count(logical=True))
                tc=psutil.cpu_count(logical=True)

                print(f"Max Frequency: {cpufreq.max:.2f}Mhz")
                print(f"Min Frequency: {cpufreq.min:.2f}Mhz")
                print(f"Current Frequency: {cpufreq.current:.2f}Mhz")
                print("CPU Usage Per Core:")
                for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
                    print(f"Core {i}: {percentage}%")
                print(f"Total CPU Usage: {psutil.cpu_percent()}%")

                speak(f"Manufacturer: {my_system.Manufacturer}")
                speak(f"Model: {my_system. Model}")
                speak(f"Name: {my_system.Name}")
                speak(f"NumberOfProcessors: {my_system.NumberOfProcessors}")
                speak(f"SystemType: {my_system.SystemType}")
                speak(f"SystemFamily: {my_system.SystemFamily}")
                speak(f"Operating System: {mysys.system}")
                speak(f"Node username: {mysys.node}")
                speak(f"Release: {mysys.release}")
                speak(f"Operating System Version: {mysys.release}")
                speak(f"Version: {mysys.version}")
                speak(f"Machine: {mysys.machine}")
                speak(f"Processor: {mysys.processor}")
                speak("My Working language: Python 3")
                speak("Speech API: Google Speech recognation api")
                speak("Develop by: Abhishek Patel")
                speak("Total use RAM:")
                speak(t)
                speak("percentage")
                speak("available RAM:")
                speak(at)
                speak("percentage")
                speak("Process ID:")
                speak(pid)
                speak(f"Boot Time: {bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}")
                speak("Physical cores:")
                speak(ph)
                speak("Total cores:")
                speak(tc)
                speak("Work Frequency of CPU")
                speak(f"Max Frequency: {cpufreq.max:.2f}Mhz")
                speak(f"Min Frequency: {cpufreq.min:.2f}Mhz")
                speak(f"Current Frequency: {cpufreq.current:.2f}Mhz")
                speak("CPU Usage Per Core:")
                for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
                    speak(f"Core {i}: {percentage}%")
                speak(f"Total CPU Usage: {psutil.cpu_percent()}%")
                total, used, free = shutil.disk_usage("/")
                obj_Disk = psutil.disk_usage('/')

                print("Total: %d Gigabytes" % (total // (2**30)))
                print("Used: %d Gigabytes" % (used // (2**30)))
                print("Free: %d Gigabytes" % (free // (2**30)))
                print (obj_Disk.percent)
                

                speak("Current Working disk Total: %d Gigabytes" % (total // (2**30)))
                speak("Current Working disk Used: %d Gigabytes" % (used // (2**30)))
                speak("Current Working disk Free: %d Gigabytes" % (free // (2**30)))
                speak("total percentage")
                speak(obj_Disk.percent)


            elif re.search("network information", query):
                speak("i am fatching network information")
                time.sleep(1)
                if_addrs = psutil.net_if_addrs()
                for interface_name, interface_addresses in if_addrs.items():
                    for address in interface_addresses:
                        print(f"=== Interface: {interface_name} ===")
                        speak(f" Interface: {interface_name}")

                        if str(address.family) == 'AddressFamily.AF_INET':
                            print(f"  IP Address: {address.address}")
                            print(f"  Netmask: {address.netmask}")
                            print(f"  Broadcast IP: {address.broadcast}")
                            speak(f"  IP Address: {address.address}")
                            speak(f"  Netmask: {address.netmask}")
                            speak(f"  Broadcast IP: {address.broadcast}")
                        elif str(address.family) == 'AddressFamily.AF_PACKET':
                            print(f"  MAC Address: {address.address}")
                            print(f"  Netmask: {address.netmask}")
                            print(f"  Broadcast MAC: {address.broadcast}")
                            speak(f"  MAC Address: {address.address}")
                            speak(f"  Netmask: {address.netmask}")
                            speak(f"  Broadcast MAC: {address.broadcast}")
                net_io = psutil.net_io_counters()

            elif re.search("send message", query) or re.search("send a message", query):
                try:
                    speak("what you want to send")

                    ms=command()

                    account_sid = os.environ['AC043775f4ec9bf0e35143764b1e5a3da1']
                    auth_token = os.environ['c37a8cb081821a27eb320b90e8ad8603']
                    client = Client(account_sid, auth_token)

                    message = client.messages \
                        .create(
                            body=ms,
                            from_='+15084333611',
                            to='+918874250240'
                        )

                    print(message.sid)
                except:
                    speak("something went wrong")

            elif re.search("internet speed", query):
                speak("plaese wait while i am fatching speed data")
                st = speedtest.Speedtest()
                u = st.upload()
                d = st.download()
                print("downloading",d)
                print("uploding",u)
                c = d / 1000000
                v = u / 1000000
                print("Downloading Speed in Megabits")
                print(c)
                print("Megabits per second")
                print("Uploading Speed in megabits")
                print(v)
                print("Megabits per second")
                n = c / 8
                m = v / 8
                print("Downloading Speed in megabytes")
                print(n)
                print("Megabytes per second")
                print("Uploading Speed in megabytes")
                print(m)
                print("Megabytes per second")


                c = d / 1000000
                v = u / 1000000
                speak("Downloading Speed in Megabits")
                speak(c)
                speak("Megabits per second")
                speak("Uploading Speed in megabits")
                speak(v)
                speak("Megabits per second")
                n = c / 8
                m = v / 8
                speak("Downloading Speed in megabytes")
                speak(n)
                speak("Megabytes per second")
                speak("Uploading Speed in megabytes")
                speak(m)
                speak("Megabytes per second")

            elif re.search("play me a song", query):
                randommusic()


            elif re.search("close music", query):
                pygame.mixer.music.stop()

            elif re.search("top bbc news", query):
                NewsFromBBC() 

            elif re.search("today's news", query):
                news_url="https://news.google.com/news/rss"
                Client=urlopen(news_url)
                xml_page=Client.read()
                Client.close()

                soup_page=soup(xml_page,"xml")
                news_list=soup_page.findAll("item")
                for news in news_list:
                    print(news.pubDate.text)
                    print(news.title.text)
                    print(news.link.text)
                    #speak(news.pubDate.text)
                    speak(news.title.text)
                    #speak(news.link.text)

            
            elif re.search("show me battery health", query) or re.search("battery health", query):
                try:
                    speak("wait i am fatching battery data")
                    time.sleep(2)
                    speak("done ! i will show you and i also save HTML file in your local directory")
                    os.system('powercfg /batteryreport') 
                    "By : Abhishek Patel @imdarkcoder"
                    # move report file one dir to another dir // In your case dir path may be diffrent
                    #shutil.move('C:/Users/abhishekpatel/battery-report.html', 'C:/Users/abhishekpatel/Desktop/battery-report.html')
                    # Open report file on web
                    url = 'file:///F:/Raw/Maya/battery-report.html'
                    webbrowser.open(url, new=1)
                except:
                    speak("Soryy !battery data went worng")

            elif re.search("delete battery report", query) or re.search("delete battery health file", query):
                try:

                    os.remove("battery-report.html")
                    speak("done ! Battery health report was deleted")
                except:
                    speak("data not found")

            
            elif re.search("wi-fi password", query) or re.search("show all wi-fi passwords", query):
                try:

                    import subprocess

                    data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
                    profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
                    for i in profiles:
                        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
                        results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
                        try:
                            print ("{:<30}|  {:<}".format(i, results[0]))
                            res = ("{:<30}|  {:<}".format(i, results[0]))
                            speak(res)
                        except IndexError:
                            print ("{:<30}|  {:<}".format(i, ""))
                            res2 = ("{:<30}|  {:<}".format(i, ""))
                            speak(res2)
                except :

                    speak("passwords not found")


            elif re.search("all wi-fi password", query) or re.search("all wi-fi passwords", query):
                try:

                    import subprocess

                    data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
                    profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
                    for i in profiles:
                        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
                        results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
                        try:
                            print ("{:<30}|  {:<}".format(i, results[0]))
                            res = ("{:<30}|  {:<}".format(i, results[0]))
                            speak(res)
                        except IndexError:
                            print ("{:<30}|  {:<}".format(i, ""))
                            res2 = ("{:<30}|  {:<}".format(i, ""))
                            speak(res2)
                except:
                    speak("passwords not found")


            elif re.search("maya generate qr code", query) or re.search("generate qr code", query):
                try:

                    from PIL import Image


                    speak("i will show you input box ! please give me QR data in the manualy")
                    time.sleep(1)
                    ROOT = tk.Tk()

                    ROOT.withdraw()
                    USER_INP = simpledialog.askstring(title="QR Generator",
                                                    prompt="QR input Data:")
                    print("Hii", USER_INP)

                    speak("please wait i am generating your qr code")

                    #time.sleep(0)

                    qr = pyqrcode.create(USER_INP)


                    img = qr.png("QRgen.jpg", scale = 5) 

                    speak("Qr code generated successfully..")
                    speak("The image is saved in the current working directory")
                    speak("wait i will show you your QR code")

                    im = Image.open(r"QRgen.jpg") 
                    
                    im.show()
                except :

                    speak("Unable to generate QR code")

            elif re.search("maya read qr code", query) or re.search("read qr code", query):
                try:
                    from PIL import Image

                    speak("ok ! i will show you the decode or readble QR code data")

                    img = Image.open('QRgen.jpg')
                    output = pyzbar.decode(img)
                    c=(output[0].data.decode())
                    print(c)


                    def printSomething():
                        label = Label(root, text= c)
                        label.pack()
                        speak("QR data is !!")
                        speak(c)

                    def quit():
                        global root
                        root.destroy()
                        time.sleep(2)
                        root.quit()  

                    root = Tk()

                    button = Button(root, text="Show QR data", command=printSomething) 
                    button.pack()
                    Button(root, text="Exit with this", command=quit).pack()

                    root.mainloop()
                    commandhotword()
                except:
                    speak("Thank you")

            elif re.search("maya delete qr code", query) or re.search("delete qr code", query):
                try:
                    os.remove("QRgen.jpg")
                    speak("done ! QR code image was deleted")
                except:
                    speak("QR code not found")
            
            elif re.search("maya delete qr code image", query) or re.search("delete qr code image", query):
                try:

                    os.remove("QRgen.jpg")
                    speak("done ! QR code image was deleted")
                except:
                    speak("qr code not found")

            elif re.search("cpu information" , query):
                speak("i am fatching CPU information")
                time.sleep(1)    
                import time
                import datetime
                from time import mktime
                from datetime import datetime
                psutil.cpu_percent()
                pid = os.getpid()
                boot_time_timestamp = psutil.boot_time()
                bt = datetime.fromtimestamp(boot_time_timestamp)
                cpufreq = psutil.cpu_freq()
                speak("processs id")
                speak(pid)
                speak("boot time")
                speak(f"Boot Time: {bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}")
                print("Physical cores:", psutil.cpu_count(logical=False))
                ph=psutil.cpu_count(logical=False)
                print("Total cores:", psutil.cpu_count(logical=True))
                tc=psutil.cpu_count(logical=True)
                speak("Physical cores:")
                speak(ph)
                speak("Total cores:")
                speak(tc)
                speak("Work Frequency of CPU")
                speak(f"Max Frequency: {cpufreq.max:.2f}Mhz")
                speak(f"Min Frequency: {cpufreq.min:.2f}Mhz")
                speak(f"Current Frequency: {cpufreq.current:.2f}Mhz")
                speak("CPU Usage Per Core:")
                for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
                    speak(f"Core {i}: {percentage}%")
                speak(f"Total CPU Usage: {psutil.cpu_percent()}%")
                total, used, free = shutil.disk_usage("/")
                obj_Disk = psutil.disk_usage('/')

            elif re.search("ram information" , query):
                speak("i am fatching RAM information")
                time.sleep(1)
                import time
                import datetime
                from time import mktime
                from datetime import datetime
                psutil.virtual_memory()
                dict(psutil.virtual_memory()._asdict())
                pid = os.getpid()
                t=psutil.virtual_memory().percent
                at=psutil.virtual_memory().available * 100 / psutil.virtual_memory().total
                print(t)
                print(at)
                speak("Total use RAM:")
                speak(t)
                speak("percentage")
                speak("available RAM:")
                speak(at)
                speak("percentage")
                speak("Process ID:")
                speak(pid)


            elif re.search("hardware information", query):
                speak("i am fatching hardware information")
                time.sleep(1)
                import time
                import datetime
                from time import mktime
                from datetime import datetime

                mysys = platform.uname()
                c = wmi.WMI()    
                my_system = c.Win32_ComputerSystem()[0]
                psutil.cpu_percent()
                pid = os.getpid()
                speak("process id")
                speak(pid)
                speak(f"Manufacturer: {my_system.Manufacturer}")
                speak(f"Model: {my_system. Model}")
                speak(f"Name: {my_system.Name}")
                speak(f"NumberOfProcessors: {my_system.NumberOfProcessors}")
                speak(f"SystemType: {my_system.SystemType}")
                speak(f"SystemFamily: {my_system.SystemFamily}")
                speak(f"Node username: {mysys.node}")
                speak(f"Release: {mysys.release}")
                speak(f"Version: {mysys.version}")
                speak(f"Machine: {mysys.machine}")
                speak(f"Processor: {mysys.processor}")

                
            elif re.search("find ip address", query) or re.search("get ip address", query):

                speak("i am fatching data of ip address")
                import socket as s
                speak("please ! input website name with domain name like .com .in something")
                ROOT = tk.Tk()
                ROOT.withdraw()
                USER_INP = simpledialog.askstring(title="IP",
                                                prompt="IP Address with domain name:")
                print("IP : ", USER_INP)
                c=USER_INP
                host = c
                speak("your website name is ")
                speak(c)
                print(f'ip of{host} is {s.gethostbyname(host)}')
                ipip=(f'IP of {host} is {s.gethostbyname(host)}')
                def printSomething():
                    label = Label(root, text= ipip)
                    label.pack()
                    speak(ipip)

                def quit():
                    global root
                    root.destroy()
                    time.sleep(2)
                    root.quit()  

                root = Tk()
                button = Button(root, text="Show Me", command=printSomething) 
                button.pack()
                Button(root, text="Exit with this", command=quit).pack()
                root.mainloop()
                commandhotword()

            elif re.search("get size of image", query) or re.search("get image resolution", query):
                try:
                    from PIL import Image
                    speak("please ! make sure")
                    speak("photo or image file save on my directory and rename with size.jpg name")
                    img = cv2.imread("size.jpg")
                    wid = img.shape[1]
                    hgt = img.shape[0]
                    print(str(wid) + "x" + str(hgt))
                    res = (str(wid) + "x" + str(hgt))
                    speak(res)

                    from skimage import io
                    import pandas as pd
                    path = "size.jpg"
                    my_df = pd.DataFrame(img.flatten())
                    print("The image pixels dimensions are ")
                    print(my_df.shape)
                    speak("The image pixels dimensions are ")
                    px = (my_df.shape)
                    speak(px)
                    speak("resolution and pixels")
                    img = Image.open("size.jpg")

                    width, height = img.size

                    print(f"dimensions of an image are : {width}x{height}")
                    are = (f"dimensions of an image are : {width}x{height}")
                    speak(are)
                except:
                    speak("file not found")


            elif re.search("get pixel of image", query) or re.search("image detail", query):
                try:
                    from PIL import Image

                    speak("please ! make sure")
                    speak("photo or image save on my directory and rename with size.jpg name")
                    img = cv2.imread("size.jpg")
                    wid = img.shape[1]
                    hgt = img.shape[0]
                    print(str(wid) + "x" + str(hgt))
                    res = (str(wid) + "x" + str(hgt))
                    speak(res)
                    speak("resolution and pixels")

                    from skimage import io
                    import pandas as pd
                    path = "size.jpg"
                    my_df = pd.DataFrame(img.flatten())
                    print("The image pixels dimensions are ")
                    print(my_df.shape)
                    speak("The image pixels dimensions are ")
                    px = (my_df.shape)
                    speak(px)
                    speak("resolution and pixels")
                    img = Image.open("size.jpg")

                    width, height = img.size

                    print(f"dimensions of an image are : {width}x{height}")
                    are = (f"dimensions of an image are : {width}x{height}")
                    speak(are)
                
                except:
                    speak("file not found")


            elif re.search("path short", query) or re.search("link short", query):

                speak("i am started shorter engine")
                import socket as s
                speak("i will show you input box ! please paste URL or linj here")
                ROOT = tk.Tk()
                ROOT.withdraw()
                USER_INP = simpledialog.askstring(title="URL",
                                                prompt="Paste URL here:")
                print("IP : ", USER_INP)
                c=USER_INP
                host = c
                speak("your url is")
                speak(c)
                import pyshorteners

                def shorten(url):
                    link = pyshorteners.Shortener()
                    return link.tinyurl.short(url)

                if __name__ == "__main__":
                    url = c
                    print(f"\n{shorten(url)}")
                    ipip = (f"\n{shorten(url)}")

                def printSomething():
                    label = Label(root, text= ipip)
                    label.pack()
                    speak(ipip)

                def web():
                    pyperclip.copy(ipip)
                    speak("url successful copy")

                def quit():
                    global root
                    root.destroy()
                    time.sleep(2)
                    root.quit()  

                root = Tk()
                button = Button(root, text="Show Me", command=printSomething) 
                button.pack()
                Button(root, text="Exit with this", command=quit).pack()
                Button(root, text="copy short url", command=web).pack()
                root.mainloop()
                commandhotword()

            elif re.search("link shorter", query) or re.search("short my link", query):

                speak("i am started shorter engine")
                import socket as s
                speak("i will show you input box ! please paste URL or linj here")
                ROOT = tk.Tk()
                ROOT.withdraw()
                USER_INP = simpledialog.askstring(title="URL",
                                                prompt="Paste URL here:")
                print("IP : ", USER_INP)
                c=USER_INP
                host = c
                speak("your url is")
                speak(c)
                import pyshorteners

                def shorten(url):
                    link = pyshorteners.Shortener()
                    return link.tinyurl.short(url)

                if __name__ == "__main__":
                    url = c
                    print(f"\n{shorten(url)}")
                    ipip = (f"\n{shorten(url)}")

                def printSomething():
                    label = Label(root, text= ipip)
                    label.pack()
                    speak(ipip)

                def web():
                    pyperclip.copy(ipip)
                    speak("url successful copy")

                def quit():
                    global root
                    root.destroy()
                    time.sleep(2)
                    root.quit()  

                root = Tk()
                button = Button(root, text="Show Me", command=printSomething) 
                button.pack()
                Button(root, text="Exit with this", command=quit).pack()
                Button(root, text="copy short url", command=web).pack()
                root.mainloop()
                commandhotword()

            elif re.search("my surveillance camera",query) or re.search("open my surveillance camera",query):
                try:
                    speak("please ! make sure laptop or pc connect with your phone hotspot")
                    speak("please wait ! i am starting surveillance camera on your pc")
                    time.sleep(3)
                    speak("please set on mind ! camera exit way only manualy")
                    speak("for exit surveillance camera press Q button from your keyboard")
                    cap = cv2.VideoCapture('https://192.168.43.1:8080/video')
                    while(True):
                        ret, frame = cap.read()
                        cv2.imshow('frame',frame)
                        if cv2.waitKey(1) & 0xFF == ord('q'):
                            speak("surveillance camera exit")
                            break

                    cap.release()
                    cv2.destroyAllWindows()
                except:
                    speak("something went worng! check ip camera is open and  also check ip address")

            elif re.search("surveillance camera",query) or re.search("open surveillance camera",query):
                try:
                    speak("please ! make sure laptop or pc connect with your phone hotspot")
                    speak("please wait ! i am starting surveillance camera on your pc")
                    time.sleep(3)
                    speak("please set on mind ! camera exit way only manualy")
                    speak("for exit surveillance camera press Q button from your keyboard")
                    ROOT = tk.Tk()
                    ROOT.withdraw()
                    USER_INP = simpledialog.askstring(title="URL",
                                                    prompt="Paste IP here:")
                    print("IP : ", USER_INP)
                    c=USER_INP
                    d="https://"+c+'/video'
                    cap = cv2.VideoCapture(d)

                    while(True):
                        ret, frame = cap.read()
                        cv2.imshow('frame',frame)
                        if cv2.waitKey(1) & 0xFF == ord('q'):
                            break

                    cap.release()
                    cv2.destroyAllWindows()
                
                except:
                    speak("something went worng! check ip camera is open and  also check ip address")




            else:
                speak("tell me help for support")
                
        elif 'exit' in hotword:
            speak("Good Bye")
            exit()
        
        elif 'lock' in hotword or 'maya lock' in hotword:
            speak("Locking Windows")
            ctypes.windll.user32.LockWorkStation()
        
        elif re.search('lock', hotword) or re.search('maya lock', hotword):
            speak("Locking Windows")
            ctypes.windll.user32.LockWorkStation()
        
        elif re.search('lock maya', hotword) or re.search('windows lock', hotword):
            speak("Locking Windows")
            ctypes.windll.user32.LockWorkStation()
        
        elif 'good morning' in hotword or 'good morning maya' in hotword:
            d = 'Good Morning','Good morning Abhishek'
            speak(random.choice(d))
        
        elif 'good afternoon' in hotword or 'good afternoon maya' in hotword:
            d = 'Good afternoon','Good afternoon Abhishek'
            speak(random.choice(d))

        elif 'good evening' in hotword or 'good evening maya' in hotword:
            d = 'Good evening','Good evening Abhishek'
            speak(random.choice(d))

        elif  'who are you' in hotword:
            webbrowser.open('maya.gif')
            speak("i am Maya human interaction program Develop By Abhishek Patel and i am work with Python")
