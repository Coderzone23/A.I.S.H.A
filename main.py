import os
import eel

from engine.features import playAssistantsound  # Import the correct function
from engine.command import*
# Initialize the Eel app
eel.init("www")

# Call the function with the correct name
playAssistantsound()

# Launch the browser with the correct URL
os.system('start msedge.exe --app="http://localhost:8000/index.html"')

# Start the Eel web application
eel.start('index.html', mode=None, host='localhost', block=True)
