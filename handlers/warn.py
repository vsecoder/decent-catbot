from aiogram import types, Bot, Router
from aiogram.filters import Command
from db import funcs

from config import STRING

warn = STRING["warn"]
warns = STRING["warns"]
router = Router()


@router.message(Command(commands=["warns", "warn"]))
async def warns_handler(event: types.Message, bot: Bot):
    pass
    # dev
    if event.chat.id != event.from_user.id:
        args = event.text.split(" ")
        command = args[0]
        member = await bot.get_chat_member(event.chat.id, event.from_user.id)
        if "administrator" == member.status or "creator" == member.status:
            if len(args) == 2:
                if command == "/warn" and event.reply_to_message:
                    funcs.create_warn(
                        event.chat.id, event.reply_to_message.from_user.id
                    )
                    await event.reply(warn.format())
