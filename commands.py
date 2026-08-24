import os
import subprocess
import webbrowser
import google.generativeai as genai

# Direct text-to-speech using pyttsx3 without needing a separate 'speech.py' file
try:
    import pyttsx3
    def speak(text):
        try:
            engine = pyttsx3.init()
            engine.say(text)
            engine.runAndWait()
        except Exception:
            pass
except ImportError:
    def speak(text):
        pass

genai.configure(api_key="AQ.Ab8RN6IFmuuDuiEu7-InUePCA7Uw9iS9yrvi6uwmtKsqDitwLw")

baryon_mode = False
COMMAND_CODE = "0000"

def ask_gemini(prompt):
    try:
        model = genai.GenerativeModel("gemini-3.6-flash")
        response = model.generate_content(prompt)
        ai_response = response.text
        print(ai_response)
        speak(ai_response)
        return ai_response
    except Exception as e:
        error_msg = f"Gemini API Error: {e}"
        print(error_msg)
        speak("Error")
        return error_msg

def execute_command(user_input):
    global baryon_mode
    print(f"Executing command for: {user_input}")
    
    if not user_input:
        print("Falling back to Gemini...")
        return ask_gemini(user_input)

    command = user_input.lower().strip()

    if "baryon mode activate" in command:
        if COMMAND_CODE in command:
            baryon_mode = True
            print("Command code activated. Full system access granted.")
            speak("Baryon mode activated.")
            return "Command code activated. Full system access granted."
        else:
            print("Incorrect command code. Access denied.")
            speak("Incorrect command code.")
            return "Incorrect command code. Access denied."

    if baryon_mode:
        if "baryon mode deactivate" in command:
            baryon_mode = False
            print("Baryon mode deactivated. Returning to normal assistant mode.")
            speak("Baryon mode deactivated.")
            return "Baryon mode deactivated. Returning to normal assistant mode."

        if "whatsapp message" in command or "send message to" in command:
            webbrowser.open("https://web.whatsapp.com/")
            print("Opening WhatsApp for messaging.")
            speak("Opening WhatsApp.")
            return "Opening WhatsApp for messaging."

        if "call" in command:
            if "hang up" in command or "cut the call" in command:
                print("Hanging up the call.")
                speak("Hanging up.")
                return "Hanging up the call."
            else:
                print("Initiating call handler...")
                speak("Initiating call.")
                return "Initiating call handler..."

        if "youtube" in command or "play" in command:
            search_query = command.replace("play", "").replace("youtube", "").strip()
            url = f"https://www.youtube.com/results?search_query={search_query}"
            webbrowser.open(url)
            print(f"Playing {search_query} on YouTube.")
            speak(f"Playing {search_query} on YouTube.")
            return f"Playing {search_query} on YouTube."

        if "balance" in command or "gpay" in command:
            print("Opening financial portal securely.")
            speak("Opening financial portal.")
            return "Opening financial portal securely."

    print("Falling back to Gemini...")
    return ask_gemini(user_input)