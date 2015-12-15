import mraa
from gcloud import pubsub
import time




x = mraa.Gpio(13)


client = pubsub.Client(project='avid-compound-114722')
topic = client.topic('websensors')

flag = x.read()

while True:
    cur = x.read()
    print cur
    if cur!= flag:
	topic.publish(str(cur))
	flag = cur
    time.sleep(2)
    

