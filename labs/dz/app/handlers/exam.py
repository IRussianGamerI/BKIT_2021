import os

from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

available_exam_subjects = ["Физика", "ТВиМС"]
available_exam_tickets = ["1", "2", "3", "4", "5"]

cur_path = os.path.dirname(os.path.abspath(__file__))


class ChooseExam(StatesGroup):
    waiting_for_exam_subject = State()
    waiting_for_exam_ticket = State()


async def exam_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for subject in available_exam_subjects:
        keyboard.add(subject)
    await message.answer("Выберите экзаменационный предмет:", reply_markup=keyboard)
    await ChooseExam.waiting_for_exam_subject.set()


async def exam_chosen(message: types.Message, state: FSMContext):
    if not is_subject(message.text):
        await message.answer("Выберите экзаменационный предмет, используя кнопки ниже.")
        return
    await state.update_data(chosen_exam=message.text)

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for ticket in available_exam_tickets:
        keyboard.add(ticket)
    # для простых шагов можно не указывать название состояния, обходясь next()
    await ChooseExam.next()
    await message.answer("Теперь выберите билет:", reply_markup=keyboard)


async def exam_ticket_chosen(message: types.Message, state: FSMContext):
    if not is_ticket(message.text):
        await message.answer("Выберите билет, используя кнопки ниже.")
        return
    user_data = await state.get_data()
    img = open(os.path.join(cur_path, '..', '..', 'img', 'exam', user_data['chosen_exam'] + message.text + '.png'),
               'rb')
    await message.answer_photo(img, f"Ваш предмет - {user_data['chosen_exam']}. Билет {message.text}.\n"
                                    f"Учите, а потом можете подготовиться к РК: /rk",
                               reply_markup=types.ReplyKeyboardRemove())
    await state.finish()


def register_handlers_exam(dp: Dispatcher):
    dp.register_message_handler(exam_start, commands="exam", state="*")
    dp.register_message_handler(exam_chosen, state=ChooseExam.waiting_for_exam_subject)
    dp.register_message_handler(exam_ticket_chosen, state=ChooseExam.waiting_for_exam_ticket)


def is_ticket(text):
    return text in available_exam_tickets


def is_subject(text):
    return text in available_exam_subjects
