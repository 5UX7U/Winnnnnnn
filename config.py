import os

BOT_TOKEN = os.environ.get("BOT_TOKEN", "5527406116:AAFwTTILY1ad3aCpbfvedlRkZohf4kFSIDM")
SUDO = int(os.environ.get("SUDO", "5004499890"))
HEROKU = os.environ.get("HEROKU", "")
APP_URL = "https://"+ HEROKU +".herokuapp.com/" + BOT_TOKEN
