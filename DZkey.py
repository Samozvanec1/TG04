from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
# aiogram.types это библиотека для создания клавиатур и ещё элементов, ReplyKeyboardMarkup - это клавиатура с кнопками,
# KeyboardButton - кнопка в клавиатуре с текстом, InlineKeyboardMarkup - клавиатура с кнопками
# InlineKeyboardButton - кнопка в клавиатуре с текстом

from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

inline_keyboard_VB = InlineKeyboardMarkup(inline_keyboard=[
      [InlineKeyboardButton(text="Делай выбор", callback_data='VB')]
])

inline_keyboard_matrica = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Синяя таблетка", callback_data='sin')],
    [InlineKeyboardButton(text="Красная таблетка", callback_data='kr')]
])

inline_keyboard_zdraste = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="HI")],
    [KeyboardButton(text="Bye")]
] , resize_keyboard=True)

all = {"музыка":"https://storage1.lightaudio.ru/dm/3998b03d/2ea34339/СтимфониЯ%20—%20Ты%20не%20джедай.mp3",
       "видео":"https://rutube.ru/video/f84f80f2835973168b225ba3469219d9/?r=wd",
       "новости":"https://120.su/2024/08/18/на-свиноферме-проводят-свадьбы/"}


async def kiborg_keyboard():
    keyboard = InlineKeyboardBuilder()
    for key in all:
        keyboard.add(InlineKeyboardButton(text=key, url=all.get(key)))
    return keyboard.adjust(2).as_markup()