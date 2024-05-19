from aiogram import types, Router
from aiogram.filters import Command

router = Router()


@router.message(Command(commands=["protects"]))
async def protects_handler(event: types.Message):
    if event.chat.id == event.from_user.id:
        return

    await event.reply(
        (
            "<b>🛡 My protects:</b>\n"
            "<b>🐵 <code>AntiTagAll</code> - Ограничивает тег всех участников</b>\n"
            "<b>👋 <code>Welcome</code> - Приветствует новых участников</b>\n"
            "<b>📯 <code>AntiChannel</code> - Запрещает написание сообщений от лица каналов</b>\n"
            "<b>🍓 <code>AntiNSFW</code> - Запрещает NSFW фото и стикеры</b>(now off)\n"
            "<b>⏱ <code>AntiFlood</code> - Запрещает флудить</b>(in dev)\n"
            "<b>😒 <code>AntiExplicit</code> - Запрещает материться </b>\n"
            "<b>👾 Админ: </b><code>/ban</code> <code>/mute</code> "
            "<code>/unban</code> <code>/unmute</code> <b>- Инструменты администраторов</b>\n"
            "<b>👮‍♂️ Предупреждения:</b> <code>/warn</code> <code>/warns</code>(in dev)\n"
            "<b>🗒 Заметки:</b> <code>/nsave</code> <code>/nstop</code> <code>/notes</code> - заметки\n"
            "<b>⏳ Настроить защиту:</b> <code>/setprotect {name} [on/off]</code>\n"
        ),
    )
