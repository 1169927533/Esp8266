from umqtt.simple import MQTTClient
from umachine import Pin
import umachine
import utime
import micropython
import _thread
#选择G4引脚
g4 = Pin(2, Pin.OUT, value=1)
# MQTT服务器地址域名为：183.230.40.39,不变
SERVER = "47.92.5.227"
#设备ID
CLIENT_ID = "d5487oUi2390"
subtopic= b"subliyu/opito"
heartbeattopic = b"hearbeattopic/opito"
callbackpic= b"callbacke/opito"#回复客户端的问答
TOPIC = b"raspberry/mqtt"
username='productID'
#产品APIKey:
password='APIKey'
state = 0
sendmsg = b'{"在线～"}'
heartmsg= b'心跳包..'
hasConnect=False
c = MQTTClient(CLIENT_ID, SERVER,1883)

def sub_cb(topic, msg):
    global state
    c.publish(callbackpic, sendmsg, qos=0)
    print((topic, msg))
    if msg == b"off":
        g4.value(1)
        state = 1
        print("1")
    elif msg == b"on":
        g4.value(0)
        state = 0
        print("0")
    elif msg == b"toggle":
        state = 1 - state
        g4.value(state)

def waitmsg(delay,id):
    while True:
        utime.sleep(delay)
        c.wait_msg()

def pubmsg(delay,id):
    while True:
        utime.sleep(delay)
        c.publish(heartbeattopic, heartmsg, qos=0)

def main(server=SERVER):
    global hasConnect
    if not hasConnect:
        hasConnect=True
        c.set_callback(sub_cb)
        c.connect()
        c.subscribe(subtopic)
        print("Connected to %s, subscribed to %s topic" % (server, subtopic))
    _thread.start_new_thread(waitmsg,(1,1))
    _thread.start_new_thread(pubmsg,(4,2))
        
        

main()


