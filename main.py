from fastapi import FastAPI, Request
from aiogram import Bot, Dispatcher, types

TOKEN = "7569431053:AAFrUDbrplrz2Bh_2ZDBMtJxTeAIVa-MYbM"
WEBHOOK_PATH = "/webhook"
WEBHOOK_URL = f"https://твой-домен.vercel.app{WEBHOOK_PATH}"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
app = FastAPI()

@app.on_event("startup")
async def startup():
    await bot.set_webhook(WEBHOOK_URL)

@app.post(WEBHOOK_PATH)
async def webhook(request: Request):
    data = await request.json()
    telegram_update = types.Update(**data)
    await dp.process_update(telegram_update)
    return {"status": "ok"}

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer("Привет! Вебхуки успешно настроены.")