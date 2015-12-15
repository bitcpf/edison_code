import mraa
from gcloud import pubsub
import time

x = mraa.Gpio(13)
x.dir(mraa.DIR_OUT)

# Initialize subscriper
client = pubsub.Client(project='avid-compound-114722')
topic = client.topic('christest')
subscription = topic.subscription('chrissub')


publisher = pubsub.Client(project='avid-compound-114722')
pubtopic = client.topic('websensors')

time.sleep(0.3)                                                                                                                                                             
cur = x.read()                                                                                                                                                              
st = pubtopic.publish(str(cur))                                                                                                                                             
print st,cur                   


while True:
    received = subscription.pull()
    if(len(received) >= 1):
	messages = [recv[1] for recv in received]
        cmd_s = [message.data for message in messages]
        ack_ids = [recv[0] for recv in received]
        subscription.acknowledge(ack_ids)
        cmd = cmd_s[0]
#        print cmd
#        print type(cmd)
	
        if(cmd == 'lumaon'):
            print "Luma ON!"
            x.write(1)
	    time.sleep(0.3)
	    cur = x.read()
	    st = pubtopic.publish(str(cur))
	    print st,cur
        if(cmd == 'lumaoff'):
	    print "Luma OFF!"
            x.write(0)
	    time.sleep(0.3)
	    cur = x.read()
	    st = pubtopic.publish(str(cur))
	    print st,cur
    del cmd_s[:] 
    time.sleep(0.5)
