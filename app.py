
from fastapi import FastAPI
from generateOutput import generate_linkedin_post
from gnews import getNewsFromSource


from utils import frontent_format_conversion
app = FastAPI()

@app.get("/")
def start():
    return ({"Message from developer" : "To fetch the news content based on topic. Please modify url as 'https://news-fetch-gemini.vercel.app/(Type your topic inside a string literal and hit enter)' "})
@app.get("/{topic}",)
def getnews(topic):

    news_articles = getNewsFromSource(topic=topic)
    
    linkedin_post = generate_linkedin_post(news_articles,topic)
    
    result = frontent_format_conversion(topic=topic,news_articles=news_articles,linkedin_post=linkedin_post)

    return({"topic":result['topic'],"news_sources":result['news_sources'],"linkedin_post":result['linkedin_post'],"image_suggestion":result['image_suggestion']})
