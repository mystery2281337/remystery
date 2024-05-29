from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_keyboard_inline():
    Keyboard_inline = InlineKeyboardMarkup(row_width=2)
    but_inline = InlineKeyboardButton('Посмотреть',url='https://www.purina.ru/cats/breed-library?ysclid=lwowj1j2xc986344276')
    but_inline2 = InlineKeyboardButton('Посмотреть',url='https://www.purina.ru/cats/breed-library?ysclid=lwowj1j2xc986344276')
    Keyboard_inline.add(but_inline, but_inline2)
    return Keyboard_inline

