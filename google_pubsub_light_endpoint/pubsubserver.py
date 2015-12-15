import mraa
from gcloud import pubsub
import time

x = mraa.Gpio(13)
x.dir(mraa.DIR_OUT)

# Initialize subscriper
client = pubsub.Client(project='avid-compound-114722')
topic = client.topic('christest')
subscription = topic.subscription('chrissub')

while True:
    received = subscription.pull()
    messages = [recv[1] for recv in received]
    cmd_s = [message.data for message in messages]
    ack_ids = [recv[0] for recv in received]
    subscription.acknowledge(ack_ids)
    if(len(cmd_s) >= 1):
        cmd = cmd_s[0]
#        print cmd
#        print type(cmd)
        if(cmd == 'lumaon'):
            print "Luma ON!"
            x.write(1)
        if(cmd == 'lumaoff'):
	    print "Luma OFF!"
            x.write(0)
    del cmd_s[:] 
    time.sleep(0.1)
