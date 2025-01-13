from playsound import playsound
import eel

@eel.expose
def playAssistantsound():
    # Use raw string to avoid issues with escape characters in file path
    music_dir = r"www\\assets\\audio\\start_sound.mp3"
    playsound(music_dir)
