import requests
from nasa_spacex_api import download_image, fetch_nasa_token
import argparse


def fetch_nasa_epic_links(token, date):
    params = {
        'api_key': token
    }
    response = requests.get(f'https://api.nasa.gov/EPIC/api/natural/date/{date}', params=params)
    response.raise_for_status()
    nasa_epic_api_data = response.json()
    nasa_epic_links = []
    for nasa_epic_api_row in nasa_epic_api_data:
        image_name = nasa_epic_api_row.get('image')
        image_datetime = nasa_epic_api_row.get('date').split()
        image_date = image_datetime[0]
        image_date = image_date.replace('-', '/')
        nasa_epic_link = f'https://api.nasa.gov/EPIC/archive/natural/{image_date}/png/{image_name}.png'
        nasa_epic_links.append(nasa_epic_link)
    return nasa_epic_links


def fetch_nasa_epic_images(token, date):
    nasa_links = fetch_nasa_epic_links(token, date)
    for link_number, link in enumerate(nasa_links):
        file_name = f'nasa_epic_image_{link_number}'
        download_image(link, file_name, 'images', '.png', token=token)


def main():
    parser = argparse.ArgumentParser(description="download images to '.images' folder")

    parser.add_argument("date", nargs='?', default='', help='the date (YYYY-MM-DD) to download NASA Epic photos')
    args = parser.parse_args()

    nasa_token = fetch_nasa_token()
    fetch_nasa_epic_images(token=nasa_token, date=args.date)  # Example date='2019-05-30'


if __name__ == '__main__':
    main()

