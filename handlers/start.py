from aiogram import types, Router
from aiogram.utils.keyboard import InlineKeyboardBuilder
from src.utils import get_full_name
from aiogram.filters import Command

from config import STRING


router = Router()


@router.message(Command(commands=["start"]))
async def start_handler(event: types.Message):
    return
    if event.chat.id == event.from_user.id:
        builder = InlineKeyboardBuilder()

        invite = types.InlineKeyboardButton(
            text="Добавить в чат", url="http://t.me/decent_catbot?startgroup=True"
        )
        url = types.InlineKeyboardButton(
            text="Политика конфиденциальности",
            url="https://telegra.ph/Politika-konfidencialnosti--Decent-catbot-06-13",
        )
        builder.add(*[invite, url])

        await event.answer(
            STRING["start"].format(get_full_name(event.from_user)),
            reply_markup=builder.as_markup(),
        )
