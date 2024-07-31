import requests
from nasa_spacex_api import download_image, fetch_nasa_token, fetch_image_ext
import argparse


def fetch_nasa_links(token, count=0):
    params = {
        'api_key': token
    }
    if count:
        params.update({'count': count})

    nasa_url = 'https://api.nasa.gov/planetary/apod'
    response = requests.get(nasa_url, params=params)
    response.raise_for_status()
    nasa_api_data = response.json()
    nasa_links = []
    if count:
        for nasa_api_row in nasa_api_data:
            nasa_links.append(nasa_api_row['url'])
    else:
        nasa_links.append(nasa_api_data['url'])
    return nasa_links


def fetch_nasa_images(token, count):
    nasa_links = fetch_nasa_links(token, count)
    for link_number, link in enumerate(nasa_links):
        file_name = f'nasa_image_{link_number}'
        download_image(link, file_name, 'images', fetch_image_ext(link))


def main():
    parser = argparse.ArgumentParser(description="download images to '.images' folder")

    parser.add_argument("count", nargs='?', default=0, help='the count to download NASA photos')
    args = parser.parse_args()

    nasa_token = fetch_nasa_token()
    fetch_nasa_images(token=nasa_token, count=args.count)  # Example count=2


if __name__ == '__main__':
    main()