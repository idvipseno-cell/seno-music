import os
from dotenv import load_dotenv

load_dotenv()

# Telegram API Credentials
API_ID = int(os.getenv("API_ID", "0"))
API_HASH = os.getenv("API_HASH", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")

# Bot Owner Info
OWNER_ID = int(os.getenv("OWNER_ID", "123456789")) # سينو
OWNER_USERNAME = os.getenv("OWNER_USERNAME", "idseno")
SUPPORT_CHANNEL = os.getenv("SUPPORT_CHANNEL", "senovip")

# NexGenBots API
API_KEY = os.getenv("API_KEY", "")
API_URL = "https://api.nexgenbots.xyz"

# Database
MONGO_DB_URI = os.getenv("MONGO_DB_URI", "")

# Assistant Account
STRING_SESSION = os.getenv("STRING_SESSION", "")

# Customization
START_IMG = os.getenv("START_IMG", "https://telegra.ph/file/your_default_image.jpg")
PLAY_IMG = os.getenv("PLAY_IMG", "https://telegra.ph/file/your_play_image.jpg")
ASSISTANT_LEAVE_TIME = 300 # 300 seconds as requested
