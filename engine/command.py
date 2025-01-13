import pyttsx3
import speech_recognition as sr
import eel

def speak(text):
    engine = pyttsx3.init()  # Initialize text-to-speech engine
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # Use female voice (index 1)
    engine.setProperty('rate', 160)  # Set speech rate
    print(voices)  # Print available voices
    engine.say(text)  # Convert text to speech
    engine.runAndWait()  # Wait until the speech is finished

@eel.expose
def takecommand():  # Ensure the function name matches here
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        eel.DisplayMessage('Listening...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        try:
            audio = r.listen(source, timeout=10, phrase_time_limit=6)
            print('Recognizing...')
            eel.DisplayMessage('Recognizing...')
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}")
            eel.DisplayMessage(query)
            speak(query)
            eel.ShowHood()
        except Exception as e:
            print("Error recognizing speech:", e)
            return ""
    return query.lower()

    @eel.expose
    def allComand():

        query = takecommand


