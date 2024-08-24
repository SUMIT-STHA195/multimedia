import pyttsx3

# Initialize the pyttsx3 text-to-speech engine
engine = pyttsx3.init()

# Set the speaking rate (speed of speech)
engine.setProperty('rate', 100)  # 100 words per minute

# Set the volume level (0.0 to 1.0)
engine.setProperty('volume', 3)  # Note: The volume value should be between 0.0 and 1.0. 3 is too high and may cause issues. Consider changing it to 1.0 for max volume.

# Define the text to be spoken
text = "hello, I am Sumit Shrestha"

# Make the engine say the text
engine.say(text)

# Run the speech engine and wait until the speech is finished
engine.runAndWait()
