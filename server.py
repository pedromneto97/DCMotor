import network
from machine import reset
from utime import sleep_ms


class Server:
    def __init__(self, ssid, password):
        self.sta = network.WLAN(network.STA_IF)
        self.sta.active(True)
        self.sta.connect(ssid, password)
        counter = 0
        while not self.sta.isconnected() and counter < 5:
            sleep_ms(200)
            counter += 1
        if counter == 5:
            reset()

    def server(self):
