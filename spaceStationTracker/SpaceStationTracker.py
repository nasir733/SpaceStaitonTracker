import requests
import webbrowser
astronaut_data= 'http://api.open-notify.org/astros.json'

#result=requests.get(astronaut_data).json()
#print(result)
#print(f"People in space {result['number']}")

#for person in result['people']:
    #print(person['name'] + 'in ' + person['craft'])


iss_location= 'http://api.open-notify.org/iss-now.json'
result=requests.get(iss_location).json()
print(result)



timestamp= result['timestamp']
lat=result['iss_position']['latitude']
lon=result['iss_position']['longitude']
print( str(timestamp)+ ' '+ lat +' '+ lon)

maps=f"http://maps.google.com/?q={lat},{lon}"

webbrowser.open_new_tab(maps)