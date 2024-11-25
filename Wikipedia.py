import asyncio
import logging
from aiogram import Dispatcher, Bot, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from wtoken import token as token
import wikipedia
wikipedia.set_lang("uz")


dp = Dispatcher()
bot = Bot(token=token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
logging.basicConfig(level=logging.INFO)

@dp.message(CommandStart())
async def startbot(message: Message):
    name = message.from_user.full_name
    await message.answer(
        f"Assalomu Aleykum {name} \n"
        "Siz WIKEPEDIA botidasiz. Bu bot orqali wikepediadan ma'lumotlar izlashingiz  mumkin.\n"
        "Iltimos, matn kiriting."
    )

@dp.message(F.text)
async def wkipedia_text(message: Message):
    w= wikipedia.summary(message.text)
    await message.answer(w)

    
async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except Exception as e:
        print(f"xato: {e}")