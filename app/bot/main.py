from aiogram import executor
import os
from .loader import dp
from .utils.notify_admins import on_startup_notify
from .utils.set_bot_commands import set_default_commands
from . import handlers,middlewares,filters 

async def on_startup(dispatcher):
    # Birlamchi komandalar (/star va /help)
    await set_default_commands(dispatcher)

    # Bot ishga tushgani haqida adminga xabar berish
    await on_startup_notify(dispatcher)


def start():
    executor.start_polling(dp, on_startup=on_startup)
