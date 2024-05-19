from handlers.ban import router as ban_handler
from handlers.mute import router as mute_handler
from handlers.protect import router as protect_handler
from handlers.protects import router as protects_handler
from handlers.start import router as start_handler
from handlers.setprotect import router as set_protect_handler
from handlers.notes import router as notes_handler
from handlers.report import router as report_handler

from aiogram import Router

router = Router()

router.include_router(ban_handler)
router.include_router(mute_handler)
router.include_router(protects_handler)
router.include_router(start_handler)
router.include_router(set_protect_handler)
router.include_router(notes_handler)
router.include_router(report_handler)
router.include_router(protect_handler)
