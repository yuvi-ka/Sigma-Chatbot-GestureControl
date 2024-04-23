import pyttsx3
import speech_recognition as sr
import eel
import time
import subprocess
import os


def speak(text):
    text = str(text)
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices') 
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 174)
    eel.DisplayMessage(text)
    engine.say(text)
    eel.receiverText(text)
    engine.runAndWait()

"""@eel.expose
def stopSpeaking():
    global engine
    engine.stop()"""


def takecommand():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('listening....')
        eel.DisplayMessage('listening....')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        
        audio = r.listen(source, 10, 6)

    try:
        print('recognizing')
        eel.DisplayMessage('recognizing....')
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")
        eel.DisplayMessage(query)
        time.sleep(2)

       
    except Exception as e:
        return ""
    
    return query.lower()


@eel.expose
def allCommands(message=1):
    if message == 1:
        query = takecommand()
        print(query)
        eel.senderText(query)
    else:
        query = message
        eel.senderText(query)



    try:

        if "open" in query:
            from engine.features import openCommand
            openCommand(query)
        elif "on youtube" in query:
            from engine.features import PlayYoutube
            PlayYoutube(query)
        elif "mouse" in query:
            activate_virtual_mouse(query)

        else:
            from engine.features import chatBot
            chatBot(query)
    except:
        print("error")
    eel.ShowHood()

def activate_virtual_mouse(query):
  if query.lower() == "mouse":
    speak("Activating virtual mouse control.")
    #script_name = "Gesture_Controller.py"  # Assuming the script name
    #script_path = os.path.join(os.getcwd(), script_name)  # Get current working directory
    subprocess.run(["python", "jarvis-main\\engine\\Gesture_Controller.py" ])
    eel.ShowHood()

    """else :
        from engine.features import process_voice_command
        # Call process_voice_command to handle the voice command
        result = process_voice_command(query)
        if result:
            print(result)  # Print the result to console
        else:
            print("Command not recognized")"""
    



    


    """if message == 1:
        query = takecommand()
        print(query)
        eel.senderText(query)
    else:
        query = message
        eel.senderText(query)
    try:

        if "open" in query:
            from engine.features import openCommand
            openCommand(query)
        elif "on youtube" in query:
            from engine.features import PlayYoutube
            PlayYoutube(query)
        
        elif "send message" in query or "phone call" in query or "video call" in query:
            from engine.features import findContact, whatsApp
            flag = ""
            contact_no, name = findContact(query)
            if(contact_no != 0):

                if "send message" in query:
                    flag = 'message'
                    speak("what message to send")
                    query = takecommand()
                    
                elif "phone call" in query:
                    flag = 'call'
                else:
                    flag = 'video call'
                    
                whatsApp(contact_no, query, flag, name)
        else:
            from engine.features import chatBot
            chatBot(query)
    except:
        print("error")"""
    
    


"""elif "open gesture controller" in query:
        # Run Gesture_Controller.py script
        script_path = os.path.join(os.getcwd(), "engine", "Gesture_Controller.py")
        subprocess.run(["python", script_path])  # Assuming Gesture_Controller.py is in the engine folder
        speak("Opening Gesture Controller")"""
