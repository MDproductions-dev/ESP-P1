import machine
import urequests

print("main initialized")
uart = machine.UART(2, baudrate=115200)
print("uart made")
uart.init(baudrate=115200, bits=8, parity=None, stop=1, timeout=5000, invert=machine.UART.INV_RX, rxbuf=2048)
print("uart initialized")

POST_URL = "https://----" # The url the ESP32 will write all the lines to
AUTH_TOKEN = "verysecrettoken" # Please change this, this will stop unauthorized people from writing data to your server

while True:
    try:
        if uart.any():
            p1_data = []
            while uart.any():
                p1_data += [uart.readline()]
            print(p1_data)
            response = urequests.post(POST_URL, json=p1_data, headers={"Authorization": AUTH_TOKEN})
            print('Response:', response.text)
            response.close()
        else:
            print("no data recieved")
    except:
        pass