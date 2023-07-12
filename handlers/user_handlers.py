from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from lexicon.lexicon import LEXICON

router: Router = Router()

# Handler for command \help
@router.message(Command(commands='help'))
async def process_help_command(message):
    await message.answer(LEXICON['/help'])
