#import library
import sys
import time
import psutil
import speedtest
import speech_recognition as sr 
import playsound  
from gtts import gTTS  
import random
import win32api
import pywhatkit
import datetime
import webbrowser
import pyautogui
import os   
import wikipedia
import json
import pyttsx3
import smtplib
import requests
from pytube import Search

#define function class person
class person:
    name = ''
    #define function name of person 
    def setName(self, name):
        self.name = name

#define function class assistant
class assistant:
    name = ''
    #define function name of person 
    def setName(self, name):
        self.name = name

#define function to list text message on audio speak
# def audio_exists(terms):
#     for term in terms:
#         if term in voice_db:
#             return True
def audio_exists(terms, voice_db):
    for term in terms:
        if term in voice_db:
            return True

#define function engine audio speak
def audio_speak(text):
    txt = str(text)
    engine.say(txt)
    engine.runAndWait()

#generate speech recognition
recognition = sr.Recognizer()

#define function for listen audio to convert text
def audio_record(ask = False):
    with sr.Microphone() as source:
        print('Listening...')
        audio_listen = recognition.listen(source, 5, 5)
        voice_db = ''

        try:
            voice_db = recognition.recognize_google(audio_listen)
        except sr.UnknownValueError:
            print('I am sorry Sir, I did not understand what you said. Can you please repeat again!')
        except sr.RequestError:
            print('I am sorry Sir, my server is going down')
        print(voice_db)
        return voice_db


#define function for get string of audio file 
def audio_speak(audio_string):
    audio_string = str(audio_string)
    google_text = gTTS(text = audio_string, lang = 'en')
    r = random.randint(1, 2000000)
    file = 'audio' + str(r) + '.mp3'
    google_text.save(file)
    playsound.playsound(file)
    print(assistantObj.name + ':', audio_string)
    os.remove(file)

#define function to send email
def audio_email(to, content):
    import smtplib
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('coldlavolcano@gmail.com', 'Cold0lava@volcano')
        server.sendmail('coldlavolcano@gmail.com', to, content)
        server.close()
        print("Email sent successfully!")
    except Exception as e:
        print("Failed to send email:", e)
#define function to start the conversation
def audio_greet():
    hour = datetime.datetime.now().hour
    if hour >= 1 and hour < 12:
        audio_speak('Good morning!')
    elif hour >= 12 and hour < 18:
        audio_speak('Good afternoon!')
    elif hour >= 18 and hour < 24:
        audio_speak('Good evening!')
    audio_speak('Please tell me how can i help you Sir!')

#define function to present about news
def audio_news():
    api_key = 'pub_41872abf99a241b395e356cd34abe52154dbc'
    news_url = 'https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=' + api_key
    try:
        response = requests.get(news_url)
        if response.status_code == 200:
            news_json = response.json()
            news = []
            articles = news_json.get('articles', [])
            for i in range(min(5, len(articles))):  # Safely loop up to 5 articles or the number available
                title = articles[i].get('title', 'No Title Available')
                news.append('Headline ' + str(i + 1) + ': ' + title + '.')
            return news
        else:
            return ["Failed to retrieve news: " + str(response.status_code)]
    except requests.RequestException as e:
        return ["Error retrieving news: " + str(e)]
#define funtion to search in youtube    
def search_youtube(query):
    # Create a Search object using the query
    s = Search(query)
    # Fetching the results
    results = s.results  # This is a list of YouTube video objects
    # Check if there are any results
    if results:
        # Select the first video from the results
        first_video = results[0]
        # Print video details
        # print(f"Opening the first result:")
        # print(f"Title: {first_video.title}")
        
        audio_speak(f"Opening the first result:")
        audio_speak(f"Title: {first_video.title}")
        print(f"URL: {first_video.watch_url}")
        # Open the first result in the default web browser
        webbrowser.open(first_video.watch_url)

#generate function class person and assistant
personObj = person()
assistantObj = assistant()
assistantObj.name = 'Nova'
engine = pyttsx3.init()

#define function to response the audio
def audio_response(voice_db):
    if audio_exists(['search weather for'], voice_db):
        api_key = '8fffa32219944ae0b5f95259241204'
        base_url = 'https://api.openweathermap.org/data/2.5/weather?'
        audio_speak('Where is the city?')
        city_name = audio_record()
        complete_url = base_url + "appid=" + api_key + "&q=" + city_name
        response = requests.get(complete_url)
        x = response.json()

        if x['cod'] != '404':
            y = x['main']
            temp = round(y['temp'] - 273)
            humidity = y['humidity']
            z = x['weather']
            description = z[0]['description']
            audio_speak('Currently in ' + city_name + ' temperature is ' + str(temp) + ' degrees celcius' + '\n humidity in percentage is ' + 
                        str(humidity) + ' percent' + '\n the condition is ' + str(description))
            print('Currently in ' + city_name + ' temperature is ' + str(temp) + ' degrees celcius' + '\n humidity in percentage is ' + 
                  str(humidity) + ' percent' + '\n the condition is ' + str(description))
    
    elif audio_exists(['current news'], voice_db):
        arr_news = audio_news()
        for news_item in arr_news:
            audio_speak(news_item)
    #       
    elif audio_exists(['what time it is'], voice_db):
        time = datetime.datetime.now().strftime('%I:%M %p')
        audio_speak('Current time is ' + time)
    #
    elif audio_exists(['tell me the location'], voice_db):
        audio_speak('What is the location?')
        location = audio_record()
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        audio_speak('Here is the location ' + location)
        
    elif audio_exists(['show my system'], voice_db):
        system_path = "C:\Program Files (x86)\MSI\Dragon Center\Dragon Center.exe"
        audio_speak('starting monitoring system')
        os.startfile(system_path)
    #
    elif audio_exists(['show internet speed'], voice_db):
        speed_test = speedtest.Speedtest()
        dowload = round(speed_test.download(), 2)
        upload = round(speed_test.upload(), 2)
        audio_speak(f'The internet have {dowload} bit per second downloading speed and {upload} bit per second uploading speed')
    #
    elif audio_exists(['show battery percent'], voice_db):
        power_battery = psutil.sensors_battery()
        battery_percentage = power_battery.percent
        audio_speak(f'The system have {battery_percentage} percent battery')
    #Send Email not working
    elif audio_exists(['send email for'], voice_db):
        try:
            audio_speak('What should I say?')
            content = audio_record()
            to = 'riskysecure@gmail.com'    
            audio_email(to, content)
            audio_speak('Email has been sent Sir')
        except Exception as e:
            print(e)
            audio_speak('Sorry your friend willi bayu. I am not able to send this email') 
    
    elif audio_exists(['play music'], voice_db):
        music_dir = "D:\\Music"
        songs = os.listdir(music_dir)
        print(songs)    
        audio_speak('Yes Sir! please wait')
        os.startfile(os.path.join(music_dir, songs[0]))
    #
    elif audio_exists(['play movie'], voice_db):
        movie_dir = "D:\\Movies"
        movies = os.listdir(movie_dir)
        print(movies)
        audio_speak('Yes Sir! please wait')
        os.startfile(os.path.join(movie_dir, movies[0]))
    #    
    elif audio_exists(['open discord'], voice_db):
        discord = "C:\\Users\\suyog\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Discord Inc\\Discord.lnk"
        audio_speak('starting discord app')
        os.startfile(discord)
    #
    elif audio_exists(['open spotify'], voice_db):
        spotify_path = "C:\\Users\\suyog\\AppData\\Roaming\\Spotify\\Spotify.exe"
        try:
            audio_speak('Starting Spotify app...')
            os.startfile(spotify_path)
        except Exception as e:
            audio_speak('Failed to open Spotify')
    elif audio_exists(['open whatsapp'], voice_db):
        spotify_path = "C:\\Users\\suyog\\AppData\\Roaming\\Spotify\\Spotify.exe"
        try:
            audio_speak('Starting Spotify app...')
            os.startfile(spotify_path)
        except Exception as e:
            audio_speak('Failed to open Spotify')
    #   
    elif audio_exists(['volume up'], voice_db):
        pyautogui.press('volumeup')
    #
    elif audio_exists(['volume down'], voice_db):
        pyautogui.press('volumedown')
    #
    elif audio_exists(['mute'], voice_db):
        pyautogui.press('volumemute')

    elif audio_exists(['take screenshot'], voice_db):
        screenshot = pyautogui.screenshot()
        screenshot.save('screenshot.png')
    #
    elif audio_exists(['who is'], voice_db):
        person = voice_db.split('for')[-1]
        info = wikipedia.summary(person, sentences = 2)
        audio_speak(info)
    #
    elif audio_exists(['search for'], voice_db):
        search = voice_db.split('for')[-1]
        url = 'http://www.google.com/search?q=' + search
        webbrowser.get().open(url)
        audio_speak('Hello Sir Here is what I found for ' + search + 'on google!')
    # elif audio_exists(['send whatsapp message']):

    elif audio_exists(['search on YouTube'], voice_db):
        toSearch = voice_db.replace('search ', '').split(' on YouTube')[0]
        search_youtube(toSearch)

    
    elif audio_exists(['thanks'], voice_db):
        audio_speak('you are welcome Sir. See you later!')
        sys.exit(0)
    


#generate function start the conversation
audio_greet()

#define function to record the audio
while (1):
    time.sleep(5)
    voice_db = audio_record('Recording...')
    print('Q:', voice_db)
    audio_response(voice_db)
