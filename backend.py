import requests
print("hi")
GNEWS_API_KEY = "0558d015ac07fb94f4ea593f99294577"  

def fetch_news_gnews(topic: str) -> str:
    print(topic)
    """
    Fetch 5 latest news articles on the given topic using GNews API.
    Input: A topic string (e.g., "Artificial Intelligence").
    Output: A formatted list of 5 news articles with titles & URLs.
    """
    url = f"https://gnews.io/api/v4/search?q={topic}&lang=en&max=5&apikey={GNEWS_API_KEY}"
    response = requests.get(url)

    if response.status_code != 200:
        return f"Error fetching news: {response.status_code}"

    data = response.json()
    articles = data.get("articles", [])

    if not articles:
        return f"No news found for topic: {topic}"

    result = []
    for article in articles[:5]:
        title = article.get("title", "No Title")
        link = article.get("url", "No URL")
        result.append(f"📰 {title}\n🔗 {link}")

    return "\n\n".join(result)
