import requests, json, math
from time import sleep

url = "https://newscatcher.p.rapidapi.com/v1/latest_headlines"

requests_per_hour = 21
seconds_apart = math.floor(60 * 60 / 21)

querystring = {
        "lang":"en",
        "media":"True"
}

headers = {
            'x-rapidapi-key': "556609e07emsh42b7bba41bc0146p11420cjsnfd72f6caa630",
            'x-rapidapi-host': "newscatcher.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)
json_object = json.loads(response.text)

while(True):
    if json_object['status'] == 'ok':
        for article in json_object['articles']:
            print(article['published_date'] + ' ' + article['clean_url'] + ': ' + article['title'])
    else:
        print('Newscatcher status: ' + json_object['status'])

    sleep(seconds_apart)
