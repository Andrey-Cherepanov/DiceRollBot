from aiogram.filters import BaseFilter
import re

class IsRoll(BaseFilter):
    def __init__(self):
        pass

    async def __call__(self, message):
        return bool(re.fullmatch(r'/?\d*[dD]\d+([hHlL]?\d*)(\s?[+\-*/]\s?\d+)?', message.text))
