import os
import redis
from rq import Worker, Queue, Connection
import time

from hello import workerstuff

listen =['high', 'default', 'low']

#redis_url= urlparse.urlparse(os.environ.get('REDISCLOUD_URL'))
#r=redis.Redis(host=url.hostname, port=url.port, password=url.password)

redis_url = os.getenv('REDISCLOUD_URL', 'redis://localhost:6379')
print redis_url
conn=redis.from_url(redis_url)



q=Queue(connection=conn)
result=q.enqueue(workerstuff)


if __name__ == '__main__':
  start=time.time()
  interval=30
  while True:
    if time.time()>=interval+start:
      start=time.time()
      with Connection(conn):
            worker=Worker(map(Queue, listen))
            worker.work()
