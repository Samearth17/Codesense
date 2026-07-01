import requests 

# api-endpoint 
URL = "https://www.example.com/page1"
  
# sending get request and saving the response as response object 
r = requests.get(url = URL) 
  
# extracting data in json format 
data = r.json() 
  
# extracting relevant data 
status = data['status'] 
sub_title = data['sub_title'] 
max_clients = data['max_clients'] 

# printing extracted data  
print("Status:", status) 
print("Sub Title:", sub_title)
print("Max Clients:", max_clients)