from aiogram import types, Bot, Router
from src.utils import _process

from protects import welcome
from protects import antiexplicit
from protects import antichannel
from protects import antitagall

from db import funcs

router = Router()


@router.message()
async def protect_handler(event: types.Message, bot: Bot):
    if event.chat.id == event.from_user.id:
        return
    funcs.init_chat(event.chat.id)

    notes = funcs.get_notes(event.chat.id)
    for note in notes:
        if f"#{_process(note['name'])}" == event.text:
            await event.reply(f'{_process(note["text"])}')

    await welcome.p__welcome(event)

    await antichannel.p__antichannel(event)

    await antitagall.p__antitagall(event)

    await antiexplicit.p__censor(event, bot)
