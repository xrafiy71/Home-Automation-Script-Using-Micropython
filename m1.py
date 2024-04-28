import machine
import usocket as socket
import time
import network


timeout = 0 # WiFi Connection Timeout variable 

#wifi = network.WLAN(network.STA_IF)
wifi = network.WLAN(network.AP_IF)


# Restarting WiFi

wifi.config(essid = 'SMART_AQURIUM 2.0',password = '12345678KTSC',authmode = network.AUTH_WPA_WPA2_PSK)
print(wifi.ifconfig())

    
# HTML Document

html='''<!DOCTYPE html>
<html lang="en">
<head>
  
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  
  <title>Smart Aqurium Webserver 01 </title>


<style>
.l2 {
  background-color: white; 
  color: black; 
  border: 6px solid #0b45b3;

  background-color: #32b336; /* Green */
  border: none;
  color: white;
  padding: 16px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 4px 2px;
  border-radius: 16px;
  transition-duration: 0.4s;
  cursor: pointer;

  
}

.l2:hover {
  background-color: #008CBA;
  color: white;
}

.l3 {
  background-color: white; 
  color: black; 
  border: 6px solid #0b45b3;

  background-color: #32b336; /* Green */
  border: none;
  color: rgba(255, 255, 255, 0.952);
  padding: 16px 42px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 20px;
  margin: 4px 2px;
  border-radius: 18px;
  transition-duration: 0.4s;
  cursor: pointer;

  
}

.l3:hover {
  background-color: #008CBA;
  color: white;
}


body{
  background-color: rgb(255, 166, 0);
}

</style>
  
</head>
<body>


<center><h1 class="b2" > Smart Aqurium Webserver 2.0 </h1></center>
<form>
<center>
<h3> FILTR </h3>
<button class="l2" name="button1" value='ON' type='submit'>  ON </button>
<button class="l2" name="button1" value='OFF' type='submit'> OFF </button>
<h3>AERATOR_OXYGEN</h3>
<button class="l2" name="button2" value='ON' type='submit'>  ON </button>
<button class="l2" name="button2"  value='OFF' type='submit'> OFF </button>
<h3> FEED_SUPLIER </h3>
<button class="l3" name="button3" value='ON' type='submit'>  Feed_Suplier </button>
<!-- <button class="l2" name="button3" value='OFF' type='submit'> OFF </button> -->
<h3> WATER_PUMP </h3>
<button class="l2" name="button4" value='ON' type='submit'>  ON </button>
<button class="l2" name="button4" value='OFF' type='submit'> OFF </button>

<h3> BULB </h3>
<button class="l2" name="button5" value='ON' type='submit'>  ON </button>
<button class="l2" name="button5" value='OFF' type='submit'> OFF </button>

<h3> BUTTON6 </h3>
<button class="l2" name="button6" value='ON' type='submit'>  ON </button>
<button class="l2" name="button6" value='OFF' type='submit' > OFF </button>



<h4 class="ktsc">Powered by ASIDDAU ALAL KUFFAR</h4>

</center>
  
</body>
</html>
'''

# Output Pin Declaration 
button1 = machine.Pin(16,machine.Pin.OUT)
button1.value(1)

button2 = machine.Pin(17,machine.Pin.OUT)
button2.value(1)

button3 = machine.Pin(19,machine.Pin.OUT)
button3.value(1)

button4 = machine.Pin(21,machine.Pin.OUT)
button4.value(1)

button5 = machine.Pin(18,machine.Pin.OUT)
button5.value(1)


button6 = machine.Pin(5,machine.Pin.OUT)
button6.value(1)

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
  button1_ON =request.find('/?button1=ON')
  button1_OFF =request.find('/?button1=OFF')
  
  button2_ON =request.find('/?button2=ON')
  button2_OFF =request.find('/?button2=OFF')
  
  button3_ON =request.find('/?button3=ON')
  button3_OFF =request.find('/?button3=OFF')
  
  button4_ON =request.find('/?button4=ON')
  button4_OFF =request.find('/?button4=OFF')
  
  button5_ON =request.find('/?button5=ON')
  button5_OFF =request.find('/?button5=OFF')
  
  button6_ON =request.find('/?button6=ON')
  button6_OFF =request.find('/?button6=OFF')
  
  if(button1_ON==6):
    button1.value(0)   
  if(button1_OFF==6):
    button1.value(1)
    
  if(button2_ON==6):
    button2.value(0)   
  if(button2_OFF==6):
    button2.value(1)
    
  if(button3_ON==6):
    t=6 # 6 seconds
    button3.value(0)
    time.sleep(t)
    button3.value(1)
   
  if(button3_OFF==6):
    button3.value(1)
    
  if(button4_ON==6):
    button4.value(0)   
  if(button4_OFF==6):
    button4.value(1)

  if(button5_ON==6):
    button5.value(0)   
  if(button5_OFF==6):
    button5.value(1)
    
  if(button6_ON==6):
    button6.value(0)   
  if(button6_OFF==6):
    button6.value(1)
    
  # Sending HTML document in response everytime to all connected clients  
  response=html 
  connection_socket.send(response)
  
  #Closing the socket
  connection_socket.close() 
