from fastapi import FastAPI, Request
from aiogram import Bot, Dispatcher, types

TOKEN = "7569431053:AAFrUDbrplrz2Bh_2ZDBMtJxTeAIVa-MYbM"
WEBHOOK_PATH = "/webhook"
WEBHOOK_URL = f"https://dks-telegram-webapp-kirills-projects-2f8f2155.vercel.app{WEBHOOK_PATH}"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Сервер работает корректно!"}

@app.post(WEBHOOK_PATH)
async def webhook(request: Request):
    try:
        data = await request.json()
        telegram_update = types.Update(**data)
        await dp.process_update(telegram_update)
        return {"status": "ok"}
    except Exception as e:
        return {"error": str(e)}

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer("Привет! Вебхуки настроены.")
