from starlette.datastructures import CommaSeparatedStrings
from starlette.config import Config
from dotenv import load_dotenv
load_dotenv()
env = Config(".env")

# environs kutubxonasidan foydalanish

# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN ="6642650076:AAGaLvx34uhm7ubip--Zhw9GsTddCUI2QL4"  # Bot toekn
print(BOT_TOKEN)
ADMINS = list(env("ADMINS",cast=CommaSeparatedStrings))  # adminlar ro'yxati
IP = env("ip",cast=str)  # Xosting ip manzili
