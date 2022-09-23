import network
import time
import urequests
AP_name = 'OPPO Find X3'
password = '1234567890qwe'
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.scan()  # Scan for available access points
sta_if.connect(AP_name, password)  # Connect to an AP
while not sta_if.isconnected():
    print('connect...')
    time.sleep(2)

# Change name/password of ESP8266's AP:
# ap_if = network.WLAN(network.AP_IF)
# ap_if.config(essid="要创建的无线网名称", authmode=network.AUTH_WPA_WPA2_PSK, password="要创建的无线网密码")

response = urequests.get('http://www.baidu.com')
print("请求成功"+response.text)

