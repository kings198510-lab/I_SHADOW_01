import pyjokes

joke = pyjokes.get_joke()
print("Here's a joke for you:")
print(joke)

print('''
Twinkle twinkle little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.
''')

import pyttsx3
engine = pyttsx3.init()
engine.say("this is a text to speech!")
engine.runAndWait()



