from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from filters.filters import IsRoll
from lexicon.lexicon import LEXICON
from services.rolling_scripts import parse_roll_command

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
    await message.reply(parse_roll_command(message.text.lstrip('/')))
