import tkinter as tk
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import subprocess
import webbrowser
# Initialize the Tkinter window
root = tk.Tk()
root.title("BABU the Assistant")
dark_mode = tk.BooleanVar(value=False)


# Create a function to toggle dark modepip gui.py
def toggle_dark_mode():
    global dark_mode
    if dark_mode.get():
        # Dark mode
        root.configure(bg='black')
        response_text.config(bg='black', fg='white')
        start_button.config(bg='dark green', fg='black')
    else:
        # Light mode
        root.configure(bg='white')
        response_text.config(bg='white', fg='black')
        start_button.config(bg='green', fg='white')

# Create a button for toggling dark mode
dark_mode_button = tk.Checkbutton(root, text="Dark Mode", variable=dark_mode, command=toggle_dark_mode)
dark_mode_button.pack()
    
def listen_for_wake_word():
    while True:
        try:
            with sr.Microphone() as source:
                print('Listening for the wake word...')
                listener.adjust_for_ambient_noise(source)
                voice = listener.listen(source)
                command = listener.recognize_google(voice).lower()
                if 'hey babu' in command:
                    return True
        except sr.UnknownValueError:
            pass
        while True:
         if listen_for_wake_word():
          run_babu()
# Create a function to handle voice commands and responses
def run_babu():
   
      
    command = take_command()
    # Display the user's question on the left
    response_text.insert(tk.END, f'You: {command}\n')
    
    if 'play' in command:
        song = command.replace('play', '')
        response_text.insert(tk.END, f'Babu Sir: Playing {song}\n')  # play song
        talk(f'Playing {song} in youtube')
        pywhatkit.playonyt(song)
    #elif 'hi' or 'hello' in command:
       # response_text.insert(tk.END, 'Babu Sir: Hello, I\'m Babu, your personal assistant. How can I help you today?\n')
       # talk('Hello, I\'m Babu, your personal assistant. How can I help you today?')
    elif 'open notepad' in command:
        response_text.insert(tk.END, 'Babu Sir: Opening Notepad\n')  # notepad
        talk('Opening Notepad')
        subprocess.Popen([r'notepad.exe']) 
    elif 'open chrome' in command:
        response_text.insert(tk.END, 'Babu Sir: Opening Chrome\n')  # chrome
        talk('Opening Chrome')
        subprocess.Popen([r'C:\Program Files\Google\Chrome\Application\chrome.exe'])
    elif 'open calculator' in command:
        response_text.insert(tk.END, 'Babu Sir: Opening Calculator\n')  # calculator
        talk('Opening Calculator')
        subprocess.Popen([r'calc.exe'])
    elif 'open discord' in command:
        response_text.insert(tk.END, 'Babu Sir: Opening Discord\n')  # discord
        talk('Opening Discord')
        subprocess.Popen([r'C:\Users\91628\AppData\Local\Discord\Update.exe --processStart Discord.exe'])
    elif 'open weather map' in command:
        response_text.insert(tk.END, 'Babu Sir: Opening weather map\n')  # ms waether map
        talk('Opening weather map')
        webbrowser.open('https://www.msn.com/en-in/weather/maps/temperature/in-Trivandrum,KL?loc=eyJsIjoiVHJpdmFuZHJ1bSIsInIiOiJLTCIsImMiOiJJbmRpYSIsImkiOiJJTiIsImciOiJlbi1pbiIsIngiOiI3Ni45Mjk1MzEwOTc0MTIxIiwieSI6IjguNTMwMzY0NDQwOTM1NDQifQ%3D%3D&weadegreetype=C&ocid=winp2fptaskbar&cvid=be03b0cb5b62408f93dcb7f12007d645&zoom=8')
    elif 'open edge' in command:
        response_text.insert(tk.END, 'Babu Sir: Opening edge\n')  # 
        talk('Opening edge')
        webbrowser.open('https://www.bing.com/?FORM=Z9FD1')
    elif 'open vs code' in command:
        response_text.insert(tk.END, 'Babu Sir: Opening VS code\n')  # 
        talk('Opening VS code')
        subprocess.Popen([r'"C:\Users\91628\AppData\Local\Programs\Microsoft VS Code\Code.exe"'])
    elif 'open steam' in command:
        response_text.insert(tk.END, 'Babu Sir: Opening steam\n')  # 
        talk('Opening steam')
        subprocess.Popen([r'"C:\Program Files (x86)\Steam\Steam.exe"'])
    elif 'open brave' in command:
        response_text.insert(tk.END, 'Babu Sir: Opening Brave\n')  # 
        talk('Opening Brave')
        subprocess.Popen([r'C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe'])
    elif 'open youtube' in command:
        response_text.insert(tk.END, 'Babu Sir: Opening YouTube in your web browser\n')  # 
        talk('Opening YouTube in your web browser')
        webbrowser.open('https://www.youtube.com')
    elif 'time' in command:
        current_time = datetime.datetime.now().strftime('%I:%M %p')
        response_text.insert(tk.END, f'Babu Sir: Current time is {current_time}\n')  # 
        talk(f'Current time is {current_time}')
    elif 'who is' in command:
        person = command.replace('who is' or 'what is', '')
        try:
            info = wikipedia.summary(person, 1)
            response_text.insert(tk.END, f'Babu Sir: {info}\n')  # 
            talk(info)
        except wikipedia.exceptions.DisambiguationError as e:
            response_text.insert(tk.END, "Babu Sir: It seems there are multiple matching results. Please be more specific.\n")  # 
            talk("It seems there are multiple matching results. Please be more specific.")
        except wikipedia.exceptions.PageError as e:
            response_text.insert(tk.END, "Babu Sir: I couldn't find any information about that.\n")  # 
            talk("I couldn't find any information about that.")
    elif 'say who is the owner' in command:
        response_text.insert(tk.END, 'Babu Sir: The owner of this laptop is Aswin\n')  # 
        talk('The owner of this laptop is Ashwin')
    elif 'who are you' in command or 'what is your name' in command:
        response_text.insert(tk.END, 'Babu Sir: Im Babu, your personal assistant\n')  # 
        talk('Im Babu, your personal assistant')
    elif 'joke' in command:
        joke = pyjokes.get_joke()
        response_text.insert(tk.END, f'Babu Sir: {joke}\n')  # 
        talk(joke)
    else:
        response_text.insert(tk.END, f'Babu Sir: Please say the command again\n')  # 
        talk('Please say the command again')
# Create a function to listen to voice commands
def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            listener.adjust_for_ambient_noise(source)  # Adjust for ambient noise
            voice = listener.listen(source)
            command = listener.recognize_google(voice).lower()
            if 'Babu' in command:
                command = command.replace('Babu', '')
                print(command)
    except sr.WaitTimeoutError as e:
        command = "Listening timeout. Please try again."
    except sr.RequestError as e:
        command = "Sorry, I couldn't request results; check your network connection."
    except sr.UnknownValueError as e:
        command = "I couldn't understand what you said."
    return command

   
# Create a function to make the AI Babu Sir speak
def talk(text):
    engine.say(text)
    engine.runAndWait()


# Create a button to trigger the AI Babu Sir 
start_button = tk.Button(root, text="Ask", command=run_babu, bg="green", fg="white")
start_button.pack(side="bottom", fill="both", expand=True)

# Create a text widget to display responses
response_text = tk.Text(root, width=50, height=10, bg='white', fg='black')
response_text.pack(side="top", fill="both", expand=True)


# Initialize speech recognition and text-to-speech
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('rate', 150)
# Set volume 0-1
engine.setProperty('volume', 0.7)
engine.setProperty('voice', voices[0].id)  # Adjust the voice index as needed

# Start the Tkinter main loop
root.mainloop()
