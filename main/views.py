from django.shortcuts import render
import json
import urllib.request
def index(request): 
    if request.method == 'POST': 
        city = request.POST['city'] 
      
        source = urllib.request.urlopen( 
            'http://api.openweathermap.org/data/2.5/weather?q=' 
                    + city + '&appid=c176a89d9538c82b6c41ce4546372c95').read() 
  
        # converting JSON data to a dictionary 
        
        list_of_data = json.loads(source) 
        kelvin_temp = (list_of_data['main']['temp'])


        celsius_temp = round(kelvin_temp - 273.15,2)
        # data for variable list_of_data 
        data = { 
            "country_code": str(list_of_data['sys']['country']), 
            "coordinate": str(list_of_data['coord']['lon']) + ', '
                        + str(list_of_data['coord']['lat']), 
            "temp":  str(celsius_temp) + 'C', 
            "pressure": str(list_of_data['main']['pressure']), 
            "humidity": str(list_of_data['main']['humidity']), 
        } 
        print(data) 
    else: 
        data ={} 
    return render(request, "main/index.html", data) 