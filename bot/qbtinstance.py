import logging
import os
import requests

from .updater import updater
from qbt import CustomClient
from qbt import OfflineClient
from config import config

logger = logging.getLogger(__name__)

qbittorrent_url = os.environ.get('TORRENT_URL', config.qbittorrent.url)
qbittorrent_login = os.environ.get('TORRENT_LOGIN', config.qbittorrent.login)
qbittorrent_secret = os.environ.get('TORRENT_SECRET', config.qbittorrent.secret)

try:
    qb = CustomClient(qbittorrent_url, bot_username=updater.bot.username)
    qb.login(qbittorrent_login, qbittorrent_secret)
except requests.exceptions.ConnectionError as e:
    logger.error('exception while connecting to qbittorrent: %s', str(e))
    qb = OfflineClient()
