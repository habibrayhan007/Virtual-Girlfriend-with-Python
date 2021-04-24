import speech_recognition as sr
from gtts import gTTS
import pyaudio
import pyttsx3
import playsound
import os
import datetime
import calendar
import wikipedia
import webbrowser
import weathercom
import json
import pywhatkit as kit

r = sr.Recognizer()




def voice_command_processor(say_something=False):
    with sr.Microphone() as source:
        if (say_something):
            audio_playback(say_something)
        print("Say Something:")
        audio = r.listen(source)

        # use google speech recognizition
        text = ''
        try:
            text = r.recognize_google(audio)
            print("You said:" + text)
        except sr.UnknownValueError:
            print("I could not understand your voice")
        except sr.RequestError as e:
            print("Request result from google speech recognization service error" + e)
        return text.lower()


# Audio Output
def audio_playback(text):
    fileName = 'test.mp3'
    tts = gTTS(text=text, lang='en')
    tts.save(fileName)
    playsound.playsound(fileName)
    os.remove(fileName)


# executing voice command
def execute_voice_command(text):
    if 'ok' in text:

        audio_playback('Ok, Thank You')

    elif 'what is your name' in text:

        audio_playback('You know already. Its a public place so I can not tell')

    elif 'who are you' in text:

        audio_playback('I am the one and only girlfriend of habib rayhan')

    elif 'do you love music' in text:

        audio_playback('Yes, of course. I love music so much')

    elif 'what can you do' in text:

        audio_playback('I can only help people with information')

    elif 'do you know everything' in text:

        audio_playback('No. I can give as much information as Habib has given me access')

    elif "what is the today's date" in text:
        get_date = getdate()
        audio_playback(get_date)

    elif "what is the today's weather" in text:
        print("which city?")
        city = voice_command_processor("which city")
        humidity, temp, phrase = weatherReport(city)
        audio_playback("currently in " + city + "  temperature is " + str(temp)
                       + " degree celsius, " + "humidity is " + str(humidity) + " percent and sky is " + phrase)


    elif "search google" in text:

        search = voice_command_processor("what do you want to search")
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)

    elif "search youtube" in text:
        search = voice_command_processor("what do you want to search")
        url = 'https://youtube.com/search?q=' + search
        webbrowser.get().open(url)


    elif "find location" in text:

        location = voice_command_processor("which location?")
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)


    elif 'this is almost 2 a.m.' in text:

        audio_playback("Yeah. I know. what do you want from me in this late night")

    elif 'sing a song for me' in text:
        print("Okey baby.")
        audio_playback("okey baby")
        os.system('start janu.m4a')

    elif 'play a song for me' in text:
        son = voice_command_processor("Which song")
        kit.playonyt(son)


# define Date time
def getdate():
    now = datetime.datetime.now()
    my_date = datetime.datetime.today()
    weekday = calendar.day_name[my_date.weekday()]
    monthNum = now.month
    dayNum = now.day

    # list of month
    month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                   'November', 'December']

    # list of ordinal number
    ordinalNumbers = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th', '10th', '11th', '12th', '13th',
                      '14th', '15th',
                      '16th', '17th', '18th', '19yh', '20th', '21st', '22nd', '23rd', '24th', '25th', '26th', '27th',
                      '28th',
                      '29th', '30th', '31st']
    return 'Today is ' + weekday + ', the ' + ordinalNumbers[dayNum - 1] + ' ' + month_names[monthNum - 1] + '.'


# define wether report
def weatherReport(city):
    weatherDetails = weathercom.getCityWeatherDetails(city)
    humidity = json.loads(weatherDetails)["vt1observation"]["humidity"]
    temp = json.loads(weatherDetails)["vt1observation"]["temperature"]
    phrase = json.loads(weatherDetails)["vt1observation"]["phrase"]
    return humidity, temp, phrase


while True:
    command = voice_command_processor()

    execute_voice_command(command)
