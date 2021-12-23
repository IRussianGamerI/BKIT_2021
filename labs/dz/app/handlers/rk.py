import os

from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

available_rk_modules = ["МатСтат", "Правоведение", "Максвелл и ЭМ волны"]
available_rk_problem = ["1", "2", "3", "4", "5"]

cur_path = os.path.dirname(os.path.abspath(__file__))


class ChooseRK(StatesGroup):
    waiting_for_rk_module = State()
    waiting_for_rk_problem = State()


async def rk_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for module in available_rk_modules:
        keyboard.add(module)
    await message.answer("Выберите тему РК:", reply_markup=keyboard)
    await ChooseRK.waiting_for_rk_module.set()


# Обратите внимание: есть второй аргумент
async def rk_chosen(message: types.Message, state: FSMContext):
    if message.text not in available_rk_modules:
        await message.answer("Выберите тему РК, используя кнопки ниже.")
        return
    await state.update_data(chosen_rk=message.text)

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for problem in available_rk_problem:
        keyboard.add(problem)
    # Для простых шагов можно не указывать название состояния, обходясь next()
    await ChooseRK.next()
    await message.answer("Выберите номер задачи:", reply_markup=keyboard)


async def rk_problem_chosen(message: types.Message, state: FSMContext):
    if message.text not in available_rk_problem:
        await message.answer("Выберите номер задачи, используя кнопки ниже.")
        return
    user_data = await state.get_data()
    img = open(os.path.join(cur_path, '..', '..', 'img', 'rk', user_data['chosen_rk'] + message.text + '.png'),
               'rb')
    await message.answer_photo(img, f"Вы выбрали {user_data['chosen_rk']}. Задача №{message.text}\n"
                                    f"Хотите подготовиться к экзамену? - /exam",
                               reply_markup=types.ReplyKeyboardRemove())
    await state.finish()


def register_handlers_rk(dp: Dispatcher):
    dp.register_message_handler(rk_start, commands="rk", state="*")
    dp.register_message_handler(rk_chosen, state=ChooseRK.waiting_for_rk_module)
    dp.register_message_handler(rk_problem_chosen, state=ChooseRK.waiting_for_rk_problem)


def is_module(text):
    return text in available_rk_modules


def is_problem(text):
    return text in available_rk_problem
