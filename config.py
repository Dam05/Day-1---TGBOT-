# config.py
import os

# Load environment variables (optional)
from dotenv import load_dotenv

load_dotenv()

# Add your bot token here
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "Your Token Goes here")
print(TELEGRAM_BOT_TOKEN)