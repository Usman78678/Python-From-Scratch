# Text to Speech Conversion using pyttsx3

import pyttsx3 # pip install pyttsx3
engine = pyttsx3.init() # object creation

# For Mac, If you face error related to "pyobjc" when running the `init()` method :
# Install 9.0.1 version of pyobjc : "pip install pyobjc>=9.0.1"

engine.say('''Twinkle, twinkle, little star, how I wonder what you are. Up above the world so high,    
Twinkle, twinkle little star, how I wonder what you
are.''')
engine.runAndWait()