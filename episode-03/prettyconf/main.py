import requests
from jinja2 import Environment, FileSystemLoader

headers = {'x-api-key': ''}
cats = []
for _ in range(5):
    response = requests.get('https://api.thecatapi.com/v1/images/search', headers=headers)
    response = response.json()[0]
    cats.append({'id': response['id'], 'url': response['url']})

env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('cats.j2')
template.stream(cats=cats).dump('cats.html')
