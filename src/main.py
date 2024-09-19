import signal
import sys
from voice_recognition import recognize_speech
from text_to_speech import text_to_speech
from command_processing import process_command

def signal_handler(sig, frame):
    print('Exiting...')
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

def main():
    while True:
        command = recognize_speech()
        if command:
            response = process_command(command)
            text_to_speech(response)

if __name__ == "__main__":
    main()
