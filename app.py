# from deta import Deta
from fastapi import FastAPI

app = FastAPI()
@app.get("/news/{topic}",)
def getnews(topic):
    print(topic)
    return {"output":topic}
