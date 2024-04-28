from machine import Pin
import usocket as socket
import time
import network


timeout = 0 # WiFi Connection Timeout variable

# Restarting WiFi
#wifi.active(False)
#time.sleep(0.5)
wifi = network.WLAN(network.AP_IF)
wifi.active(True)

wifi.config(essid = 'ZISUN',password = '12345678KTSC',authmode = network.AUTH_WPA_WPA2_PSK)
print(wifi.ifconfig())

'''if not wifi.isconnected():
    print('connecting..')
    while (not wifi.isconnected() and timeout < 5):
        print(5 - timeout)
        timeout = timeout + 1
        time.sleep(1)
        
if(wifi.isconnected()):
    print('Connected...')
    print('network config:', wifi.ifconfig())'''


# HTML Document

html='''<!DOCTYPE html>
<html lang="en">
<head>
  
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  
  <title>Powered by ASIDDAU ALAL KUFFAR</title>


<style>
.l2 {
  background-color: white; 
  color: black; 
  border: 6px solid #008CBA;

  background-color: white; /* Green */
  border: none;
  color: black;
  padding: 16px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 4px 2px;
  border-radius: 30%;
  transition-duration: 0.4s;
  cursor: pointer;

  
}

.l2:hover {
  background-color: #008CBA;
  color: white;
}

body{
  background-color: skyblue;
}

</style>
  
</head>
<body>


<center><h2 class="b2" > Smart Webserver  </h2></center>
<form>
<center>
<h3> WATER_PUMP </h3>
<button class="l2" name="button1" value='ON' type='submit'>  ON </button>
<button class="l2" name="button1" value='OFF' type='submit'> OFF </button>
<h3> BUTTON2 </h3>
<button class="l2" name="button2" value='ON' type='submit'>  ON </button>
<button class="l2" name="button2"  value='OFF' type='submit'> OFF </button>


<h3 class="ktsc">Powered by ASIDDAU ALAL KUFFAR</h3>



</center>
  
</body>
</html>
'''

# Output Pin Declaration 
LED1 = Pin(15,Pin.OUT)
LED1.value(1)

LED2 = Pin(2,Pin.OUT)
LED2.value(0)



# Initialising Socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # AF_INET - Internet Socket, SOCK_STREAM - TCP protocol

Host = '' # Empty means, it will allow all IP address to connect
Port = 80 # HTTP port
s.bind(('',80)) # Host,Port

s.listen(5) # It will handle maximum 5 clients at a time

# main loop
while True:
  connection_socket,address=s.accept() # Storing Conn_socket & address of new client connected
  print("Got a connection from ", address)
  request=connection_socket.recv(1024) # Storing Response coming from client
  print("Content ", request) # Printing Response 
  request=str(request) # Coverting Bytes to String
  # Comparing & Finding Postion of word in String 
  LED1_ON =request.find('/?button1=ON')
  LED1_OFF =request.find('/?button1=OFF')
  
  LED2_ON =request.find('/?button2=ON')
  LED2_OFF =request.find('/?button2=OFF')
  
  if(LED1_ON==6):
    LED1.value(0)   
  if(LED1_OFF==6):
    LED1.value(1)
    
  if(LED2_ON==6):
      t=6 #seconds
      LED2.value(1)
      time.sleep(t)
      LED2.value(0)
      
  if(LED2_OFF==6):
    LED2.value(0)
    
    
    
    
  # Sending HTML document in response everytime to all connected clients  
  response=html 
  connection_socket.send(response)
  
  #Closing the socket
  connection_socket.close() 





