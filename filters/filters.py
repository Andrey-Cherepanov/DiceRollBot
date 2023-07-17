from aiogram.filters import BaseFilter
from string import digits

class IsRoll(BaseFilter):
    def __init__(self):
        pass

    async def __call__(self, message):
        text = message.text
        allowed_chars = ''.join(digits) + 'dkK +-/*'
        for c in text:
            if c not in allowed_chars:
                return False
        if text.count('d') != 1:
            return False
        result = (text[0] in digits and 'd' in text) or (text[0] == 'd')
        return result
