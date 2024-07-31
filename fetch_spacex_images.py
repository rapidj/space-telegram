import requests
import argparse
from nasa_spacex_api import download_image


def fetch_spacex_links(launch_id):
    response = requests.get(f"https://api.spacexdata.com/v5/launches/{launch_id}")
    response.raise_for_status()
    return response.json()['links']['flickr']['original']


def fetch_spacex_last_launch(launch_id='latest'):
    spacex_links = fetch_spacex_links(launch_id)
    for link_number, link in enumerate(spacex_links):
        file_name = f'spacex_image_{link_number}'
        download_image(link, file_name, 'images', '.jpg')


def main():
    parser = argparse.ArgumentParser(description="download images to '.images' folder")

    parser.add_argument("id", nargs='?', default='latest', help='id of required SpaceX launch')
    args = parser.parse_args()
    fetch_spacex_last_launch(args.id)  # Example '5eb87d47ffd86e000604b38a'


if __name__ == '__main__':
    main()

