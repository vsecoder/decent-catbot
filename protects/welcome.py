from aiogram import types
from src.utils import get_full_name
from db.funcs import is_protected

from config import BOT, STRING


async def p__welcome(event: types.Message):
    if not is_protected(event.chat.id, "welcome"):
        return

    if getattr(event, "new_chat_members", None):
        if int(event.new_chat_member["id"]) != BOT["id"]:
            welcome_text = "👋 Приветствую, <b>{}</b> в чате <b>{}</b>!".format(
                get_full_name(event.new_chat_member), event.chat.title
            )
        else:
            welcome_text = STRING["welcome_bot"]

        await event.reply(
            welcome_text,
        )
