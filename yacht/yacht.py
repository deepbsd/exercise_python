# Score categories
# Change the values as you see fit

def full_house(dice):
    if len(set(dice)) == 2:
        num1 = tuple(sorted(set(dice)))[0]
        if dice.count(num1) in (2,3): return sum(dice)
    return 0

def four_kind(dice):
    if len(set(dice)) <= 2:
        num1 = tuple(sorted(set(dice)))[0]
        try:
            num2 = tuple(sorted(set(dice)))[1] 
        except:
            IndexError
        if dice.count(num1) in (4,5): return 4 * num1 
        else: return 4 * num2
    return 0

YACHT = lambda dice: 50 if len(set(dice)) == 1 else 0
ONES = lambda dice: 1 * dice.count(1) if dice.count(1) >= 1 else 0
TWOS = lambda dice: 2 * dice.count(2) if dice.count(2) >= 1 else 0
THREES = lambda dice: 3 * dice.count(3) if dice.count(3) >= 1 else 0
FOURS = lambda dice: 4 * dice.count(4) if dice.count(4) >= 1 else 0
FIVES = lambda dice: 5 * dice.count(5) if dice.count(5) >= 1 else 0
SIXES = lambda dice: 6 * dice.count(6) if dice.count(6) >= 1 else 0
FULL_HOUSE = lambda dice: full_house(dice)
FOUR_OF_A_KIND = lambda dice: four_kind(dice)
LITTLE_STRAIGHT = lambda dice: 30 if sorted(dice) == [1,2,3,4,5] else 0
BIG_STRAIGHT = lambda dice: 30  if sorted(dice) == [2,3,4,5,6] else 0
CHOICE = lambda dice: sum(dice)


def score(dice, category):
    return category(dice)
