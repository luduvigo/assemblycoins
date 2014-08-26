import os
import redis
from rq import Worker, Queue, Connection
import time

from rq_scheduler import Scheduler
from datetime import datetime

from hello import workerstuff

listen =['high', 'default', 'low']

#redis_url= urlparse.urlparse(os.environ.get('REDISCLOUD_URL'))
#r=redis.Redis(host=url.hostname, port=url.port, password=url.password)

redis_url = os.getenv('REDISCLOUD_URL', 'redis://localhost:6379')
print redis_url
conn=redis.from_url(redis_url)

use_connection()

scheduler=Scheduler()
scheduler.schedule(
datetime.now(),
workerstuff,
interval=30
)

#
#
# q=Queue(connection=conn)
# q.
# result=q.enqueue(workerstuff)


if __name__ == '__main__':
  with Connection(conn):
    worker=Worker(map(Queue, listen))
    worker.work()
