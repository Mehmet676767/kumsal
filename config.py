import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID", "21194358"))
API_HASH = getenv("API_HASH", "9623f07eca023e4e3c561c966513a642")
BOT_TOKEN = getenv("BOT_TOKEN", "7164261117:AAFHmsgJrZDvxlsJwSLWj1DjvmA1r14HnaQ")
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://kurt67143:nays@cluster0.vjg7bma.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 500))
LOGGER_ID = int(getenv("LOGGER_ID", "-1002065943011"))
OWNER_ID = int(getenv("OWNER_ID", "6387858072"))
UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "",
)
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/masaldestekkanal")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/kumsalm𝗎zikk")
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))
STRING1 = getenv("STRING_SESSION", "BAGXyHkABQ2QLhrCYP8Jz7WRzYrYDaaY5o9V95zKw1w7e6H3_A6f5rywtQClctV8P1PncPyS0BsyumgWtiZLl6z_1BHTOc0kmXNy5LdNBWt_6tXwe9EDO_8ieiyWFmGx-ift095wT4W0G_a0W__YycgiGGCufZwLQiXEo9hYSYE7g6DdswY4tdfMoPml62Ps_8-DHtRS4PYaAlvP6hkh5riCqCaOk0XrpZR4Oqv6SdjB__2JOBwNeeQBzWVBSc5HQLGLOiwaRDFFXVwjD9Bh2U8MKS5WqvZ8bS6KLE0aEcN1hAaaJrmaKB9Te8UsX8fInRq3vOcZz3mDxtUtVRR429YRVigtFgAAAAGrSarFAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)



HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes
# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "1c21247d714244ddbb09925dac565aed")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "709e1a2969664491b58200860623ef19")

UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)
# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))

BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://telegra.ph/Jww-06-18"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://telegra.ph/Jww-06-18"
)
PLAYLIST_IMG_URL = "https://telegra.ph/Jww-06-18"
STATS_IMG_URL = "https://telegra.ph/Jww-06-18"
TELEGRAM_AUDIO_URL = "https://telegra.ph/Jww-06-18"
TELEGRAM_VIDEO_URL = "https://graph.org/file/6c6cce625f4a721569703.jpg"
STREAM_IMG_URL = "https://graph.org/file/6c6cce625f4a721569703.jpg"
SOUNCLOUD_IMG_URL = "https://graph.org/file/6c6cce625f4a721569703.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/6c6cce625f4a721569703.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/6c6cce625f4a721569703.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://graph.org/file/6c6cce625f4a721569703.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/6c6cce625f4a721569703.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
)
