# src/command_processing.py
from news_api import get_news
from weather_api import get_weather

def process_command(command):
    if 'hello' in command.lower():
        return "Hello! How can I assist you today?"
    elif 'weather' in command.lower():
        return get_weather('58d05671baa94424b1b183730241909')
    elif 'news' in command.lower():
        news = get_news('b3358f544fb1474e9f1ff968dd2f6258')
        return "\n".join(news)
    elif 'joke' in command.lower():
        return "Jokes functionality is not implemented yet."
    else:
        return "Sorry, I didn't understand that command."
