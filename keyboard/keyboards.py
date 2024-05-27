from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_keyboard_1():
    Keyboard = ReplyKeyboardMarkup(resize_keyboard= True)
    button_1 = KeyboardButton('Отправь фото кота')
    button_2 = KeyboardButton('Перейти на следующую клавиатуру')
    Keyboard.add(button_1, button_2)
    return Keyboard
def get_keyboard_2():
    Keyboard_2 = ReplyKeyboardMarkup(resize_keyboard= True)
    button_3 = KeyboardButton('Отправь фото собаки')
    button_4 = KeyboardButton('Вернуться на 1 клавиатуру')
    Keyboard_2.add(button_3, button_4)
    return Keyboard_2