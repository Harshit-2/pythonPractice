import psutil
import pyautogui
import pyttsx3  # pip install pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import json
import os
import cv2  # camera library
import smtplib
import random
import pywhatkit as kit
from requests import get
import time  # time library
import pyjokes
from requests import get
import requests
from bs4 import BeautifulSoup
import sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.encoders import encode_base64
import geocoder
import instadownloader
import PyPDF2
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QObject, QTimer, QTime, QDate, QtMsgType
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from Cipher_GUI import Ui_MainWindow
import re


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")

    elif 12 <= hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("Sir, I am Cipher. Please tell me how may I help you")

def get_news_headlines():
    url = "https://newsapi.org/v2/top-headlines?country=us&apiKey=8969ef45f64047d1a83d74eb19504c9d"
    response = requests.get(url)
    data = json.loads(response.text)

    speak("Here are the top headlines today:")
    for index, article in enumerate(data["articles"][:5]):
        speak(str(index + 1) + ". " + article["title"])

def perform_calculation(self):
    speak("Which operation would you like to perform?")
    operation = self.takeCommand()

    if operation in ["addition", "sum", "plus"]:
        speak("Please provide the numbers to add.")
        expression = self.takeCommand()
        match = re.search(r"(\d+) (?:and|plus) (\d+)", expression)
        if match:
            num1 = float(match.group(1))
            num2 = float(match.group(2))
            result = num1 + num2
            speak("The sum is " + str(result))
        else:
            speak("Sorry, I couldn't understand the numbers to add.")

    elif operation in ["subtraction", "minus"]:
        speak("Please provide the numbers for subtraction.")
        expression = self.takeCommand()
        match = re.search(r"(\d+) (?:minus|subtract) (\d+)", expression)
        if match:
            num1 = float(match.group(1))
            num2 = float(match.group(2))
            result = num1 - num2
            speak("The difference is " + str(result))
        else:
            speak("Sorry, I couldn't understand the numbers for subtraction.")

    elif operation in ["multiplication", "multiply", "times"]:
        speak("Please provide the numbers to multiply.")
        expression = self.takeCommand()
        match = re.search(r"(\d+) (?:times|multiply) (\d+)", expression)
        if match:
            num1 = float(match.group(1))
            num2 = float(match.group(2))
            result = num1 * num2
            speak("The product is " + str(result))
        else:
            speak("Sorry, I couldn't understand the numbers to multiply.")

    elif operation in ["division", "divide"]:
        speak("Please provide the numbers for division.")
        expression = self.takeCommand()
        match = re.search(r"(\d+) (?:divided by) (\d+)", expression)
        if match:
            num1 = float(match.group(1))
            num2 = float(match.group(2))
            if num2 != 0:
                result = num1 / num2
                speak("The quotient is " + str(result))
            else:
                speak("Sorry, cannot divide by zero.")
        else:
            speak("Sorry, I couldn't understand the numbers for division.")

    else:
        speak("Sorry, I didn't recognize the operation.")



def getPNRStatus():
    pnr = "2741819259" # PNR number of the ticket to be checked
    url = "https://www.indianrail.gov.in/enquiry/PNR/PnrEnquiry.html?locale=en"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    response = requests.post(url, data={"inputPnrNo": pnr}, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    result = soup.find_all("td", {"class": "table_border_both"})
    if len(result) == 0:
        speak("Invalid PNR number")
        return
    else:
        status = result[10].text.strip()
        speak("PNR status is " + status)

# def news():
#     main_url= 'https://newsapi.org/v2/everything?q=tesla&from=2023-04-10&sortBy=publishedAt&apiKey=8969ef45f64047d1a83d74eb19504c9d'
#     main_page = requests.get(main_url).json()
#     articles = main_page["articles"]
#     head = []
#     day = {"first","second","third","fourth","fifth","sixth","seventh","eighth","ninth","tenth"}
#     for ar in articles:
#         head.append(ar["title"])
#     for i in range(len(day)):
#         speak(f"Today's {day[i]} news is: {head[i]}")



def getLocation():
    # get location
    g = geocoder.ip('me')
    lat_lng = g.latlng

    # get address from latitude and longitude
    address = geocoder.osm(lat_lng, method='reverse')

    # print address
    print(f"Your current location is {address.address}")
    speak(f"Your current location is {address.address}")

class MainThread(QThread):

    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        self.TaskExecution()


    def pdf_reader():
        book = open('phase3_final.pdf', 'rb')
        pdfReader = PyPDF2.PdfFileReader(book)
        pages = pdfReader.numPages
        speak(f"The total number of pages in this file are {pages}")
        speak("Please tell me the page number I have to read")
        pg = int(input("Enter the page number: "))
        page = pdfReader.getPage(pg)
        text = page.extractText()
        speak(text)

    
    def takeCommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("listeninig...")
            r.pause_threshold = 1
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")

        except Exception as e:
            # print(e)
            print("Say that again please...")
            return "none"
        return query


    def TaskExecution(self):
        wishMe()
        while True:

            self.query = self.takeCommand().lower()

            if 'open notepad' in self.query:
                codePath = "C:\\Windows\\System32\\notepad.exe"
                os.startfile(codePath)

            elif "close notepad" in self.query:
                speak("okay sir, closing notepad")
                os.system("taskkill /f /im notepad")

            elif "open command prompt" in self.query:
                os.system("start cmd")

            elif "open camera" in self.query:
                cap = cv2.VideoCapture(0)
                while True:
                    ret, img = cap.read()
                    cv2.imshow('webcam', img)
                    k = cv2.waitKey(100)
                    if k == 27:
                        break
                    cap.release()
                    cv2.destroyAllWindows()

            elif 'play music' in self.query:
                music_dir = 'D:\\cipher\\music'
                songs = os.listdir(music_dir)
                for song in songs:
                    if song.endswith('.mp3'):
                        os.startfile(os.path.join(music_dir, song))

            elif "ip address" in self.query:
                ip = get('https://api.ipify.org').text
                speak(f"your IP adress is {ip}")

            elif 'wikipedia' in self.query:
                speak('Searching Wikipedia...')
                self.query = self.query.replace("wikipedia", "")
                results = wikipedia.summary(self.query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)

            elif 'open youtube' in self.query:
                webbrowser.open("youtube.com")

            elif 'browser' in self.query:
                webbrowser.open("google.com")

            elif 'stackoverflow' in self.query:
                webbrowser.open("stack overflow.com")

            elif "open google" in self.query:
                speak("sir, what should i search on google")
                cm = self.takeCommand().lower()
                webbrowser.open(f"{cm}")



            elif 'play song on youtube' in self.query:
                speak("Which song do you want me to play on YouTube?")
                song_name = self.takeCommand().lower()
                kit.playonyt(song_name)

            elif "what is time now" in self.query:
                speak("The time is {}.".format(datetime.now().strftime("%I:%M %p")))

            elif "set alarm" in self.query:
                nn = int(datetime.datetime.now().hour)
                if nn == 22:
                    music_dir = 'E:\\music'
                    songs = os.listdir(music_dir)
                    os.startfile(os.path.join(music_dir, songs[0]))

            elif "tell me a joke" in self.query:
                joke = pyjokes.get_joke()
                speak(joke)

            elif "shut down the system" in self.query:
                os.system("shutdown /s /t 5")

            elif "restart the system" in self.query:
                os.system("shutdown /r /t 5")

            elif "sleep the system" in self.query:
                os.system("rundll32.exe powrprof.dll, SetSuspendState 0,1,0")

            elif "switch the window" in self.query:
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                time.sleep(1)
                pyautogui.keyUp("alt")

            elif "tell me the news" in self.query:
                speak("Please wait sir, I am fetching the news...")
                get_news_headlines()
            elif "where i am" in self.query or "where we are" in self.query:
                speak("wait sir, let me check")
                try:
                    ipAdd = requests.get('https://api.ipify.org').text
                    print(ipAdd)
                    url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
                    geo_requests = requests.get(url)
                    geo_data = geo_requests.json()
                    city = geo_data['city']
                    country = geo_data['country']
                    speak(
                        f"sir i am not sure, but i think we are in {city} city of {country} country")

                except Exception as e:
                    speak(
                        "sorry sir, Due to network issue i am not able to find where we are.")
                    pass

            elif "instagram profile" in self.query or "profile on instagram" in self.query:
                # speak("sir please enter the user name correctly.")
                # name =self.takeCommand().lower()
                webbrowser.open(f"www.instagram.com/_abhishek_284_")
                speak(f"Sir here is the profile of you")
                time.sleep(5)
            elif "take a screenshot of this" in self.query or "take a screenshot" in self.query:
                speak("Sir, please tell me the name for this file")
                name = self.takeCommand().lower()
                speak("Please sir wait for a few seconds, I am taking the screenshot")
                time.sleep(3)
                img = pyautogui.screenshot()
                img.save(f"{name}.png")
                speak("Sir your screenshot has  been saved!")
            # elif "read pdf" in self.query:
            #     pdf_reader()

            elif "hide all files" in self.query or "hide this folder" in self.query or "visible for everyone" in self.query:
                speak("sir please tell me you want to hide this folder or make it visible for everyone")
                condition = self.takeCommand().lower()

                if "hide" in condition:
                     os.system("attrib +h /s /d")
                     speak("sir, all the files in this folder are now hidden.")

                elif "visible" in condition:
                    os.system("attrib -h /s /d")
                    speak("sir, all the files in this folder are now visible to everyone")
                elif "leave it" in condition or "leave for now" in condition:
                    speak("Ok sir")

            elif 'pnr status' in self.query:
                getPNRStatus()

            elif  "do calculation" in self.query:
                perform_calculation(self)
                
                
                

startExecution = MainThread()


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie = QtGui.QMovie("G:\\cipher\\gui\Iron_Template_1.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("G:\\cipher\\gui\\AI assistant Cipher Logo.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("G:\\cipher\\gui\\initial.gif")
        self.ui.label_3.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("G:\\cipher\\gui\\load.gif")
        self.ui.label_4.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()

    def showTime(self):

        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt. ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_3.setText(label_time)

app = QApplication(sys.argv)
Cipher = Main()
Cipher.show()   
exit(app.exec_())



    # if __name__ == "__main__":
    #     TaskExecution()
