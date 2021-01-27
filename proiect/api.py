import requests

# url = 'https://jobs.github.com/positions.json?'
# headers = {}
# # params = {"description": 'python', "type": 'Full Time'}
# response = requests.request(method="GET", url=url, headers=headers, data=params)
# # print(response.json())
# for item in response.json():
#     pass
    # print(item['location'])
    # if item['location'] == 'Remote':
    # print(item['company'], "|", item['title'])

# url = 'http://newsapi.org/v2/everything'
url = 'http://newsapi.org/v2/everything?q=bitcoin&from=2021-01-01&sortBy=publishedAt&apiKey=8cb3f97dee184e6c9cf8e25c14d9f780'
headers = {}
params = {}
# params = {"apiKey": "8cb3f97dee184e6c9cf8e25c14d9f780", "q": "bitcoin", "from": "2021-01-01", "sortBy": "publishedAt", }
response = requests.request('GET', url=url, headers=headers, data=params)
print(response.json())

