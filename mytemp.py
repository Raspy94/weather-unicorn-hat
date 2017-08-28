from urllib2 import urlopen
import json
import time


apikey="yourapikey"
lati =""  #find your latitude and longitude from google maps. 
longi = ""

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

except KeyboardInterrupt:
 print("Exit")
