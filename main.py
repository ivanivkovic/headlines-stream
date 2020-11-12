import requests, json, math, os, time, sys

url = "https://newscatcher.p.rapidapi.com/v1/latest_headlines"

requests_per_hour = 21
seconds_apart = math.floor(3600 / requests_per_hour)
#seconds_apart = 15 

querystring = {
        "lang": "en",
        "media": "True"
}

if len(sys.argv) > 1:
    querystring['topic'] = sys.argv[1]

headers = {
    'x-rapidapi-key': "556609e07emsh42b7bba41bc0146p11420cjsnfd72f6caa630",
    'x-rapidapi-host': "newscatcher.p.rapidapi.com"
}

while(True):

    os.system('clear')

    response = requests.request("GET", url, headers=headers, params=querystring)
    
    if response.status_code != 200:
        print('Newscatcher status: ' + str(response.status_code))

    else:
        json_object = json.loads(response.text)
    
        for article in json_object['articles']:
            print(article['published_date'] + ' ' + article['clean_url'] + ': ' + article['title'])

    time.sleep(seconds_apart)
