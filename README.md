# proSapient
[![Build Status](https://travis-ci.org/alexsukhrin/proSapient.svg?branch=master)](https://travis-ci.org/alexsukhrin/proSapient)
[![codecov](https://codecov.io/gh/alexsukhrin/proSapient/branch/master/graph/badge.svg)](https://codecov.io/gh/alexsukhrin/proSapient)

**What problems does the project solve**

1. I want to be able to get last K tweets queried by specific phrase once in a configured period of time (N) (Periodic background job)
2. I want to be able to see all unique tweets from the point above
3. I want to be able to see an aggregated statistic for each queried phrase for a given period of time:
    - `top 3 hashtags found in tweets`
    - `top 3 users that made max amount of tweets`
    - `amount of analyzed tweets`

**Open Documentation API**
```
http://0.0.0.0:8004/docs
```

**Project Launch Instructions:**
```
docker-compose build
docker-compose up
open 0.0.0.0:8004
```

**example env file**
```
HOST=0.0.0.0
PORT=8000
POSTGRES_USER=john
POSTGRES_PASSWORD=pwd0123456789
POSTGRES_DB=sapient
POSTGRES_PORT=5432
POSTGRES_HOST=db
TWITTER_CONSUMER_KEY=454aaArVGfr57ZETE4UXkfQR4
TWITTER_CONSUMER_SECRET=HPbBPW6GvEJRQveY1vncEhB9lmkhkA7uhoeOPWWMiyDLL3J45A
API_URL=https://api.twitter.com/oauth2/token
TWEETS_URL=https://api.twitter.com/1.1/search/tweets.json
TWITTER_COUNT=10
TWITTER_QUERY=украина
SCHEDULE_WORK=5
```

**Code Style Flake8 integration with Git**
```
flake8 --install-hook git
git config --bool flake8.strict true
```