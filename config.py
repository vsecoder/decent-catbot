"""
Bot configs and texts
"""

BOT = {
    "id": 5504395725,
    "token": "5504395725:AAFmjuz9M54hJLJRug3meYE4F54wDhQJKfI",
    "name": "A decent cat🐈",
    "version": "2.5.3",
    "description": "A bot for multifunctional chat moderation.",
    "parse_mode": "HTML",
    "owner": "@vsecoder",
    "username": "decent_catbot",
}

STRING = {
    "start": "Привет, <b>{}</b> 👋\n\nДобавьте меня в чат, и выдайте права администратора, остальное расскажу по мере поступления!",
    "ban": '🔒 <b><a href="{}">{}</a> забанен на {} минут. Причина: </b><i>{}</i>',
    "unban": '🔑 <b><a href="{}">{}</a> отбанен</b>',
    "mute": '🔇 <b><a href="{}">{}</a> замучен на {} минут</b>\nПричина: {}',
    "unmute": '🔈 <b><a href="{}">{}</a> отмучен</b>',
    "warn": '👮‍♂️ <b><a href="{}">{}</a></b> получил {}/7 предупреждение\nПричина: <b>{}</b>',
    "warns": '👮‍♂️ <b><a href="{}">{}</a></b> имеет {}/7 предупреждений',
    "nsave": "💼 <b>Заметка </b><code>{}</code><b> сохранена!</b>",
    "nstop": "💼 <b>Заметка </b><code>{}</code><b> удалена!</b>",
    "notes": "💼 <b>Заметки:</b>\n",
    "explicit": '🤐 <a href="{}">{}</a>:\n <blockquote>{}</blockquote>',
    "welcome_bot": "🧐 <b>Хм, а тут уютненько, жду <u>права администратора</u>, а чтобы начать использовать бота, напишите сюда <code>/protects</code>!</b>",
    "protect": "🛡 <b>Защита {} {}</b>",
    "report": '🚨 <b>Жалоба на пользователя</b><a href="{}">⠀</a><a href="{}">{}</a>:\n<blockquote>{}</blockquote>',
}

PROTECTS = [
    {"name": "AntiTagAll"},
    {"name": "Welcome"},
    {"name": "AntiRaid"},
    {"name": "AntiChannel"},
    {"name": "AntiGIF"},
    {"name": "AntiNSFW"},
    {"name": "AntiFlood"},
    {"name": "AntiExplicit"},
    {"name": "BanNinja"},
]
