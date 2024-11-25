import asyncio
import logging
from aiogram import Dispatcher, F, html, Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command, CommandStart
from aiogram.types import Message,FSInputFile
from trtoken import bot_token
# from googletrans import Translator
from deep_translator import GoogleTranslator
from gtts import gTTS

tr = GoogleTranslator()
dp = Dispatcher()
bot = Bot(token=bot_token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
logging.basicConfig(level=logging.INFO)
@dp.message(CommandStart())
async def StarBot(message: Message):
    ism = message.from_user.first_name
    await message.answer(f"Assalomu aleykum {ism} Bu bot orqali siz uzbek tilidgi so'zlarni ruscha tarijimasini topingiz mumkin. \nNImani qidirmoqchisiz kiriting:")

@dp.message(F.text)
async def TranslateText(message: Message):
    # uid = message.from_user.id
    # ism = message.from_user.first_name
    # user = message.from_user.username
    
    texs = message.text
    translat = tr.translate(text=texs, dest="ru")
    translat_audio = gTTS(text=translat.text, lang='ru', slow=False)
    translat_audio.save("audio.mp3")
    await message.reply(text=f"Rus tilida:\n{translat.text}")
    await message.reply_audio(audio=FSInputFile("audio.mp3"))
  
    # if uid !=5148276461:
    #     await bot.send_message(chat_id=5148276461, text=f"Ism: {ism}\nUser: {user}\nYozgan so'zi: {texs}")
    # else:
    #     print(f"{ism} yozgan so'zi: {texs}")

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except Exception as e:
        print(f"xato: {e}")




