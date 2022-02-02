import requests
import settings
from jinja2 import Environment, FileSystemLoader

headers = {'x-api-key': settings.CATS_API_KEY}
cats = []
for _ in range(settings.NUM_CATS):
    response = requests.get(settings.CATS_API_URL)
    response = response.json()[0]
    cats.append({'id': response['id'], 'url': response['url']})

env = Environment(loader=FileSystemLoader('.'))
template = env.get_template(settings.SOURCE_TEMPLATE)
template.stream(cats=cats, img_size=settings.CATS_IMG_SIZE).dump(settings.TARGET_TEMPLATE)
