import time
import mqttsub
import network
def do_connect():
        sta_if = network.WLAN(network.STA_IF)
        ap_if = network.WLAN(network.AP_IF)
        if ap_if.active():
                ap_if.active(False)
        if not sta_if.isconnected():
                print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('OPPO Find X3', '1234567890qweer') #wifi的SSID和密码
        while not sta_if.isconnected():
                pass
        print('network config:', sta_if.ifconfig())
        mqttsub.hasConnect = False
        mqttsub.main()

while True:
    try:
        do_connect()
    except:
        print("lost connection")
        time.sleep(5)
        do_connect()
    time.sleep(1)



