import asyncio # импортируем библиотеку asyncio это необходимо для использования библиотеки aiogram
from aiogram import Bot, Dispatcher, F # из библиотеки aiogram импортируем необходимые модули, Bot это бот,
# Dispatcher - диспетчер, F - фильтры принимаемые ботом при получении сообщения
from aiogram.filters import CommandStart, Command # импортируем команды
from aiogram.types import Message, FSInputFile, CallbackQuery # импортируем типы сообщений и коллбеков


from config import TOKEN
import DZkey as kb # импортируем модуль с клавиатурами
import logging # импортируем модуль для логирования бота

logging.basicConfig(level=logging.INFO) # устанавливаем уровень логирования в консоли

bot = Bot(token=TOKEN) # создаем бота с токеном из переменной TOKEN
dp = Dispatcher() # создаем диспетчера


@dp.message(F.text == "HI")
async def hi(message: Message):
    await message.answer(f'Хай, {message.from_user.first_name}')


@dp.message(F.text == "Bye")
async def bye(message: Message):
    await message.answer(f'Бай, {message.from_user.first_name} , спи блин')

@dp.message(Command('dynamic'))
async def dynamic(message: Message):
    await message.answer(f'''Приешь синюю таблетку, {message.from_user.first_name} - и сказке конец. Ты проснёшься в своей постели
       и поверишь, что это был сон. Примешь красную таблетку - войдёшь в страну чудес Я покажу тебе, глубока ли кроличья нора.''', reply_markup=kb.inline_keyboard_VB)

@dp.callback_query(F.data == 'VB')
async def vb(callback: CallbackQuery):
    await callback.message.edit_text("ㅤ ", reply_markup=kb.inline_keyboard_matrica)

@dp.callback_query(F.data == 'sin')
async def sinyaa(callback: CallbackQuery):
    await callback.answer("Ты дома в постели, пора на работу", show_alert=True)

@dp.callback_query(F.data == 'kr')
async def kraska(callback: CallbackQuery):
    await callback.answer("Ты провалился в кроличью нору. С днём рождения", show_alert=True)


@dp.message(Command('links'))
async def links(message: Message):
    await message.answer('Жми пока не протухли ', reply_markup=await kb.kiborg_keyboard())

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(f'ЖМИ, {message.from_user.first_name}', reply_markup=kb.inline_keyboard_zdraste)



async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())