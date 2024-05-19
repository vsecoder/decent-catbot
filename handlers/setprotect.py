from aiogram import types, Bot, Router
from aiogram.filters import Command
from db import funcs

from config import STRING

anwer = STRING["protect"]
router = Router()


@router.message(Command(commands=["setprotect"]))
async def set_protect_handler(event: types.Message, bot: Bot):
    if event.chat.id != event.from_user.id:
        member = await bot.get_chat_member(event.chat.id, event.from_user.id)
        if "administrator" == member.status or "creator" == member.status:
            args = event.text.split(" ")
            if len(args) == 3:
                state = True if args[2] == "on" else False
                funcs.set_protected(event.chat.id, args[1].lower(), state)
                await event.answer(
                    anwer.format(args[1].lower(), "включена" if state else "отключена")
                )
            else:
                await event.answer("Неверный формат!")
