from aiogram import types, Bot
from src.utils import censore, get_full_name, get_link
from db import funcs

from config import STRING

answer = STRING["explicit"]


async def p__censor(event: types.Message, bot: Bot):
    if funcs.is_protected(event.chat.id, "antiexplicit"):
        if getattr(event, "text", False):
            text = censore(event.text)
            if text:
                await bot.send_message(
                    event.chat.id,
                    answer.format(
                        get_link(event.from_user), get_full_name(event.from_user), text
                    ),
                    message_thread_id=getattr(event, "message_thread_id", None),
                )
                await event.delete()
        if getattr(event, "caption", False):
            text = censore(event.caption)
            if text:
                await event.delete()
                await event.answer(
                    f"🤐 Пожалуйста без таких выражений <b>{get_full_name(event.from_user)}</b>!"
                )
