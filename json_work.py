import json 

'''
    Read a json from file update value and save into same file.
'''
from warnings import catch_warnings

try:
    file = open('simple/city.json', 'r');

    strJson = file.read();

    print('json data = {}'.format(strJson))
    
    cityJson = json.loads(strJson)
    
    print(f'id of city is: {cityJson["cityId"]} and name of city is: {cityJson["name"]} and pincode of city is: {cityJson["zipcode"]}' )
    
#     update the value
    cityJson["name"] = 'varanasi'
    cityJson['zipcode'] = '221001'
    
    print(f'id of city is: {cityJson["cityId"]} and name of city is: {cityJson["name"]} and pincode of city is: {cityJson["zipcode"]}' )
    
#     Write date into new file
    file = open('simple/city.json','w')
    strJson = json.dumps(cityJson);
    file.write(strJson)
    
    file.close();
except FileNotFoundError:
    print('file not found')

    
