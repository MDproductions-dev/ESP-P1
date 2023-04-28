# Please keep in mind the MIT licence and credit appropriately when you use this in a (commercial) project. 
This code is made public to help other people in our project class with reading the P1 data, it may not fit your needs.

# ESP-P1
Code for reading data from a dutch smart meter's P1 port with an ESP32 running micropython.

The raw data lines will be sent in an array to the specified url.

The code is made for ESMR 5.0 output, please adjust the values in main.py on line 7 for your specific meter standards.

Values to be changed:

boot.py: 
| Variable       | Description       | Example value  |
| ------------- |:-------------:| --------------:|
| network_ssid    | The ssid of your wifi network. | Ziggo1234 |
| network_password    | The password of your wifi network.      |   Wifi1234 |

main.py:
| Variable       | Description       | Example value  |
| ------------- |:-------------:| --------------:|
| POST_URL    | The url where the ESP32 will post to.  | https://example.com/posturl |
| AUTH_TOKEN    |  A token used to post data to the url, please change this to disallow unauthorized people from sending data to your server. (also make sure your server checks this token!!!)  |   verysecrettoken |
