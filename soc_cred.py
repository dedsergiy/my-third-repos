from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
import random

bot = Bot(token='')
dp = Dispatcher(bot)
kb = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton('/помогити')
b2 = KeyboardButton('/кошкадевачка')
b3 = KeyboardButton('/чего')
b4 = KeyboardButton('/мискариса')
kb.add(b1).add(b2).insert(b3).insert(b4)

soc_cred = dict()

HELP = """
миска рис просто так не дать
"""


@dp.message_handler(commands=['начати'])
async def start_bot(message: types.Message):
    await message.answer('кошкадевочка наблюдать за тобой',
                         reply_markup=kb)
    if message.from_user.id not in soc_cred.keys():
        soc_cred[message.from_user.id] = 0
    await message.delete()


@dp.message_handler(commands=['помогити'])
async def get_help(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=HELP)


@dp.message_handler(commands=['чего'])
async def desc(message: types.Message):
    await message.reply('ты работать на завод кошкодевочка, ты кидать фото, кошкодевочка радоваться')


@dp.message_handler(commands=['кошкадевачка'])
async def give_photo(message: types.Message):
    await message.reply('тупой дурак не уметь социал рейтинк, кошкодевочка злитса')
    await bot.send_photo(chat_id=message.chat.id,
                         photo='https://sun9-54.userapi.com/impg/iwQBV1ZO0VrZrh-klOVSE9ZyICI5ZOEerrLb_Q/QXXAnzsdhj8.jpg?size=604x518&quality=96&sign=1ebdeca3fd30b159dea153f2a683c034&type=album')


@dp.message_handler(content_types='photo')
async def plus_sr(message: types.Message):
    plus = random.randrange(10, 100, 10)
    await message.reply(
        f'молодец миска риса не зря есть, ещё потрудись и кошкодевочка будет довольна, на {plus} социл кридит')
    soc_cred[message.from_user.id] += plus


@dp.message_handler(commands=['мискариса'])
async def miska(message: types.Message):
    if message.from_user.id not in soc_cred.keys():
        soc_cred[message.from_user.id] = 0
    if soc_cred[message.from_user.id] < 999:
        await bot.send_message(chat_id=message.from_user.id,
                               text=f'дурак, ты плоха работать, сегодня без миска риса, рабоатт ищё {1000 - soc_cred[message.from_user.id]}')
    elif soc_cred[message.from_user.id] > 1000:
        await bot.send_photo(chat_id=message.from_user.id,
                             photo='https://i-a.d-cd.net/2d8-ruyIcjKyG_VuOYDZhAOR-tA-1920.jpg')


if __name__ == '__main__':
    executor.start_polling(dp)
