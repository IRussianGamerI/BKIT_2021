import os
import random
from aiogram import Bot, Dispatcher, executor, types

# Имя бота для поиска в Telegram: aiogram_iu5_34b_levbara_button_bot

# Токен бота
TOKEN = '5057157373:AAFNnDAHpzbf_oSEwzEs7qJXJrIoiM5JKSw'

mes_phys = 'Физика'
mes_prob = 'ТВиМС'

cur_path = os.path.dirname(os.path.abspath(__file__))

bot = Bot(token=TOKEN)

dp = Dispatcher(bot)


@dp.message_handler()
async def answer_all(message: types.Message):
    text = message.text

    if text == mes_phys:
        num = random.randint(1, 5)
        img = open(os.path.join(cur_path, 'img', 'phys' + str(num) + '.jpg'), 'rb')
        await bot.send_photo(message.from_user.id, img, "Учи физику")
    elif text == mes_prob:
        num = random.randint(1, 5)
        img = open(os.path.join(cur_path, 'img', 'prob' + str(num) + '.png'), 'rb')
        await bot.send_photo(message.from_user.id, img, "Учи тервер")
    else:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = [mes_phys, mes_prob]
        keyboard.add(*buttons)
        await message.answer('Нажми кнопочку. Экзамены на носу. Давай!', reply_markup=keyboard)


if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)
