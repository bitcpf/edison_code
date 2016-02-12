import mraa
from gcloud import pubsub
import time

u=mraa.Uart(0) 
u.setBaudRate(9600)
u.setMode(8, mraa.UART_PARITY_NONE, 1)
u.setFlowcontrol(False, False)





# Initialize subscriper
client = pubsub.Client(project='avid-compound-114722')
topic = client.topic('christest')
subscription = topic.subscription('chrissub')


publisher = pubsub.Client(project='avid-compound-114722')
pubtopic = client.topic('websensors')

time.sleep(0.3)                                                                                                                                                             
cur = 0                                                                                                                                                              
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
	    msg_s = "C 2 L 1\r"
            u.flush()
	    u.writeStr(msg_s)
	    if u.dataAvailable(100):
		print("We've got a response: '{0}', says the other side".format(u.readStr(20)))
	    else:
		print("No data received, do you have anything at the other end?")
	    time.sleep(0.3)
	    cur = 1
	    st = pubtopic.publish(str(cur))
	    print st,cur
        if(cmd == 'lumaoff'):
	    print "Luma OFF!"
	    msg_s = "C 2 L 0\r"
            u.flush()
	    u.writeStr(msg_s)
	    if u.dataAvailable(100):
		print("We've got a response: '{0}', says the other side".format(u.readStr(20)))
	    else:
		print("No data received, do you have anything at the other end?")
	    time.sleep(0.3)
	    cur = 0 
	    st = pubtopic.publish(str(cur))
	    print st,cur
    del cmd_s[:] 
    time.sleep(0.5)
