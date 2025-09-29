# from deta import Deta
from fastapi import FastAPI
from generateOutput import generate_linkedin_post
from gnews import getNewsFromSource

app = FastAPI()
@app.get("/news/{topic}",)
def getnews(topic):
    print(topic)
    output = getNewsFromSource(topic=topic)
    final_output = generate_linkedin_post(output,topic)
    print("---------------------------------------------------------------------------------")
    print(final_output)
    return {"output":topic}


