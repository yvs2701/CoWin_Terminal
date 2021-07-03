import requests

def getStates():
    URL = "https://cdn-api.co-vin.in/api/v2/admin/location/states"
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    data = requests.get(URL, headers= headers)
    results_json = data.json()
    stateList = results_json['states']
    for state in stateList:
        print(str(state['state_id'])+'.', state['state_name'])

if __name__ == '__main__':
    getStates()