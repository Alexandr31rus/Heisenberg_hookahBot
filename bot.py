from aiogram import Bot, Dispatcher, executor, types



TOKEN_API = "5968756063:AAFxB3ZYXrpf9LjbSvC8HOR3ShL9BCLFNJw"
CHANNEL_ID=-1001677766887

HELP_COMMAND = """
/help  - список команд
/start - начать работу с ботом
"""

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

async def on_startup(_):
    print("Бот был успешно запущен!")


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.answer(text=HELP_COMMAND)


@dp.message_handler(commands=['start'])
async def help_command(message: types.Message):
    await message.answer(text='Здарова Ёптить, хули надо!?')
    await bot.send_sticker(message.from_user.id, sticker="CAACAgIAAxkBAAEIknhkOHBJQMNGnv0hbsLxFlND34YEMwACIgAD_1o4I3SbwbbrnT0XLwQ")
    await message.answer(text="Хммм.... наверное хочешь /Kalyanchik? 💨")

@dp.message_handler(commands=['Kalyanchik'])
async def help_command(message: types.Message):
    await message.answer(text="Ну тогда скорее звони по номеру +78005553535 и будет тебе счастье")

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
