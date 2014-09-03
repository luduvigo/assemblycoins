import time
from main import workerstuff

start=time.time()
interval=10
while True:
  if time.time()>=interval+start:
    start=time.time()
    workerstuff()
