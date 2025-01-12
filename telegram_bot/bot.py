#t.me/b2112_bot
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import requests
from bs4 import BeautifulSoup

v = """
Встала весна, чорну землю
Сонну розбудила,
Уквітчала її рястом,
Барвінком укрила;
І на полі жайворонок,
Соловейко в гаї
Землю, убрану весною,
Вранці зустрічають…
"""

list_comand = """
/help - назви всіх команд
/hello - Привітання
/sa1 - вірш Тарас Шевченку

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


app = ApplicationBuilder().token("7898752027:AAGmXozS8zdZQ7VwgTvujIFaNWhul9rcQIo").build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("hello", help))
app.add_handler(CommandHandler("hello", say1))
app.add_handler(CommandHandler("hello", say2))
app.add_handler(CommandHandler("hello", say3))
app.add_handler(CommandHandler("hello", say4))
app.add_handler(CommandHandler("hello", say5))
app.add_handler(CommandHandler("hello", say6))
app.add_handler(CommandHandler("hello", say7))
app.add_handler(CommandHandler("hello", say8))
app.add_handler(CommandHandler("hello", say9))
app.add_handler(CommandHandler("hello", say10))
app.run_polling()