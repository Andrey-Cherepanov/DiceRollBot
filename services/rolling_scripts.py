import random as r

class Roll:
    def __init__(self, current=None, maximum=20):
        if current == None:
            self.current = r.randint(1, maximum)
        else:
            self.current = current
        self.maximum = maximum

    def __str__(self):
        return f'roll: {self.current}/{self.maximum}'

    def to_tuple(self):
        return (self.current, self.maximum)

    def reroll(self):
        self.current = r.randint(1, self.maximum)

def single_roll(dice:int) -> Roll:
    return Roll(maximum=dice)

def list_roll(dice:int, n:int):
    return [Roll(maximum=dice) for _ in range(n)]

def up_list_roll(dice:int, n:int, top:int=1):
    roll_list = list_roll(dice=dice, n=n)
    maximum = sorted(roll_list, key = lambda x: x.current, reverse=True)[:top]
    return list(maximum), roll_list

def down_list_roll(dice:int, n:int, top:int=1):
    roll_list = list_roll(dice=dice, n=n)
    minimum = sorted(roll_list, key = lambda x: x.current)[:top]
    return minimum, roll_list
