# Virtual Voice Assistant (NOVA)
<img src="https://github.com/Bayunova28/Navillera/blob/master/Benefits-of-Having-a-Virtual-Assistant.jpg" width="1100" height="450">

<p align="justify">Virtual assistants are intelligent software agents that their performance is attributed to voice command. Some virtual assistants use synthesized voices to interpret the voice of 
human and response to the voice. The mundane activities and tasks perform by human waste time and energy that would have been expended on something meaningful. This is common in 
routine scenario that calls for immediate response as found in some of our everyday tasks. The technology behind virtual assistants allows users to: ask the virtual assistants 
questions, control home automation devices, play media playback through voice and manage other basic tasks such as email, to-do lists, and calendars. For example, virtual 
assistants help in the office activities in the sense that some hundreds of e-mail messages that need to be answered which could not be humanly attended to can be answered through
the hiring of virtual assistants. Any business owner can get the stress from their daily activities. There are many administrative tasks that could be solved during the day to 
free up time and relieve stress, an assistant is needed who will help in a difficult situation.<p>

## Weather Mapping API
This project using [weather mapping API](https://openweathermap.org/api). Before you build this program, you must [register account](https://home.openweathermap.org/users/sign_in) for got the API. After that, you can choose these API :
```
api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
```
```
api.openweathermap.org/data/2.5/weather?q={city name},{state code}&appid={API key}
```
```
api.openweathermap.org/data/2.5/weather?q={city name},{state code},{country code}&appid={API key}
```

## News API
This project also using [news API](https://newsapi.org/). You must register account and [get API key](https://newsapi.org/register). After that you can choose some news from News API. Here are some news API:
```
https://newsapi.org/v2/everything?q=apple&from=2022-01-18&to=2022-01-18&sortBy=popularity&apiKey=
```
```
https://newsapi.org/v2/everything?q=tesla&from=2021-12-19&sortBy=publishedAt&apiKey=
```
```
https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=
```
```
https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=
```
```
https://newsapi.org/v2/everything?domains=wsj.com&apiKey=
```

## Control accesss to less secure apps
If you ran the program and got a gmail SMTP authentication error but your username or password was correct, check your problem [here](https://support.google.com/accounts/answer/6010255). This is step if you're using smtp.gmail.com :
* Turn on the less secure apps in [recent security activity](https://myaccount.google.com/u/1/security?utm_source=OGB&utm_medium=act)
* You'll get the security mail in your gmail inbox, Click 'Yes,it's me' in that.
* Now run your code again.

## Install Package
```python
pip install SpeechRecognition
pip install playsound
pip install gTTS
pip install random2
pip install pywin32
pip install pywhatkit
pip install DateTime
pip install wikipedia
pip install pyttsx3
pip install json
pip install requests
pip install smtplib
pip install psutil
pip install speedtest-cli
pip install pyautogui
```

## Setting up response of person and assistant
```python
class person:
    name = ''
    def setName(self, name):
        self.name = name

class assistant:
    name = ''
    def setName(self, name):
        self.name = name
```

## Setting up list of text message on audio
```python
def audio_exists(terms):
    for term in terms:
        if term in voice_db:
            return True
```

## Setting up audio to convert the text
```python
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
```

## Setting up start the conversation
```python
def audio_greet():
    hour = datetime.datetime.now().hour
    if hour >= 1 and hour < 12:
        audio_speak('Good morning!')
    elif hour >= 12 and hour < 18:
        audio_speak('Good afternoon!')
    elif hour >= 18 and hour < 24:
        audio_speak('Good evening!')
    audio_speak('Nova is online. Please tell me how can i help you Sir!')
```

## Setting up to send the email
```python
def audio_email(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()
```

## Setting up to present about the news
```python
def audio_news():
    api_key = 'your-api-key'
    news_url = 'https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=' + api_key
    news_json = requests.get(news_url).json()
    news = []

    for i in range(5):
        news.append('Headline ' + str(i + 1) + ', ' + news_json['articles'][i]['title'] + '.')
    return news
```

## Setting up to save the audio record
```python
def audio_speak(audio_string):
    audio_string = str(audio_string)
    google_text = gTTS(text = audio_string, lang = 'en')
    r = random.randint(1, 2000000)
    file = 'audio' + str(r) + '.mp3'
    google_text.save(file)
    playsound.playsound(file)
    print(assistantObj.name + ':', audio_string)
    os.remove(file)
```

## Setting up audio response the message
```python
def audio_response(voice_db):
    if audio_exists(['Nova search weather for']):
        api_key = 'your-api-key'
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
                  
    elif audio_exists(['Nova current news']):
        arr_news = audio_news()
        for i in range(len(arr_news)):
            audio_speak(arr_news[i])
            print(arr_news[i])
            
    elif audio_exists(['Nova what time is it']):
        time = datetime.datetime.now().strftime('%I:%M %p')
        audio_speak('Current time is ' + time)
    
    elif audio_exists(['Nova tell me the location']):
        audio_speak('What is the location?')
        location = audio_record()
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        audio_speak('Here is the location ' + location)
    
    elif audio_exists(['Nova show my system']):
        system_path = "YOUR LINK SYSTEM PATH"
        audio_speak('starting monitoring system')
        os.startfile(system_path)
    
     elif audio_exists(['Nova show internet speed']):
        speed_test = speedtest.Speedtest()
        dowload = round(speed_test.download(), 2)
        upload = round(speed_test.upload(), 2)
        audio_speak(f'The internet have {dowload} bit per second downloading speed and {upload} bit per second uploading speed')

    elif audio_exists(['Nova show power battery']):
        power_battery = psutil.sensors_battery()
        battery_percentage = power_battery.percent
        audio_speak(f'The system have {battery_percentage} percent battery')
    
    elif audio_exists(['Nova send email for']):
        try:
            audio_speak("What should I say? Sir")
            content = audio_record()
            to = 'youremail@gmail.com'    
            audio_email(to, content)
            audio_speak('Email has been sent Sir')
        except Exception as e:
            print(e)
            audio_speak('Sorry your friend willi bayu. I am not able to send this email') 
    
    elif audio_exists(['Nova play music']):
        music_dir = "YOUR LINK PATH MUSIC"
        songs = os.listdir(music_dir)
        print(songs)    
        audio_speak('Yes Sir! please wait')
        os.startfile(os.path.join(music_dir, songs[0]))
        
    elif audio_exists(['Nova play movie']):
        movie_dir = "YOUR LINK PATH VIDEO"
        movies = os.listdir(movie_dir)
        print(movies)
        audio_speak('Yes Sir! please wait')
        os.startfile(os.path.join(movie_dir, movies[0]))

    elif audio_exists(['Nova open Discord']):
        discord = "YOUR LINK PATH DISCORD"
        audio_speak('starting discord app')
        os.startfile(discord)

    elif audio_exists(['Nova open Spotify']):
        spotify = "YOUR LINK PATH SPOTIFY"
        audio_speak('starting spotify app')
        os.startfile(spotify)
        
    elif audio_exists(['Nova volume up']):
        pyautogui.press('volumeup')

    elif audio_exists(['Nova volume down']):
        pyautogui.press('volumedown')

    elif audio_exists(['Nova mute']):
        pyautogui.press('volumemute') 

    elif audio_exists(['Nova who is']):
        person = voice_db.split('for')[-1]
        info = wikipedia.summary(person, sentences = 5)
        audio_speak(info)
    
    elif audio_exists(['Nova search for']):
        search = voice_db.split('for')[-1]
        url = 'http://www.google.com/search?q=' + search
        webbrowser.get().open(url)
        audio_speak('Hello Sir Here is what I found for ' + search + 'on google!')
    
    elif audio_exists(['thank you']):
        audio_speak('you are welcome Sir. See you later!')
        sys.exit(0)

```
