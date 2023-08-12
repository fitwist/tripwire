import os
from dotenv import load_dotenv

load_dotenv()

tg_token = str(os.getenv('TELEGRAM_TOKEN'))
TELEGRAM_BOT_NAME = str(os.getenv('TELEGRAM_BOT_NAME'))
ADMINS = str(os.getenv('BOT_ADMINS'))
DATABASE = str(os.getenv('DATABASE'))
SKIP_CHECK_TIME = bool(os.getenv('SKIP_CHECK_TIME'))
