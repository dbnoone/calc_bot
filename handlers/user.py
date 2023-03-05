from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext

from Course import Course


# @dp.message_handler(state=FSMAdmin.course_command)
async def show_course(message: types.Message, state: FSMContext):
    api = Course()
    course = api.get()
    await state.finish()
    await message.answer('Текущий курс = ' + str(course))


def register_user_handlers(dp: Dispatcher):
    dp.register_message_handler(show_course, lambda message: message.text == "Показать курс")
