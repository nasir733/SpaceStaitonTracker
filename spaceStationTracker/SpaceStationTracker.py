import requests
import webbrowser
import time
import turtle

screen = turtle.Screen()
screen.setup(8192,4096)
screen.bgpic('map.gif')
turtle.mainloop()



'''astronaut_data= 'http://api.open-notify.org/astros.json'

#result=requests.get(astronaut_data).json()
#print(result)
#print(f"People in space {result['number']}")

#for person in result['people']:
    #print(person['name'] + 'in ' + person['craft'])

iss_location= 'http://api.open-notify.org/iss-now.json'


while True:
    result=requests.get(iss_location).json()
    #print(result)
    timestamp= result['timestamp']
    lat=result['iss_position']['latitude']
    lon=result['iss_position']['longitude']
    print( str(timestamp)+ ' '+ lat +' '+ lon)
    time.sleep(.1)



maps=f"http://maps.google.com/?q={lat},{lon}"

webbrowser.open_new_tab(maps)'''