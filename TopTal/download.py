from imgurpython import ImgurClient
import json
import os
import logging
import time
from pathlib import Path
from urllib.request import urlopen
import sys


dl_logger = logging.getLogger(f"TopTal_multi.{__name__}")
types = {"image/jpeg", "image/png"}



def get_links():
    client_id = '40ce09cb894ea5d'
    client_secret = '8b991489b7be222b4b991a7acee3d360b392ec81'
    access_token = '35455cec21ebfa7f0f36b078a48526c69af3cbf2'
    refresh_token = 'a0a7659f3ff8052be32a397eff3087dc9463fd69'
    # Note since access tokens expire after an hour, only the refresh token is required (library handles autorefresh)
    client = ImgurClient(client_id, client_secret, access_token, refresh_token)
    album = client.gallery() #list
    links = []
    for item in album:
        try:
            if item.images[0]['type'] in types:
                links.append(item.images[0]['link'])
        except:
            dl_logger.error(f"on file {item.type} received: {sys.exc_info()[0]}")
    return links


def download_link(directory, link):
    """Takes 2 pos args: where to download to, url to download"""
    pos_url = Path(link)
    download_path = directory.joinpath(pos_url.name)
    content = urlopen(link)
    with open(download_path, "wb") as f:
        f.write(content.read())
    dl_logger.info(f"Downloaded: {link}")


def setup_download_dir():
    download_dir = Path("/home/wendiw/Xenial_Backup/PythonPlay/TopTal/images")
    if not download_dir.exists():
        download_dir.mkdir()
    return download_dir
