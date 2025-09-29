from langchain_google_genai import ChatGoogleGenerativeAI
from constants import GOOGLE_API_KEY
from constants import GNEWS_API_KEY

def get_news_url(topic):
    url =f"https://gnews.io/api/v4/search?q={topic}&lang=en&max=5&apikey={GNEWS_API_KEY}"
    return url

def gemini_initialization():
    gemini = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        api_key=GOOGLE_API_KEY,
        temperature=0.7
    )
    return gemini
def frontent_format_conversion(topic,news_articles,linkedin_post):
    frontend_payload = {
        "topic": topic,
        "news_sources": [article["url"] for article in news_articles],
        "linkedin_post": linkedin_post,
        "image_suggestion": [article["image"] for article in news_articles if article["image"]]
    }
    return frontend_payload