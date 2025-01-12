#t.me/b2112_bot
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import requests
from bs4 import BeautifulSoup

v1 = """
Встала весна, чорну землю
Сонну розбудила,
Уквітчала її рястом,
Барвінком укрила;
І на полі жайворонок,
Соловейко в гаї
Землю, убрану весною,
Вранці зустрічають…
"""

v2 = """
Сонце гріє, вітер віє
З поля на долину,
Над водою гне з вербою
Червону калину,
На калині одиноке
Гніздечко гойдає.
А де ж дівся соловейко?
Не питай, не знає.
"""

v3 = """
Реве та стогне Дніпр широкий,
Сердитий вітер завива,
Додолу верби гне високі,
Горами хвилю підійма.
І блідний місяць на ту пору
Із хмари де-де виглядав,
Неначе човен в синім морі,
То виринав, то потопав.
Ще треті півні не співали,
Ніхто нігде не гомонів,
Сичі в гаю перекликались,
Та ясен раз у раз скрипів.
"""
v4 = """
За сонцем хмаронька пливе,
Червоні поли розстилає
І сонце спатоньки зове
У синє море: покриває
Рожевою пеленою,
Мов мати дитину.
"""
v5 = """
По діброві вітер виє,
Гуляє по полю,
Край дороги гне тополю
До самого долу.
Стан високий, лист широкий –
Нащо зеленіє?
Кругом поле, як те море
Широке синіє.
Та ясен раз у раз скрипів.
"""
v6 = """
Зоре моя вечірняя,
Зійди над горою,
Поговорим тихесенько
В неволі з тобою.
Розкажи, як за горою
Сонечко сідає,
Як у Дніпра веселочка
Воду позичає.
Як широка сокорина
Віти розпустила...
А над самою водою
Верба похилилась;
Аж по воді розіслала
Зеленії віти,
А на вітах гойдаються
Нехрещені діти.
"""
v7 = """
Садок вишневий коло хати,
Хрущі над вишнями гудуть,
Плугатарі з плугами йдуть,
Співають ідучи дівчата,
А матері вечерять ждуть.
Сім’я вечеря коло хати,
Вечірня зіронька встає.
Дочка вечерять подає,
А мати хоче научати,
Так соловейко не дає.
Поклала мати коло хати
Маленьких діточок своїх;
Сама заснула коло їх.
Затихло все, тілько дівчата
Та соловейко не затих.
"""
v8 = """
Село! І серце одпочине...
Село на нашій Україні –
Неначе писанка: село
Зеленим гаєм поросло;
Цвітуть сади, біліють хати,
А на горі стоять палати
Неначе диво, а кругом
Широколистиї тополі;
А там і ліс – і ліс, і поле,
І сині гори за Дніпром:
Сам Бог вітає над селом!..
"""
v9 = """
Червоний місяць аж горить,
З-за хмари тихо виступає.
І ніби гори оживають.
Дуби з діброви, мов дива,
У поле тихо одхожають.
І пугач пуга, і сова
З-під стріхи в поле вилітає,
А жаби крякають, гудуть.
"""
v10 = """
І небо невмите, і заспані хвилі;
І понад берегом геть-геть,
Неначе п’яний, очерет
Без вітру гнеться. Боже милий!
Чи довго буде ще мені
В оцій незамкнутій тюрмі,
Понад оцим нікчемним морем
Нудити світом? Не говорить,
Мовчить і гнеться, мов жива,
В степу пожовклая трава;
Не хоче правдоньки сказать,
А більше ні в кого спитать.
"""
list_comand = """
/help - назви всіх команд
/hello - Привітання
/sa1 - вірш Тарас Шевченка
/say2 - вірш Тарас Шевченка
/say3 - вірш Тарас Шевченка
/say4 - вірш Тарас Шевченка
/say5 - вірш Тарас Шевченка
/say6 - вірш Тарас Шевченка
/say7 - вірш Тарас Шевченка
/say8 - вірш Тарас Шевченка
/say9 - вірш Тарас Шевченка
/say10 - вірш Тарас Шевченка
"""

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(list_comand)

async def say1(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(v1)

async def say2(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(v2)

async def say3(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(v3)

async def say4(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(v4)

async def say5(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(v5)

async def say6(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(v6)

async def say7(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(v7)

async def say8(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(v8)

async def say9(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(v9)

async def say10(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(v10)


app = ApplicationBuilder().token("7898752027:AAGmXozS8zdZQ7VwgTvujIFaNWhul9rcQIo").build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("help", help))
app.add_handler(CommandHandler("say1", say1))
app.add_handler(CommandHandler("say2", say2))
app.add_handler(CommandHandler("say3", say3))
app.add_handler(CommandHandler("say4", say4))
app.add_handler(CommandHandler("say5", say5))
app.add_handler(CommandHandler("say6", say6))
app.add_handler(CommandHandler("say7", say7))
app.add_handler(CommandHandler("say8", say8))
app.add_handler(CommandHandler("say9", say9))
app.add_handler(CommandHandler("say10", say10))

app.run_polling()