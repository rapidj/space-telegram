import requests
from pathlib import Path
import os
from urllib.parse import urlsplit, unquote
from os.path import split, splitext
from dotenv import load_dotenv


def download_image(url, file_name, dir_name, extension='.jpg', token=None, params=None):
    full_file_name = f'{file_name}{extension}'
    Path(dir_name).mkdir(parents=True, exist_ok=True)
    file_path = os.path.join(dir_name, full_file_name)
    if token:
        params = {
            'api_key': token,
        }
    response = requests.get(url, params=params)
    response.raise_for_status()
    with open(file_path, 'wb') as file:
        file.write(response.content)


def fetch_image_ext(link):
    split_result = urlsplit(link)
    unquote_result = unquote(split_result.path)
    ext = splitext(split(unquote_result)[-1])[-1]
    return ext


def fetch_nasa_token():
    load_dotenv()
    token = os.environ['NASA_TOKEN']
    return token


def fetch_images_list(path):
    paths = []
    for root, dirs, files in os.walk(path):
        for file in files:
            paths.append(os.path.join(root, file))

    return paths
