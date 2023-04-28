import network

network_ssid = "Ziggo1234"
network_password = "Wifi1234"

#Connect to WiFi
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(network_ssid, network_password)
while not wifi.isconnected():
    pass
print('Connected to WiFi:', wifi.ifconfig())