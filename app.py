# from deta import Deta
from fastapi import FastAPI
from generateOutput import generate_linkedin_post
from gnews import getNewsFromSource
import json
app = FastAPI()
@app.get("/news/{topic}",)
def getnews(topic):
    print(topic)
    news_articles = getNewsFromSource(topic=topic)
    linkedin_post = generate_linkedin_post(news_articles,topic)
    frontend_payload = {
        "topic": topic,
        "news_sources": [article["url"] for article in news_articles],
        "linkedin_post": linkedin_post,
        "image_suggestion": [article["image"] for article in news_articles if article["image"]]
    }
    print("---------------------------------------------------------------------------------")
    # print(frontend_payload)
    # print(type(frontend_payload))
    # print(result)
    # return({"topic":topic})
    return({"topic":frontend_payload['topic'],"news_sources":frontend_payload['news_sources'],"linkedin_post":frontend_payload['linkedin_post'],"image_suggestion":frontend_payload['image_suggestion']})
