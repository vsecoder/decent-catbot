from aiogram import Bot, types, Router
from aiogram.filters import Command
from src.utils import get_full_name, get_link

from config import STRING, BOT

report_text = STRING["report"]

router = Router()


@router.message(Command(commands=["report"]))
async def report_handler(event: types.Message, bot: Bot):
    """
    /report {reason}

    need to reply to user
    """

    if not event.reply_to_message:
        return await event.reply(
            "♦️ <b>Ошибка, команда должна быть в ответ на сообщение</b>\n\nПример: <code>/report flood</code>"
        )

    if event.reply_to_message.from_user.id == BOT["id"]:
        return await event.reply("♦️ <b>Ошибка, нельзя пожаловаться на бота</b>")

    if len(event.text.split()) == 1:
        return await event.reply(
            "♦️ <b>Ошибка, текст аргументов</b>\n\nПример: <code>/report flood</code>"
        )

    reason = event.text.split(" ", 1)[1]
    chat_admins = await bot.get_chat_administrators(event.chat.id)
    owner = [admin.user.id for admin in chat_admins if admin.status == "creator"][0]

    await event.reply(
        report_text.format(
            f"tg://user?id={owner}",
            get_link(event.reply_to_message.from_user),
            get_full_name(event.reply_to_message.from_user),
            reason,
        )
    )
