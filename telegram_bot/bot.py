#t.me/b2112_bot
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import requests
from bs4 import BeautifulSoup

v1 = """
������ �����, ����� �����
����� ���������,
�������� �� ������,
�������� ������;
� �� ��� ����������,
��������� � ��
�����, ������ ������,
������ �����������
"""

v2 = """
����� ��, ���� ⳺
� ���� �� ������,
��� ����� ��� � ������
������� ������,
�� ����� �������
�������� �����.
� �� � ���� ���������?
�� �����, �� ���.
"""

v3 = """
���� �� ������ ���� �������,
�������� ���� ������,
������ ����� ��� �����,
������ ����� �����.
� ������ ����� �� �� ����
�� ����� ��-�� ��������,
������ ����� � ���� ���,
�� �������, �� �������.
�� ���� ��� �� ������,
ͳ��� ���� �� ������,
���� � ��� �������������,
�� ���� ��� � ��� ������.
"""
v4 = """
�� ������ ��������� �����,
������ ���� ��������
� ����� ��������� ����
� ��� ����: �������
������� �������,
��� ���� ������.
"""
v5 = """
�� ����� ���� ��,
����� �� ����,
���� ������ ��� ������
�� ������ ����.
���� �������, ���� ������� �
���� �����?
������ ����, �� �� ����
������ ���.
�� ���� ��� � ��� ������.
"""
v6 = """
���� ��� ��������,
ǳ��� ��� �����,
��������� ����������
� ����� � �����.
�������, �� �� �����
������� ���,
�� � ����� ���������
���� ������.
�� ������ ��������
³�� ����������...
� ��� ����� �����
����� ����������;
�� �� ��� ��������
����� ���,
� �� ���� ����������
�������� ���.
"""
v7 = """
����� �������� ���� ����,
����� ��� ������� ������,
�������� � ������� �����,
������� ����� ������,
� ����� �������� �����.
ѳ�� ������ ���� ����,
������� ������� ����.
����� �������� ����,
� ���� ���� �������,
��� ��������� �� ��.
������� ���� ���� ����
��������� ������ ����;
���� ������� ���� ��.
������� ���, ����� ������
�� ��������� �� �����.
"""
v8 = """
����! � ����� ��������...
���� �� ����� ����� �
������ �������: ����
������� ��� �������;
������ ����, ����� ����,
� �� ��� ������ ������
������ ����, � ������
����������� �����;
� ��� � �� � � ��, � ����,
� ��� ���� �� ������:
��� ��� ��� ��� �����!..
"""
v9 = """
�������� ����� �� ������,
�-�� ����� ���� �������.
� ��� ���� ��������.
���� � ������, ��� ����,
� ���� ���� ���������.
� ����� ����, � ����
�-�� ����� � ���� �����,
� ���� ��������, ������.
"""
v10 = """
� ���� �������, � ������ ����;
� ����� ������� ����-����,
������ �����, ������
��� ���� �������. ���� �����!
�� ����� ���� �� ���
� ���� ���������� ����,
����� ���� �������� �����
������ �����? �� ��������,
������� � �������, ��� ����,
� ����� ��������� �����;
�� ���� ���������� �������,
� ����� � � ���� �������.
"""
list_comand = """
/help - ����� ��� ������
/hello - ���������
/sa1 - ��� ����� ��������
/say2 - ��� ����� ��������
/say3 - ��� ����� ��������
/say4 - ��� ����� ��������
/say5 - ��� ����� ��������
/say6 - ��� ����� ��������
/say7 - ��� ����� ��������
/say8 - ��� ����� ��������
/say9 - ��� ����� ��������
/say10 - ��� ����� ��������
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