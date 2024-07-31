import telegram
from dotenv import load_dotenv
import argparse
import os
from nasa_spacex_api import fetch_images_list
import time
import random
import logging
import telegram.error as tlg_err


def fetch_tlg_settings():
    load_dotenv()
    token = os.environ['TLG_BOT_TOKEN']
    chat_id = os.environ['TLG_CHANNEL_ID']
    delay = float(os.environ.get('DELAY_PUBL', '4'))
    return token, chat_id, delay


def send_image(bot, chat_id, image):
    with open(image, 'rb') as image_to_send:
        bot.send_photo(chat_id=chat_id, photo=image_to_send)


def send_images(bot, chat_id, images_list, delay):
    for image in images_list:
        send_image(bot, chat_id, image)
        time.sleep(delay)


def main():
    tlg_token, tlg_chat_id, default_delay = fetch_tlg_settings()
    bot = telegram.Bot(token=tlg_token)

    parser = argparse.ArgumentParser(description="post images from '.images' folder to telegram channel")
    parser.add_argument("delay", nargs='?', type=float, default=default_delay,
                        help='Delay in image publishing, hours (positive float number). Default = 4h')
    args = parser.parse_args()
    delay = args.delay * 3600

    images_list = fetch_images_list('images')
    if not images_list:
        logging.error("No images in the '.images' folder")
        exit(1)

    while True:
        try:
            send_images(bot, tlg_chat_id, images_list, delay)
            random.shuffle(images_list)
        except tlg_err.NetworkError as e:
            logging.info('Problems with internet connection')
            time.sleep(2)


if __name__ == '__main__':
    main()
