import urllib.request
import os.path
import shutil

BIG_PICTURE_URL = 'https://cdn.akamai.steamstatic.com/steam/apps/{steamid}/header.jpg'
BIG_PICTURE_PATH = '{shortcutid}.jpg'
BACKGROUND_URL = 'https://steamcdn-a.akamaihd.net/steam/apps/{steamid}/library_hero.jpg'
BACKGROUND_PATH = '{shortcutid}_hero.jpg'
LOGO_URL = 'https://steamcdn-a.akamaihd.net/steam/apps/{steamid}/logo.png'
LOGO_PATH = '{shortcutid}_logo.jpg'
COVERART_URL = 'https://steamcdn-a.akamaihd.net/steam/apps/{steamid}/library_600x900.jpg'
COVERART_PATH = '{shortcutid}p.jpg'


def download_assets_for_steamid(steamid):
    urllib.request.urlretrieve(BIG_PICTURE_URL.format(steamid=steamid),
                               "bigpicture.jpg")
    urllib.request.urlretrieve(BACKGROUND_URL.format(steamid=steamid),
                               "background.jpg")
    urllib.request.urlretrieve(LOGO_URL.format(steamid=steamid),
                               "logo.jpg")
    urllib.request.urlretrieve(COVERART_URL.format(steamid=steamid),
                               "coverart.jpg")


def link_artwork_to_users(shortcutid):
    userdata_folder = os.path.join(os.path.expanduser("~"), '.steam', 'steam', 'userdata')
    for userid in os.listdir(userdata_folder):
        grid_directory = os.path.join(userdata_folder, userid, 'config', 'grid/')
        if not os.path.exists(grid_directory):
            os.makedirs(grid_directory)
        shutil.copyfile('bigpicture.jpg', os.path.join(grid_directory, BIG_PICTURE_PATH.format(shortcutid=shortcutid)))
        shutil.copyfile('logo.jpg', os.path.join(grid_directory, LOGO_PATH.format(shortcutid=shortcutid)))
        shutil.copyfile('background.jpg', os.path.join(grid_directory, BACKGROUND_PATH.format(shortcutid=shortcutid)))
        shutil.copyfile('coverart.jpg', os.path.join(grid_directory, COVERART_PATH.format(shortcutid=shortcutid)))
