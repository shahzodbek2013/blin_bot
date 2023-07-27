import logging


from aiogram import Bot, Dispatcher, executor, types
API_TOKEN = '6141553139:AAFwM5w7NEFv7sBvQ4y2dJ4vVvEkzu7JqMQ'


logging.basicConfig(level=logging.INFO)


bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)




@dp.message_handler(commands=['start'])
async def start_bot (message: types.message):
    await message.answer("salom")


if __name__ == '__main__':
    executor.start_polling(dp)
