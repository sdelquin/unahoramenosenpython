# Prettyconf 🚀
from prettyconf import config


def cast_img_size(value: str):
    width, height = value.strip().split('x')
    return int(width), int(height)


CATS_API_KEY = config('CATS_API_KEY', default='putyourapikeyhere')
NUM_CATS = config('NUM_CATS', default=3, cast=int)
CATS_API_URL = config('CATS_API_URL', default='https://api.thecatapi.com/v1/images/search')
SOURCE_TEMPLATE = config('SOURCE_TEMPLATE', default='cats.j2')
TARGET_TEMPLATE = config('TARGET_TEMPLATE', default='cats.html')
CATS_IMG_SIZE = config('CATS_IMG_SIZE', default=(250, 250), cast=cast_img_size)
