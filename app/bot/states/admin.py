from aiogram.dispatcher.filters.state import State, StatesGroup


class NewsState(StatesGroup):
    title = State()
    description = State()
    image = State()
    confirm = State()