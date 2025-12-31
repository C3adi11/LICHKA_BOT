import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command

logging.basicConfig(level=logging.INFO)

BOT_TOKEN = "8203442150:AAEz5gzvW-YnEhbyi8HlOUBmKGH4ZW14cOA"
ADMIN_ID = 8460927181

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer(
        "📨 *Анонимный бот для обратной связи*\n\n"
        "👇 *Пишите ниже то, что хотите передать администратору:*\n"
        "• Текст\n"
        "• Фото (можно с подписью)\n"
        "• Видео\n"
        "• Документы\n"
        "• Голосовые сообщения\n"
        "• Видеосообщения (кружки)\n\n"
        "🔒 *Всё отправляется анонимно!*",
        parse_mode="Markdown"
    )


@dp.message(F.photo)
async def handle_photo(message: types.Message):
    caption = message.caption or "Без описания"
    
    admin_text = f"""
📷 *АНОНИМНОЕ ФОТО*

📝 *Описание:*
{caption}
"""

    try:
        await bot.send_photo(
            chat_id=ADMIN_ID,
            photo=message.photo[-1].file_id,
            caption=admin_text,
            parse_mode="Markdown"
        )
        await message.answer("✅ *Фото отправлено анонимно!*", parse_mode="Markdown")
    except Exception as e:
        logging.error(f"Ошибка отправки фото: {e}")
        await message.answer("❌ *Ошибка отправки фото*", parse_mode="Markdown")


@dp.message(F.video)
async def handle_video(message: types.Message):
    caption = message.caption or "Без описания"
    
    admin_text = f"""
🎬 *АНОНИМНОЕ ВИДЕО*

📝 *Описание:*
{caption}
"""

    try:
        await bot.send_video(
            chat_id=ADMIN_ID,
            video=message.video.file_id,
            caption=admin_text,
            parse_mode="Markdown"
        )
        await message.answer("✅ *Видео отправлено анонимно!*", parse_mode="Markdown")
    except Exception as e:
        logging.error(f"Ошибка отправки видео: {e}")
        await message.answer("❌ *Ошибка отправки видео*", parse_mode="Markdown")


@dp.message(F.document)
async def handle_document(message: types.Message):
    admin_text = f"""
📄 *АНОНИМНЫЙ ДОКУМЕНТ*

📁 *Файл:* {message.document.file_name}
"""

    try:
        await bot.send_document(
            chat_id=ADMIN_ID,
            document=message.document.file_id,
            caption=admin_text,
            parse_mode="Markdown"
        )
        await message.answer("✅ *Документ отправлен анонимно!*", parse_mode="Markdown")
    except Exception as e:
        logging.error(f"Ошибка отправки документа: {e}")
        await message.answer("❌ *Ошибка отправки документа*", parse_mode="Markdown")


@dp.message(F.voice)
async def handle_voice(message: types.Message):
    admin_text = "🎤 *АНОНИМНОЕ ГОЛОСОВОЕ СООБЩЕНИЕ*"
    
    try:
        await bot.send_voice(
            chat_id=ADMIN_ID,
            voice=message.voice.file_id,
            caption=admin_text,
            parse_mode="Markdown"
        )
        await message.answer("✅ *Голосовое сообщение отправлено анонимно!*", parse_mode="Markdown")
    except Exception as e:
        logging.error(f"Ошибка отправки голосового: {e}")
        await message.answer("❌ *Ошибка отправки голосового сообщения*", parse_mode="Markdown")


@dp.message(F.video_note)
async def handle_video_note(message: types.Message):
    admin_text = "🎥 *АНОНИМНОЕ ВИДЕОСООБЩЕНИЕ (КРУЖОК)*"
    
    try:
        await bot.send_video_note(
            chat_id=ADMIN_ID,
            video_note=message.video_note.file_id
        )
        await bot.send_message(
            chat_id=ADMIN_ID,
            text=admin_text,
            parse_mode="Markdown"
        )
        await message.answer("✅ *Видеосообщение отправлено анонимно!*", parse_mode="Markdown")
    except Exception as e:
        logging.error(f"Ошибка отправки видеосообщения: {e}")
        await message.answer("❌ *Ошибка отправки видеосообщения*", parse_mode="Markdown")


@dp.message(F.text)
async def handle_text(message: types.Message):
    if message.text.startswith('/'):
        return
    
    admin_text = f"""
💬 *АНОНИМНОЕ СООБЩЕНИЕ*

📝 *Текст:*
{message.text}
"""

    try:
        await bot.send_message(
            chat_id=ADMIN_ID,
            text=admin_text,
            parse_mode="Markdown"
        )
        await message.answer("✅ *Сообщение отправлено анонимно!*", parse_mode="Markdown")
    except Exception as e:
        logging.error(f"Ошибка отправки текста: {e}")
        await message.answer("❌ *Ошибка отправки сообщения*", parse_mode="Markdown")


async def main():
    print("🤖 Анонимный бот запущен...")
    print(f"👑 Администратор: {ADMIN_ID}")
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
