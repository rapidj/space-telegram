# space-telegram
Publishing space images in Telegram

# How to start

Python3 should be already installed. Then use pip to install dependencies:

```bash
pip install -r requirements.txt
```

### Environment variables

- NASA_TOKEN <- generate your "API Key" on https://api.nasa.gov/
- TLG_BOT_TOKEN <- token for your Telegram bot
- TLG_CHANNEL_ID <- id of your Telegram channel
- DELAY_PUBL <- default delay in image publishing, hours. Default value = 4. (optional) 

### How to get

1. Crete a Telegram bot (please see the [documentation](https://core.telegram.org/bots/features#botfather))

2. Create a Telegram channel

3. Add your bot as administrator to your channel 

### Run

If you want to download the image of one SpaceX launch by ID to '.images' folder, just run fetch_spacex_images.py
script and pass the ID of the launch. 
If you omit the ID of the launch, all the images from the latest launch will be downloaded to '.images' folder.

```bash
$ python fetch_spacex_images.py '5eb87d47ffd86e000604b38a'  
```
   
If you want to download the image of the day from https://apod.nasa.gov/apod/astropix.html to '.images' folder, run 
fetch_nasa_images.py script. 
If you pass the count parameter, then the specified count of randomly chosen images will be downloaded. 

```bash
$ python fetch_nasa_images.py
$ python fetch_nasa_images.py 2  
```

If you want to download the full disc images of the Earth from https://epic.gsfc.nasa.gov/ to '.images' folder, run 
fetch_nasa_epic_images.py script and pass the specific date YYYY-MM-DD. 

```bash
$ python fetch_nasa_epic_images.py '2019-05-30'
```

If you want to publish images from ".images" folder to Telegram channel, run publish_images_bot.py script.
You can pass the delay in image publishing parameter in hours. 
Once all images have been published, images will start to be published in random order.

```bash
$ python publish_images_bot.py 0.0001
```

Instead of running all scripts separately, you can run one main.py script and pass it parameters:
- ID of the SpaceX launch
- the count of the images of the day from https://apod.nasa.gov/apod/astropix.html
- the specific date YYYY-MM-DD for images of the Earth from https://epic.gsfc.nasa.gov/.
In this case all the scripts will be run sequentially, one after another.

```bash
$ python main.py '5eb87d47ffd86e000604b38a' 2 0.0001
```