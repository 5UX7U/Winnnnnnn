import os

BOT_TOKEN = os.environ.get("BOT_TOKEN", "5527406116:AAGM1dPjGBxEaiFM2WwXHjF-k30V7adAreQ")
SUDO = int(os.environ.get("SUDO", "5004499890"))
HEROKU = os.environ.get("HEROKU", "kdbdjdbfjffb")
APP_URL = "https://"+ HEROKU +".herokuapp.com/" + BOT_TOKEN
