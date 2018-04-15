import os
import redis
from rq import Worker, Queue, Connection

listen = ['default']

# localhost redis url
# redis_url = os.getenv('REDISTOGO_URL', 'redis://localhost:6379')
# Heroku redis url
redis_url = os.getenv('REDIS_URL', 'redis://h:p31fceac16f88a241f4ee01587cf164a7c20e9eb2895f6d1ddcf3c67c218f3669@ec2-35-171-227-50.compute-1.amazonaws.com:55429')
conn = redis.from_url(redis_url)

if __name__ == '__main__':
    with Connection(conn):
        worker = Worker(list(map(Queue, listen)))
        worker.work()
