from aiogram import Dispatcher
from aiogram.types import Message


async def user_start(message: Message):
<<<<<<< HEAD
    await message.reply("Hello, user!")
=======
    print(message)
>>>>>>> 12f5b35e53a1b298bc03d28b8284799360e5e4cd


def register_user(dp: Dispatcher):
    dp.register_message_handler(user_start, commands=["start"], state="*")
