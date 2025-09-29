from langgraph.prebuilt import create_react_agent
from langchain_google_genai import ChatGoogleGenerativeAI  # <-- use this!

import requests

GNEWS_API_KEY = "0558d015ac07fb94f4ea593f99294577"

def fetch_news_gnews(topic: str) -> str:
    """
    Fetch 5 latest news articles on the given topic using GNews API,
    including the image for each article.
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
        image = article.get("image", "No Image")
        result.append(f"📰 {title}\n🔗 {link}\n🖼️ {image}")

    return "\n\n".join(result)


# ✅ Use ChatGoogleGenerativeAI here
gemini = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    api_key="AIzaSyCjkLJ-U9CkIGJdCzk2pWm3JDxpfezVPZw",
    temperature=0
)

agent = create_react_agent(
    model=gemini,
    tools=[fetch_news_gnews],
    prompt="You are a helpful assistant"
)

output = agent.invoke(
    {"messages": [{"role": "user", "content": "Give me latest news on Artificial Intelligence"}]}
)

print(output["messages"][-1].content)  # show only the assistant reply

# agent = initialize_agent(
#     tools=tools,
#     llm=gemini,
#     agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
#     verbose=True,
# )
# resp = agent.run("Give me latest news on Artificial Intelligence")
# print(resp)








# from google import genai

# # The client gets the API key from the environment variable `GEMINI_API_KEY`.
# client = genai.Client(api_key="AIzaSyCjkLJ-U9CkIGJdCzk2pWm3JDxpfezVPZw")

# response = client.models.generate_content(
#     model="gemini-2.5-flash", contents="Explain how AI works in a few words"
# )
# print(response.text)