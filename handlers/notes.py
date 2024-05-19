from aiogram import types, Bot, Router
from aiogram.filters import Command
from db import funcs
from src.utils import _process

from config import STRING

nsave = STRING["nsave"]
nstop = STRING["nstop"]
answer = STRING["notes"]

router = Router()


@router.message(Command(commands=["notes", "nsave", "nstop"]))
async def notes_handler(event: types.Message, bot: Bot):
    if event.chat.id != event.from_user.id:
        args = event.text.split(" ")
        command = args[0]
        member = await bot.get_chat_member(event.chat.id, event.from_user.id)
        if "administrator" == member.status or "creator" == member.status:
            if len(args) == 2:
                if command == "/nsave" and event.reply_to_message:
                    funcs.create_note(
                        event.chat.id, args[1], event.reply_to_message.text
                    )
                    await event.answer(nsave.format(args[1]))
                if command == "/nstop":
                    funcs.delete_note(event.chat.id, args[1])
                    await event.answer(nstop.format(args[1]))
        if len(args) == 1:
            if command == "/notes":
                msg = answer
                notes = funcs.get_notes(event.chat.id)
                for note in notes:
                    msg += f' - <code>#{_process(note["name"])}</code>\n'
                await event.answer(msg)
