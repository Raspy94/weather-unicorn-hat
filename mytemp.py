from urllib2 import urlopen
import json
import time
import RPi.GPIO as GPIO

apikey="ac97a383cd2a3e1ecebdf197c4c7a5f9"
lati ="51.18466"  #find your latitude and longitude from google maps. 
longi = "0.08045"
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(27, GPIO.OUT) #blue
GPIO.setup(22, GPIO.OUT) #red
GPIO.setup(23, GPIO.OUT) #yellow
GPIO.setup(24, GPIO.OUT) #green

try:
#get the data from the api website
 url="https://api.forecast.io/forecast/"+apikey+"/"+lati+","+longi+"?units=si"
 oldTemp = 0          
#in case the Internet is not working: try it but then use the oldTemp just in case
 try:
  meteo=urlopen(url).read()
  meteo = meteo.decode('utf-8')
  weather = json.loads(meteo)        
  currentTemp = weather['currently']['temperature']        
  condition = weather['currently']['icon']
  wind = weather['currently']['windSpeed']
 except IOError:           
  currentTemp = oldTemp
    
  oldTemp = currentTemp #set oldTemp to last known temperature

 print currentTemp
 print condition
 print wind
 
 mytemp=str(condition) +" "+ str(currentTemp)+" "+str(wind)
 file = open('temp.txt','w') 
 
 file.write(mytemp) 

#NOT REQUIRED
 if wind > 6:
  GPIO.output(22,GPIO.HIGH)
  time.sleep(1)
  GPIO.output(22,GPIO.LOW)
  time.sleep(1)
  GPIO.output(22,GPIO.HIGH)
  time.sleep(1)
  GPIO.output(22,GPIO.LOW)
  time.sleep(1)
 else:
  GPIO.output(22,GPIO.LOW) 

 if 0 < currentTemp < 10:
  GPIO.output(27,GPIO.HIGH)
  GPIO.output(23,GPIO.LOW) 
  GPIO.output(22,GPIO.LOW) 
  GPIO.output(24,GPIO.LOW)
 
 if 10 < currentTemp < 17:
  GPIO.output(24,GPIO.HIGH)
  GPIO.output(23,GPIO.LOW)
  GPIO.output(22,GPIO.LOW)
  GPIO.output(27,GPIO.LOW)

 if 17 < currentTemp < 25:
  GPIO.output(23,GPIO.HIGH)
  GPIO.output(24,GPIO.LOW)
  GPIO.output(22,GPIO.LOW) 
  GPIO.output(27,GPIO.LOW)

 if currentTemp > 25: 
  GPIO.output(22,GPIO.HIGH)
  GPIO.output(23,GPIO.LOW)
  GPIO.output(24,GPIO.LOW)
  GPIO.output(27,GPIO.LOW)

except KeyboardInterrupt:
 print("Exit")
