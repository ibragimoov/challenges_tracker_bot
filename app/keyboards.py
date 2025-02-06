from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
import requests

menu_reply_markup = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Главная'), KeyboardButton(text='Новости')],
    [KeyboardButton(text='Помощь')],
], resize_keyboard=True)
