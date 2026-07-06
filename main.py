import speech_recognition as sr
import pyttsx3
import webbrowser
import musicLibrary
from openai import OpenAI



recognizer = sr.Recognizer()
engine = pyttsx3.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()
    

def aiProcess(command):
    client = OpenAI(api_key="sk-ijklmnopqrstuvwxijklmnopqrstuvwxijklmnop")

    response = client.responses.create(
        model = ("gpt-5.5"),
        input = command
    )

    return (response.output_text)


def processCommand(c):
    if "open" or "google" in c.lower():
        webbrowser.open("https://google.com/")
    
    elif "instagram" in c.lower():
        webbrowser.open("https://www.instagram.com/")
    
    elif "play" or "thermometer" in c.lower():
        webbrowser.open("https://www.youtube.com/watch?v=rJgNgZRCi6s&list=RDrJgNgZRCi6s&start_radio=1")
    
    elif "linkedin" or "kholo" or "open" in c.lower():
        webbrowser.open("https://www.linkedin.com/feed/")
    
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com/")
    
    elif c.lower().startwith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music(song)
        webbrowser.open(link)
    
    else:
        # Let openAI handle the rest
        output = aiProcess()
        speak(output)



if __name__ == "__main__":
    speak("...Starting jarvis...")
    while True:
        r = sr.Recognizer()
        print("Recognizing...")
        try:
            # Listen for the wake word 'Jarvis'
            # Obtain audio from the microphone 
            with sr.Microphone() as source:
                print("Listening...")
                # r.adjust_for_ambient_noise(source, duration=5)
                audio = r.listen(source , timeout=2 , phrase_time_limit=1)
                
            word = r.recognize_google(audio)
            if word.lower() == "jarvis":
                print("Recognized: ", word)
                speak("Yes sir")
            
                # recognize command using Google Speech Recognition
                with sr.Microphone() as source:
                    print("Jarvis active...")
                    # r.adjust_for_ambient_noise(source, duration=5)
                    audio = r.listen(source, timeout=2, phrase_time_limit=1)
                    command = r.recognize_google(audio)

                                        
                            
        
        except Exception as e:
            print(type(e).__name__)
            print(e)
            