import pyupm_htu21d as htu21d
import time
from gcloud import datastore

edsensor = htu21d.HTU21D(1)

client = datastore.Client(dataset_id='sb-acl')






while True:

    cur_temp = edsensor.getTemperature(1)
    cur_hud = edsensor.getHumidity(1)

#    print cur_temp
#    print cur_hud

    # Put to data store
#    cur_date = time.strftime("%x")
#    cur_time = time.strftime("%X")
    cur_time = time.time()
    key = client.key('Sensor')
    entity = datastore.Entity(key)    
    entity['SensorID'] = 1 
    entity['Humidity'] = cur_hud
    entity['Temperature'] = cur_temp
    entity['Time'] = cur_time
#    entity['Date'] = cur_date
    client.put(entity)
#    print cur_time

    time.sleep(60)
