import urllib.request

BIG_PICTURE_URL = 'https://cdn.akamai.steamstatic.com/steam/apps/{steamid}/header.jpg'
BIG_PICTURE_PATH = '{shortcutid}.{extension}'
BACKGROUND_URL = 'https://steamcdn-a.akamaihd.net/steam/apps/{steamid}/library_hero.jpg'
BACKGROUND_PATH = '{shortcutid}_hero.{extension}'
LOGO_URL = 'https://steamcdn-a.akamaihd.net/steam/apps/{steamid}/logo.png'
LOGO_PATH = '{shortcutid}_logo.{extension}'
COVERART_URL = 'https://steamcdn-a.akamaihd.net/steam/apps/{steamid}/library_600x900.jpg'
COVERART_PATH = '{shortcutid}p.{extension}'


def download_assets_for_steamid(steamid):
    urllib.request.urlretrieve(BIG_PICTURE_URL.format(steamid=steamid),
                               "bigpicture.jpg")
    urllib.request.urlretrieve(BACKGROUND_URL.format(steamid=steamid),
                               "background.jpg")
    urllib.request.urlretrieve(LOGO_URL.format(steamid=steamid),
                               "logo.jpg")
    urllib.request.urlretrieve(COVERART_URL.format(steamid=steamid),
                               "coverart.jpg")
