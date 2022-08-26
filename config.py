## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "1ApWapzMBu0eHxNOYgATDwQlB-QqnxtfjFt9rQCOnKvFp2qh03hGD7-UTg-TGbV3yQrvA1HYF5rIyffxkWNcyjh-D-JV2-mRItVeF1NJ-OtwHPRnzdP5bKmotinCa2xEtvfifPEFcmtixcuknX9s8rFL9eaFTNklJAkYmng09z6LxmIcg5B8GiVnuu4Rk6oNweNUt9N5wArhSG1k-rvTdjNtvUlmPu5158l4q8AwkYF-n8lH2roPOhFgLY_nTAFaWfbOKll_hefSuFtYMOBSkDt_hGmnE83VkjpagVadrll-K1XA6rm40DoFrIh6obNAgtB9VbVZ0R_HdigjHT7SWXP7EMgz5lH0=")
BOT_TOKEN = getenv("BOT_TOKEN", "5324188888:AAHQp65-bKjclumEC9U46RNRRmustqjxkYc")
BOT_NAME = getenv("BOT_NAME", "بوت تشغيل الاغاني")
API_ID = int(getenv("API_ID", "17388553"))
API_HASH = getenv("API_HASH", "f79a7edc8fabb2aa4cb804829db06e14")
OWNER_NAME = getenv("OWNER_NAME", "سجاد")
OWNER_USERNAME = getenv("OWNER_USERNAME", "@U_V_U_U")
ALIVE_NAME = getenv("ALIVE_NAME", "سجاد")
BOT_USERNAME = getenv("BOT_USERNAME", "@U_V_U_U_bot")
OWNER_ID = getenv("OWNER_ID", "5338921544")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "@T_O_O_B")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "https://t.me/dfjkoiutdsd")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "https://t.me/HHHSSQO")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5338921544").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/407ce4c57a645c11f65c0.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/e22e5d1f0ccd57fa5f677.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/muntazer995/ing")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/402c519808f75bd9b1803.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/c74686f70a1b918060b8e.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/478f9fa85efb2740f2544.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/430dcf25456f2bb38109f.jpg")
