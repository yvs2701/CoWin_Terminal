import requests
from datetime import date
import time
from playsound import playsound


def findByPin(pin: int, min_age: int, max_age: int, urlParams: str = "") -> bool:
    '''Check the availibility of the vaccines in the specified district'''
    # fetch data
    today = date.today()
    URL = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode={}&date={}'.format(pin, today.strftime("%d-%m-%Y"))
    URL = URL + urlParams
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

    # parse data
    data = requests.get(URL, headers=headers)
    response_json = data.json()
    results = response_json["sessions"]
    
    # print data
    counter = 0
    ### CoWin APIs started malfunction and url param for vaccine was not working so this is an alternative
    # search for COVISHIELD
    if (urlParams == 'COVISHIELD'):
        for result in results:
            if((result["available_capacity"] > 0) and (result["min_age_limit"] >= min_age) and (result["min_age_limit"] < max_age) and result["vaccine"] == "COVISHIELD"):
                counter += 1
                print('name:    ', result["name"])
                print('pincode: ', result["pincode"])
                print('vaccine: ', result["vaccine"])
                print('min age: ', result["min_age_limit"])
                print('SLOTS:   ', result["available_capacity"])
                print() # prints \n
        if(counter == 0):
            return False
        # else
        playsound('./sounds/ding.mp3') # notify user
        return True
    # search for COVAXIN
    elif (urlParams == 'COVAXIN'):
        for result in results:
            if((result["available_capacity"] > 0) and (result["min_age_limit"] >= min_age) and (result["min_age_limit"] < max_age) and result["vaccine"] == "COVAXIN"):
                counter += 1
                print('name:    ', result["name"])
                print('pincode: ', result["pincode"])
                print('vaccine: ', result["vaccine"])
                print('min age: ', result["min_age_limit"])
                print('SLOTS:   ', result["available_capacity"])
                print() # prints \n
        if(counter == 0):
            return False
        # else
        playsound('./sounds/ding.mp3') # notify user
        return True
    else:
        for result in results:
            if((result["available_capacity"] > 0) and (result["min_age_limit"] >= min_age) and (result["min_age_limit"] < max_age)):
                counter += 1
                print('name:    ', result["name"])
                print('pincode: ', result["pincode"])
                print('vaccine: ', result["vaccine"])
                print('min age: ', result["min_age_limit"])
                print('SLOTS:   ', result["available_capacity"])
                print() # prints \n
        if(counter == 0):
            return False
        # else
        playsound('./sounds/ding.mp3') # notify user
        return True

# driver code
if __name__ == '__main__':
    while(findByPin(462001, 18) != True):
        time.sleep(5)
        findByPin(462001, 18)
