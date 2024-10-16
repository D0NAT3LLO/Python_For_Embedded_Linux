import webbrowser
import os
import speech_recognition as sr
from datetime import datetime
import pyttsx3

recognizer= sr.Recognizer()
engine = pyttsx3.init()
def speak(text):
        engine.say(text)
        engine.runAndWait()

def listen():
        with sr.Microphone() as source :
            recognizer.adjust_for_ambient_noise(source)
            print("Listening...")
            audio = recognizer.listen(source)
            try:
                command = recognizer.recognize_google(audio)
                print(f"You said = {command} ")
                return command.lower()
            except sr.UnknownValueError:
                  speak("Sorry, I did not get that. ")
                  return ""
            except sr.RequestError:
                  speak("I didnot connect properly to the Internet. ")
                  return ""
            
def open_website(site):
    websites = {
        "facebook": "https://www.facebook.com",
        "twitter": "https://www.twitter.com",
        "instagram": "https://www.instagram.com",
        "youtube": "https://www.youtube.com",
    }
    if site in websites:
          webbrowser.open(websites[site])
          speak(f"Opening {site}  ")
    else:
          speak("Trouble opening the site. Please try again !") 

def open_folder(folder_path):
    if os.path.exists(folder_path):
            os.startfile(folder_path)  # Use 'xdg-open' on Linux/Mac
            speak(f"Opening the folder whose path is {folder_path}")
    else:
            speak(f"Sorry, I did not found the folder")

def process_command(command):
    if "time" in command:
            current_time = datetime.now().strftime("%H:%M")
            speak(f"the time right now is {current_time}")
            print(f"Current time is {current_time}")

    elif "open" in command and "facebook" in command:
          open_website("facebook")    
    elif "open" in command and "instagram" in command:
            open_website("instagram")   
    elif "open" in command and "twitter" in command:
            open_website("twitter")   
    elif "open" in command and "youtube" in command:
            open_website("youtube")    
    elif "open folder" in command :
        folder_path = r"D:\UNICORN"
        open_folder(folder_path)
    elif "thank you" in command:
          speak("You are welcome, anything else to assist you with?")
    else:
        speak("Sorry,I didnot get the command.")

def main():
        speak("Hello, How may I assist you today?")
        while True:
                command = listen()
                if "exit" in command or "quit" in command:
                        speak("Goodbye!")
                        break
                else:
                        process_command(command)

if __name__ == "__main__":
    main()