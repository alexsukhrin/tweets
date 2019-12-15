from fastapi import FastAPI
import uvicorn
from typing import List
from models import Tweets
import asyncpg
import config
from handler import ApiHandler

app = FastAPI()


@app.on_event("startup")
async def startup():
    """
    The func returns connect to db.
    :return: db
    """
    pool = await asyncpg.create_pool(
        database=config.POSTGRES_DB,
        user=config.POSTGRES_USER,
        password=config.POSTGRES_PASSWORD,
        host=config.POSTGRES_HOST,
        port=config.POSTGRES_PORT,
    )
    setattr(app, 'pool', pool)
    return app


@app.on_event("shutdown")
async def shutdown():
    """
    The func close connect db.
    :return:
    """
    pool = getattr(app, 'pool', None)
    if pool:
        await pool.close()


@app.get("/", response_model=List[Tweets])
async def read_notes():
    """
    The handler returns tweets.
    :return: list
    """
    handler = ApiHandler(app=app)
    return await handler.response()


if __name__ == '__main__':
    uvicorn.run(app, host=config.HOST, port=int(config.PORT))
