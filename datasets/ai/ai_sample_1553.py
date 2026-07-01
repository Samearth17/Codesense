import requests 
  
# api-endpoint 
URL = "https://www.example.com/api/v1/data"
  
# location given here 
  
# sending get request and saving the response as response object 
r = requests.get(url = URL) 
  
# extracting data in json format 
data = r.json() 
  
# extracting latitude, longitude and formatted address  
# of the first matching location 
# latitude = data['results'][0]['geometry']['location']['lat'] 
# longitude = data['results'][0]['geometry']['location']['lng'] 
# formatted_address = data['results'][0]['formatted_address'] 
  
# printing the output 
# print("Latitude:%s\nLongitude:%s\nFormatted Address:%s"
#       %(latitude, longitude,formatted_address))