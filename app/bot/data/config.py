from starlette.datastructures import CommaSeparatedStrings
from starlette.config import Config
from dotenv import load_dotenv
load_dotenv()
env = Config(".env")

# environs kutubxonasidan foydalanish

# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = env("BOT_TOKEN",cast=str)  # Bot toekn
ADMINS = list(env("ADMINS",cast=CommaSeparatedStrings))  # adminlar ro'yxati
IP = env("ip",cast=str)  # Xosting ip manzili
