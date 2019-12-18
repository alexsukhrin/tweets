"""Install the config for caching. """
from aiocache import caches  # type: ignore


caches.set_config({
    'default': {
        'cache': "aiocache.SimpleMemoryCache",
        'serializer': {
            'class': "aiocache.serializers.StringSerializer"
        }
    }
})
