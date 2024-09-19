import tkinter as tk
from voice_recognition import listen
from text_to_speech import speak
from command_processing import process_command
from system_control import execute_command

def on_button_click():
    command = listen()
    if command:
        response = process_command(command)
        speak(response)
        execute_command(command)

def setup_ui():
    root = tk.Tk()
    root.title("Jarvis Desktop Assistant")

    button = tk.Button(root, text="Speak", command=on_button_click)
    button.pack()

    root.mainloop()
