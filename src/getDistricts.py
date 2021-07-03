import requests

def getDist(stateNum):
    URL = 'https://cdn-api.co-vin.in/api/v2/admin/location/districts/{}'.format(stateNum)
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    data = requests.get(URL,headers= headers)
    response_json = data.json()
    stateList = response_json['districts']
    for state in stateList:
        print(str(state['district_id'])+'.', state['district_name'])

if __name__ == '__main__':
    getDist(20)