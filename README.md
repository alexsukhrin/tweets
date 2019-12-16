# proSapient
Пользовательские истории
Вот истории пользователей для начала:

1. Я хочу, чтобы последние K твитов запрашивались по определенной фразе
один раз за заданный период времени ( N ) (Периодическое фоновое задание)

2. Я хочу иметь возможность видеть все уникальные твиты из пункта выше

3. Я хочу видеть агрегированную статистику для каждой запрашиваемой фразы 
за определенный период времени:

    топ 3 хэштеги найдены в твитах
    Топ 3 пользователей, которые сделали максимальное количество твитов 
    количество проанализированных твитов

### Status
[![Build Status](https://travis-ci.org/alexsukhrin/proSapient.svg?branch=master)](https://travis-ci.org/alexsukhrin/proSapient)
[![codecov](https://codecov.io/gh/alexsukhrin/proSapient/branch/master/graph/badge.svg)](https://codecov.io/gh/alexsukhrin/proSapient)

## run service
`docker-compose build`
`docker-compose up`
`open 0.0.0.0:8004`

## example env file
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

## open documentation
`http://0.0.0.0:8004/docs`