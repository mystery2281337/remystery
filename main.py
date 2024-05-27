from aiogram import Bot, Dispatcher, types, executor
from config import TELEGRAM_TOKEN
from keyboard.keyboards import get_keyboard_1, get_keyboard_2
from keyboard.key_inline import get_keyboard_inline


bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(bot)


async def set_commands(bot: Bot):
    commands = [
        types.BotCommand(command= '/start', description= 'Команда для того, чтобы запустить бота'),
        types.BotCommand(command='/help', description='Команда для того, чтобы узнать с чем может помочь бот'),
        types.BotCommand(command='/info', description='Команда для того, чтобы узнать информацию о боте'),
        types.BotCommand(command='/cancel', description='Команда для того, чтобы закончить диалог с ботом'),
        types.BotCommand(command='/exit', description='Команда для того, чтобы выйти из бота')
        ]

    await bot.set_my_commands(commands)


@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.reply('Привет, я твой первый эхо бот', reply_markup= get_keyboard_1())

@dp.message_handler(lambda message: message.text == 'Отправь фото кота')
async def button_1_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo='http://i1.wallbox.ru/wallpapers/main2/201730/mordocka-koska-vzglad-dikaa.jpg', caption= 'Вот тебе кот', reply_markup=get_keyboard_inline())



@dp.message_handler(lambda message: message.text == 'Перейти на следующую клавиатуру')
async def button_2_click(message: types.Message):
    await message.answer('Тут ты можешь попросить отправить фото собаки', reply_markup= get_keyboard_2())

@dp.message_handler(lambda message: message.text == 'Отправь фото собаки')
async def button_3_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo='https://st03.kakprosto.ru/images/article/2019/5/9/357356_5cd44215399af5cd44215399ee.jpeg', caption= 'Вот тебе собака')


@dp.message_handler(lambda message: message.text == 'Вернуться на 1 клавиатуру')
async def button_4_click(message: types.Message):
    await message.answer('Тут ты можешь попросить отправить фото кота', reply_markup= get_keyboard_1())



@dp.message_handler(commands='help')
async def help(message: types.Message):
    await message.reply('Я могу тебе помочь тебе с ....')

@dp.message_handler(commands='info')
async def info(message: types.Message):
        await message.reply('Привет, тут есть вся информация о боте')

@dp.message_handler(commands='cancel')
async def cancel(message: types.Message):
            await message.reply('Привет, наш диалог с вами на этом закончен')

@dp.message_handler(commands='exit')
async def exit(message: types.Message):
                await message.reply('Пока, увидимся в следующий раз!')

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

async def on_startup(dispatcher):
    await set_commands(dispatcher.bot)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates= True, on_startup= on_startup)

