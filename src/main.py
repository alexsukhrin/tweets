from fastapi import FastAPI
import uvicorn
from config import HOST, PORT, DATABASE_URL
import databases
from typing import List
from tables import tweets
from models import Tweets

app = FastAPI()
db = databases.Database(DATABASE_URL)


@app.on_event("startup")
async def startup():
    await db.connect()


@app.on_event("shutdown")
async def shutdown():
    await db.disconnect()


@app.get("/", response_model=List[Tweets])
async def read_notes():
    query = tweets.select()
    return await db.fetch_all(query)


if __name__ == '__main__':
    uvicorn.run(app, host=HOST, port=int(PORT))
