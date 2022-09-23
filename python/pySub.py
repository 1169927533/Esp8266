from simple import MQTTClient
from machine import Pin
import machine
import time
import micropython
#选择G4引脚
g4 = Pin(2, Pin.OUT, value=0)
# MQTT服务器地址域名为：183.230.40.39,不变
SERVER = "47.92.5.227"
#设备ID
CLIENT_ID = "deviceID"
#随便起个名字
TOPIC = b"raspberry/mqtt"
#产品ID
username='productID'
#产品APIKey:
password='APIKey'
state = 0
sendmsg = b'{"在线～"}'

def sub_cb(topic, msg):
    global state
    print((topic, msg))
    if msg == b"off":
        c.publish(TOPIC, sendmsg, qos=0)
        g4.value(1)
        state = 1
        print("1")
    elif msg == b"on":
        c.publish(TOPIC, sendmsg, qos=0)
        g4.value(0)
        state = 0
        print("0")
    elif msg == b"toggle":
        c.publish(TOPIC, sendmsg, qos=0)
        state = 1 - state
        g4.value(state)
        
c = MQTTClient(CLIENT_ID, SERVER,1883)
def main(server=SERVER):
    #端口号为：6002
    c.set_callback(sub_cb)
    c.connect()
    c.subscribe(TOPIC)
    print("Connected to %s, subscribed to %s topic" % (server, TOPIC))
    try:
        while 1:
            time.sleep(1)
            c.wait_msg()
    finally:
        c.disconnect()


