import subprocess
import os

def open_application(application_name):
    try:
        if "chrome" in application_name.lower():
            subprocess.Popen([r"C:\Program Files\Google\Chrome\Application\chrome.exe"])
        elif "notepad" in application_name.lower():
            subprocess.Popen([r"C:\Windows\System32\notepad.exe"])
        elif "whatsapp" in application_name.lower():
            subprocess.Popen([r"C:\Users\Farhaan Ali\AppData\Local\WhatsApp\WhatsApp.exe"])  # Ensure the path is correct
        else:
            print(f"Application '{application_name}' is not configured.")
    except Exception as e:
        print(f"Failed to open application: {str(e)}")
