
from tkinter import *
import tkinter as tk
from bs4 import BeautifulSoup
import pywhatkit
import requests
import wikipedia as wp
import pyttsx3
import speech_recognition as sr
import webbrowser

from spotipy.oauth2 import SpotifyClientCredentials

def clear_text(event):
    search_entry.delete(0, "end")
    
    
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 170)


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1  
        audio = r.listen(source)

    try:
          print("Recognizing")
          query = r.recognize_google(audio, language='en-in')
          print("user said: {query}\n")
    except Exception as e:
         #print(e)

         print("say that again please...")
         speak("say that again please...")
         return "None"
    return query





def tohid():
    query = takecommand().lower()
    if "google" in query:
        speak('searching on google...')
        query = query.replace("google", "")
        search_url = "https://www.google.com/search?q=" + query
        results = requests.get(search_url)
        soup = BeautifulSoup(results.text, 'html.parser')
        search_results = soup.find_all('div', class_='BNeawe s3v9rd AP7Wnd')
        limit = 3  # set the limit to 3 sentences
        count = 0
        for i in search_results:
            if count == limit:
                break
            print(i.get_text())
            speak(i.get_text())
            count += 1


    
    


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1  
        audio = r.listen(source)

    try:
          print("Recognizing")
          query = r.recognize_google(audio, language='en-in')
          print("user said: {query}\n")
    except Exception as e:
         #print(e)

         print("say that again please...")
         speak("say that again please...")
         return "None"
    return query

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def search():
    # song = search_entry.get()
    # pywhatkit.playonyt(song)
    search_song = search_entry.get()
    pywhatkit.playonyt(search_song)
    
    
def wikipedia_search():
    search_query = search_something.get()
    summary = wp.summary(search_query, sentences=3)
    print(summary)
    speak(summary)
    
def resso2():
    query = takecommand().lower()
    if "play" in query and "song" in query:
        speak("What song would you like to play?")
        song = takecommand().lower()
        search_url = "https://m.resso.app/search/posts/?page=1&keyword=" + song
        webbrowser.open(search_url)


root = tk.Tk()
root.geometry("700x500")
root.title("THE DISCOVERER")

# Load the background image file
bg_image = tk.PhotoImage(file="pro2.png")

# Create a label to display the background image
bg_label = tk.Label(root, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Add the other widgets on top of the background image
search_label = tk.Label(root,text="Enter song name:", bg="black",foreground="white")
search_label.place(x=320, y=140)


search_entry = tk.Entry(root, width=40)
search_entry.place(x=250, y=170)



# Bind the function to the Entry widget

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++
# speak=(search_entry)

play_button = tk.Button(root, text="Play", command=search)
play_button.place(x=350, y=200)

search_label = tk.Label(root,text="Enter to search on wikipedia:", bg="black",foreground="white")
search_label.place(x=300, y=240)
search_something = tk.Entry(root, width=40)
search_something.place(x=250, y=270)
# speak=(search_something)

search_wiki_button = tk.Button(root, text="search_wiki", command=wikipedia_search)
search_wiki_button.place(x=330, y=300)


search_wiki_button = tk.Button(root, text="search", command=tohid)
search_wiki_button.place(x=40, y=30)

search_wiki_button = tk.Button(root, text="resso", command=resso2)
search_wiki_button.place(x=40, y=60)

root.mainloop()
