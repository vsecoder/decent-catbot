import time
import logging
import asyncio

from aiogram import Bot, types, Router
from aiogram.filters import Command
from src.utils import convert_time, get_full_name, get_link

from config import STRING

ban_text = STRING["ban"]
unban_text = STRING["unban"]

logger = logging.getLogger(__name__)

router = Router()


@router.message(Command(commands=["ban", "unban"]))
async def ban_handler(event: types.Message, bot: Bot):
    """
    /ban {time} {reason}

    need to reply to user
    """
    command = event.text.split()[0]
    try:
        member = await bot.get_chat_member(event.chat.id, event.from_user.id)
        if "administrator" == member.status or "creator" == member.status:
            if not event.reply_to_message:
                m = await event.reply(
                    f"♦️ <b>Ошибка, команда должна быть в ответ на сообщение</b>\n\nПример: <code>/ban 1d flood</code> or <code>/unban</code>"
                )
                await asyncio.sleep(5)
                await m.delete()
                await event.delete()
                return

            args = event.text.replace(command, "").split(" ", 2)
            if args[0] == "":
                args.remove("")

            if command == "/ban":
                if len(args) != 2:
                    m = await event.reply(
                        f"♦️ <b>Ошибка, текст аргументов</b>\n\nПример: <code>/ban 1d flood</code> or <code>/unban</code>"
                    )
                    await asyncio.sleep(5)
                    await m.delete()
                    await event.delete()
                    return

                t = convert_time(args[0])
                await bot.kick_chat_member(
                    chat_id=event.chat.id,
                    user_id=event.reply_to_message.from_user.id,
                    until_date=time.time() + t,
                )
                await event.reply(
                    ban_text.format(
                        get_link(event.reply_to_message.from_user),
                        get_full_name(event.reply_to_message.from_user),
                        t / 60,
                        args[1],
                    )
                )

            if command == "/unban":
                await bot.unban_chat_member(
                    chat_id=event.chat.id,
                    user_id=event.reply_to_message.from_user.id,
                )
                m = await event.reply(
                    unban_text.format(
                        get_link(event.reply_to_message.from_user),
                        get_full_name(event.reply_to_message.from_user),
                    )
                )
                await asyncio.sleep(5)
                await m.delete()
                await event.delete()
    except Exception as e:
        logger.error(e)
        m = await event.reply(
            f"♦️ <b>Ошибка, проверьте права бота, и правильность команды</b>\n\nПример: <code>/ban 1d flood</code> or <code>/unban</code>"
        )
        await asyncio.sleep(5)
        await m.delete()
        await event.delete()
        return
