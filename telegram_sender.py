import telegram
from _secrets import telgram_bot_token, telegram_chat_id

async def send_telegram_msg(msg):
    bot = telegram.Bot(token=telgram_bot_token)
    await bot.sendMessage(chat_id=telegram_chat_id, text=msg)