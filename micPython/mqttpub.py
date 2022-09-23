# pub.py
import time
from simple import MQTTClient

# 定义 pub 客户端的连接信息
server = "47.92.5.227"
ClientID = f'raspberry-pub-{time.time_ns()}'
user = "emqx"
password = "public"
topic = "raspberry/mqtt"
msg = b'{"msg":"hello"}'


# 创建连接，参数分别为客户端 ID，broker 地址，broker 端口号，认证信息
def connect():
    print('Connected to MQTT Broker "%s"' % (server))
    client = MQTTClient(ClientID, server, 1883)
    client.connect()
    return client


# 若能连接到 broker，调用 connect()，反之调用 reconnect()
def main():
    client = connect()

    while True:
        # 每隔 1 秒给主题 raspberry/mqtt 发送一条消息
        print('send message %s on topic %s' % (msg, topic))
        client.publish(topic, msg, qos=0)
        time.sleep(1)