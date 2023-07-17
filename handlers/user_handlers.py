from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from filters.filters import IsRoll

from lexicon.lexicon import LEXICON

router: Router = Router()

# Handler for command /start
@router.message(Command(commands='start'))
async def process_start_command(message):
    await message.answer(LEXICON['/start'])

# Handler for command /help
@router.message(Command(commands='help'))
async def process_help_command(message):
    await message.answer(LEXICON['/help'])

@router.message(IsRoll())
async def process_roll_command(message):
    await message.answer('Вуху!')
