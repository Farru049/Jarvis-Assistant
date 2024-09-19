# src/news_api.py
import requests

def get_news(api_key, query='latest'):
    url = f"https://newsapi.org/v2/everything?q={query}&apiKey={api_key}"
    response = requests.get(url)
    data = response.json()
    articles = data.get('articles', [])
    news = [article['title'] for article in articles]
    return news

# Example usage
if __name__ == "__main__":
    api_key = 'YOUR_API_KEY'
    news = get_news(api_key)
    for headline in news:
        print(headline)
