
from constants import GNEWS_API_KEY
import requests
def getnews(topic):
    """
    Fetch 5 latest news articles on the given topic using GNews API,
    including the image for each article.
    """
    url = f"https://gnews.io/api/v4/search?q={topic}&lang=en&max=5&apikey={GNEWS_API_KEY}"
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Error fetching news: {response.status_code}")
        return []
    data = response.json()
    articles = data.get("articles", [])
    result = []
    for article in articles[:5]:
        result.append({
            "title": article.get("title", "No Title"),
            "url": article.get("url", "No URL"),
            "image": article.get("image", None)
        })
    return result