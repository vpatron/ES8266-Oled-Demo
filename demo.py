import machine
import ssd1306
import network
import time

SSID = 'myhomewifi'
PWD = 'myhomewifipassword'
WIDTH = const(128)
HEIGHT = const(32)

pscl = machine.Pin(5, machine.Pin.OUT)
psda = machine.Pin(4, machine.Pin.OUT)
i2c = machine.I2C(scl=pscl, sda=psda)
ssd = ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c)

ssd.text(' Hello, World!', 0, 5, 1)
ssd.hline(10, 16, 107, 1)               #Line in middle

# Box around screen
ssd.hline(0, 0, 127, 1)
ssd.hline(0, 31, 127, 1)
ssd.vline(0, 0, 31, 1)
ssd.vline(127, 0, 31, 1)
ssd.show()

# Turn off access point and turn on station WiFi. When WLAN connected, 
# show the IP address.
ap_if = network.WLAN(network.AP_IF)
ap_if.active(False) 
sta_if = network.WLAN(network.STA_IF)
sta_if.connect(SSID, PWD)
sta_if.active(True)
while not sta_if.isconnected():
    pass
WLAN_IP = sta_if.ifconfig()[0]
ssd.text(WLAN_IP, 2, 20, 1)
ssd.show()

# Show time
while True:
    time_str = str(time.time())
    ssd.fill_rect(1, 5, 126, 8, 0)
    ssd.text(time_str, 38, 4, 1)
    ssd.show()
    time.sleep(0.98)
