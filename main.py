import network
import ujson
from utime import sleep_ms

from server import start

with open('env.json', 'r') as f:
    env = ujson.loads(f.read())

sta = network.WLAN(network.STA_IF)
sta.active(True)
login = env.get('wireless')
sta.connect(login.get('ssid'), login.get('password'))

while sta.status() != network.STAT_GOT_IP:
    sleep_ms(500)

start(sta)
