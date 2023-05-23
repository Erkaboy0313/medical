from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from ...data.config import ADMINS
from ...loader import dp,bot
from ...states.admin import NewsState
from aiogram.dispatcher import FSMContext
from aiogram.types import ContentTypes
from ...keyboards.inline.user import confirm
from ....models import News
from django.core.files import File

import io
# from app.models import News

# from app.models import News
@dp.message_handler(CommandStart(), chat_id =ADMINS)
async def bot_start(message: types.Message):
    await message.answer(f"Salom, Yangilik kiritamizmi?!")

@dp.message_handler(lambda text: 'yes' in text.text ,chat_id =ADMINS)
async def start_news(message:types.Message):
    await message.answer("yangilik titleni kiriting")
    await NewsState.title.set()

@dp.message_handler(chat_id =ADMINS,state=NewsState.title)
async def set_title(message:types.Message,state:FSMContext):
    await state.update_data({"title":message.text})
    await message.answer('body kiriting')
    await NewsState.description.set()

@dp.message_handler(chat_id =ADMINS,state=NewsState.description)
async def set_description(message:types.Message,state:FSMContext):
    await state.update_data({"body":message.text})
    await message.answer('image yuklang')
    await NewsState.image.set()

@dp.message_handler(chat_id =ADMINS,state=NewsState.image,content_types=ContentTypes.PHOTO)
@dp.message_handler(chat_id =ADMINS,state=NewsState.image,content_types=ContentTypes.DOCUMENT)
async def set_image(message:types.Message,state:FSMContext):
    data = await state.get_data()
    text = f"{data['title']}\n {data['body']}"
    if message.photo:
        file_id = message.photo[0].file_id
        await message.answer_photo(file_id,text)
    elif message.document:
        file_id = message.document.file_id        
        await message.answer_document(file_id,text)
    await state.update_data({"photo":file_id})
    await message.answer('Tasdiqlaysimi?',reply_markup=confirm)
    await NewsState.confirm.set()

@dp.callback_query_handler(chat_id =ADMINS,state=NewsState.confirm)
async def confirmation(call:types.CallbackQuery,state:FSMContext):
    if call.data == 'yes':
        data = await state.get_data()
        image = await bot.get_file(data['photo'])
        file = "app/bot/handlers/users/"+image.file_path.split('/')[-1]
        await bot.download_file(image.file_path,file)
        local_file = open(file, "rb")
        djangofile = File(local_file)
        await News.objects.acreate(title = data['title'],description=data['body'],image = djangofile)
        local_file.close()
        await call.message.answer('tasdiqlandi')
    await bot_start(call.message)
    await state.finish()
        

