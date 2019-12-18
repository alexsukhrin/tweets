"""The main file to start the service. """
from fastapi import FastAPI
import uvicorn  # type: ignore
import asyncpg  # type: ignore
from typing import List

try:
    from .models import (
        Tweets,
        Amount,
        Users,
        Hashtags,
    )
    from . import config
    from .handler import ApiHandler
except ImportError:
    # if the package path was not found in Docker
    from models import (
        Tweets,
        Amount,
        Users,
        Hashtags,
    )
    import config
    from handler import ApiHandler

app = FastAPI()


@app.on_event("startup")
async def startup():
    """The func returns connect to db. """
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
    """The func close connect db. """
    pool = getattr(app, 'pool', None)
    if pool:
        await pool.close()


@app.get("/", response_model=List[Tweets])
async def tweets(offset: int = 0, limit: int = 100) -> list:
    """The handler returns tweets."""
    return await ApiHandler(app=app).tweets(limit=limit, offset=offset)


@app.get("/amount", response_model=List[Amount])
async def amount() -> list:
    """The handler returns amount tweets."""
    return await ApiHandler(app=app).amount()


@app.get("/hashtags", response_model=List[Hashtags])
async def hashtags(limit: int = 3) -> list:
    """The handler returns top three hashtags."""
    return await ApiHandler(app=app).hashtags(limit=limit)


@app.get("/users", response_model=List[Users])
async def users(limit: int = 3) -> list:
    """The handler returns top three users."""
    return await ApiHandler(app=app).users(limit=limit)


if __name__ == '__main__':
    uvicorn.run(app, host=config.HOST, port=int(config.PORT))
