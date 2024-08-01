import telegram
from dotenv import load_dotenv
import argparse
import os
from nasa_spacex_helpers import fetch_images_list
import time
import random
import logging
import telegram.error as tlg_err


def send_image(bot, chat_id, image):
    with open(image, 'rb') as image_to_send:
        bot.send_photo(chat_id=chat_id, photo=image_to_send)


def main():
    load_dotenv()
    tlg_token = os.environ['TLG_BOT_TOKEN']
    tlg_chat_id = os.environ['TLG_CHANNEL_ID']
    default_delay = float(os.environ.get('DELAY_PUBL', '4'))
    bot = telegram.Bot(token=tlg_token)

    parser = argparse.ArgumentParser(description="post images from '.images' folder to telegram channel")
    parser.add_argument("delay", nargs='?', type=float, default=default_delay,
                        help='Delay in image publishing, hours (positive float number). Default = 4h')
    args = parser.parse_args()
    delay = args.delay * 3600

    images = fetch_images_list('images')
    if not images:
        logging.error("No images in the '.images' folder")
        exit(1)

    while True:
        try:
            for image in images:
                send_image(bot, tlg_chat_id, image)
                time.sleep(delay)
            random.shuffle(images)
        except tlg_err.NetworkError as e:
            logging.info('Problems with internet connection')
            time.sleep(2)


if __name__ == '__main__':
    main()
