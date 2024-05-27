from aiogram import Bot, Dispatcher, types, executor
from config import TELEGRAM_TOKEN
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
    await message.reply('Привет, я твой первый эхо бот')

@dp.message_handler(commands='help')
async def help(message: types.Message):
    await message.reply('Я могу тебе помочь тебе с ....')

@dp.message_handler(commands='info')
async def start(message: types.Message):
        await message.reply('Привет, тут есть вся информация о боте')

@dp.message_handler(commands='cancel')
async def start(message: types.Message):
            await message.reply('Привет, наш диалог с вами на этом закончен')

@dp.message_handler(commands='exit')
async def start(message: types.Message):
                await message.reply('Пока, увидимся в следующий раз!')

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

async def on_startup(dispatcher):
    await set_commands(dispatcher.bot)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates= True, on_startup= on_startup)

