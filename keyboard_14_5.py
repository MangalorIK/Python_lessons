from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

kb = ReplyKeyboardMarkup(resize_keyboard=True)
button = KeyboardButton(text="Рассчитать")
button2 = KeyboardButton(text="Информация")
kb.add(button, button2)
kb.add(KeyboardButton(text="Купить"), KeyboardButton(text="Регистрация"))

inline_kb = InlineKeyboardMarkup(resize_keyboard=True)
button = InlineKeyboardButton(text="Рассчитать норму калорий", callback_data="calories")
button2 = InlineKeyboardButton(text="Формулы расчёта", callback_data="formulas")
inline_kb.add(button)
inline_kb.add(button2)

inline_kb_buy = InlineKeyboardMarkup(resize_keyboard=True)
inline_kb_buy.add(
    InlineKeyboardButton(text="Product1", callback_data="product_buying"),
    InlineKeyboardButton(text="Product2", callback_data="product_buying"),
    InlineKeyboardButton(text="Product3", callback_data="product_buying"),
    InlineKeyboardButton(text="Product4", callback_data="product_buying")
)

admin_panel = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Пользователи", callback_data='users')],
        [InlineKeyboardButton(text="Статистика", callback_data='stat')],
        [
            InlineKeyboardButton(text="Блокировка", callback_data='block'),
            InlineKeyboardButton(text="Разблокировка", callback_data='unblock')
        ]
    ]
)
