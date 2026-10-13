import asyncio
import re
from aiogram import Bot, Dispatcher, types

TOKEN = "8779974670:AAERWxtBQ8OflErSMSILyMSrHrlDdiExwh8"

TRIGGERS = {
    "да": "пизда",
    "нет": "пидора ответ",
    "твоя": "иди нахуй",
    "дa": "пизда",
    "нeт": "пидора ответ",
    "шлюхи аргумент": "аргумент не нужен пидор обнаружен",
    "кура": "цыпа цыпа цыпа",
    "ок": "мармок",
    "oк": "мармок",
    "нит": "питара атвит",
    "до": "после",
    "иди нахуй": "мут 5 минут",
    "пашов наху": "мут 5 минут",
    "пошол наху": "мут 5 минут",
}

# Стикеры: слово → file_id
STICKERS = {
    "гас": "CAACAgIAAxkBAAPoas3vroJAYk86VXaRdPYE6tJBoMYAAvenAAK7eMBKORU3FtyuDLQ9BA",
}

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message()
async def react_to_word(message: types.Message):
    if not message.text:
        return
    text = message.text.lower()

    # 1. Сначала проверяем фразы (где есть пробел)
    for trigger, reply in TRIGGERS.items():
        if " " in trigger and trigger in text:
            await message.reply(reply)
            return

    # 2. Разбиваем на слова
    words = re.findall(r"[а-яёa-z]+", text)

    # 3. Проверяем стикеры
    for word in words:
        if word in STICKERS:
            await message.reply_sticker(STICKERS[word])
            return

    # 4. Проверяем текстовые триггеры
    for word in words:
        if word in TRIGGERS:
            await message.reply(TRIGGERS[word])
            return

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
