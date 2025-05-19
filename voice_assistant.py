import speech_recognition as sr  # For converting speech to text
import pyttsx3  # For converting text to speech
import datetime  # For getting current time and date
import wikipedia  # For searching Wikipedia
import webbrowser  # For opening web browser
import os
import time
import requests
from dotenv import load_dotenv  # For loading environment variables

# Load environment variables from .env file (if any)
load_dotenv()

class VoiceAssistant:
    """
    A simple voice assistant that can perform basic tasks through voice commands.
    This class demonstrates the use of various Python libraries and basic programming concepts.
    """
    
    def __init__(self):
        """Initialize the voice assistant with text-to-speech and speech recognition"""
        # Initialize text-to-speech engine
        self.engine = pyttsx3.init()
        # Set speaking rate (words per minute)
        self.engine.setProperty('rate', 150)
        
        # Initialize speech recognition
        self.recognizer = sr.Recognizer()
        
        # Set voice properties (using default system voice)
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[0].id)
        
    def speak(self, text):
        """
        Convert text to speech and print it to console
        Args:
            text (str): The text to be spoken
        """
        print(f"Assistant: {text}")
        self.engine.say(text)
        self.engine.runAndWait()
        
    def listen(self):
        """
        Listen for voice commands using the microphone
        Returns:
            str: The recognized command in lowercase, or empty string if recognition fails
        """
        with sr.Microphone() as source:
            print("Listening...")
            # Adjust for ambient noise
            self.recognizer.adjust_for_ambient_noise(source)
            # Listen for audio input
            audio = self.recognizer.listen(source)
            
        try:
            # Use Google's speech recognition
            command = self.recognizer.recognize_google(audio).lower()
            print(f"User said: {command}")
            return command
        except sr.UnknownValueError:
            self.speak("Sorry, I didn't catch that. Could you repeat?")
            return ""
        except sr.RequestError:
            self.speak("Sorry, there was an error with the speech recognition service.")
            return ""
            
    def get_time(self):
        """Get and speak the current time"""
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        self.speak(f"The current time is {current_time}")
        
    def get_date(self):
        """Get and speak the current date"""
        current_date = datetime.datetime.now().strftime("%B %d, %Y")
        self.speak(f"Today is {current_date}")
        
    def search_wikipedia(self, query):
        """
        Search Wikipedia for information
        Args:
            query (str): The topic to search for
        """
        try:
            self.speak("Searching Wikipedia...")
            # Get a summary of the topic (2 sentences)
            results = wikipedia.summary(query, sentences=2)
            self.speak("According to Wikipedia:")
            self.speak(results)
        except Exception as e:
            self.speak("Sorry, I couldn't find that information on Wikipedia.")
            
    def search_web(self, query):
        """
        Search the web using Google
        Args:
            query (str): The search query
        """
        search_url = f"https://www.google.com/search?q={query}"
        webbrowser.open(search_url)
        self.speak(f"Here's what I found for {query}")
        
    def process_command(self, command):
        """
        Process the voice command and perform appropriate action
        Args:
            command (str): The voice command to process
        Returns:
            bool: False if the command is to exit, True otherwise
        """
        if "hello" in command:
            self.speak("Hello! How can I help you today?")
            
        elif "time" in command:
            self.get_time()
            
        elif "date" in command:
            self.get_date()
            
        elif "search for" in command:
            # Extract the search query from the command
            query = command.replace("search for", "").strip()
            self.search_web(query)
            
        elif "tell me about" in command:
            # Extract the topic from the command
            query = command.replace("tell me about", "").strip()
            self.search_wikipedia(query)
            
        elif "exit" in command or "quit" in command:
            self.speak("Goodbye!")
            return False
            
        return True
        
    def run(self):
        """Main loop for the voice assistant"""
        self.speak("Hello! I'm your voice assistant. How can I help you?")
        
        running = True
        while running:
            command = self.listen()
            if command:
                running = self.process_command(command)
                
if __name__ == "__main__":
    # Create and run the voice assistant
    assistant = VoiceAssistant()
    assistant.run() 