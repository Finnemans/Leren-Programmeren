import time
from termcolor import colored
from data import *
from math import ceil

##################### O03 #####################

def copper2silver(amount:int) -> float:
    return round(amount / 10, 2)

def silver2gold(amount:int) -> float:
    return round(amount / 5, 2)

def copper2gold(amount:int) -> float:
    silver = copper2silver(amount)
    gold = silver2gold(silver)
    return round(gold, 2)

def platinum2gold(amount:int) -> float:
    return round(amount * 25, 2)

def getPersonCashInGold(personCash:dict) -> float:
    cash = 0
    for money in personCash:
        if money == 'copper':
            cash += copper2gold(personCash[money])
        if money == 'silver':
            cash += silver2gold(personCash[money])
        if money == 'gold':
            cash += (personCash[money])
        if money == 'platinum':
            cash += platinum2gold(personCash[money])
    return round(cash, 2)

##################### O05 #####################

def getJourneyFoodCostsInGold(people:int, horses:int) -> float:
    foodCost = COST_FOOD_HUMAN_COPPER_PER_DAY * people
    horseCost = COST_FOOD_HORSE_COPPER_PER_DAY * horses
    return copper2gold((foodCost + horseCost) * JOURNEY_IN_DAYS)

##################### O06 #####################

def getFromListByKeyIs(list:list, key:str, value:any) -> list:
    newList = []
    for keys in list:
        if key in keys and keys[key] == value:
            newList.append(keys)
    return newList

def getAdventuringPeople(people:list) -> list:
    return getFromListByKeyIs(people, 'adventuring', True)

def getShareWithFriends(friends:list) -> list:
    return getFromListByKeyIs(friends, 'shareWith', True)

def getAdventuringFriends(friends:list) -> list:
    adventuringFriends = getAdventuringPeople(friends)
    return getShareWithFriends(adventuringFriends)

##################### O07 #####################

def getNumberOfHorsesNeeded(people:int) -> int:
    return ceil(people / 2)

def getNumberOfTentsNeeded(people:int) -> int:
    return (people + 2) // 3 

def getTotalRentalCost(horses:int, tents:int) -> float:
    horseCost = silver2gold(COST_HORSE_SILVER_PER_DAY) * horses * JOURNEY_IN_DAYS
    tentsCost = COST_TENT_GOLD_PER_WEEK * tents * ceil(JOURNEY_IN_DAYS / 7)
    return round(horseCost + tentsCost, 2)
##################### O08 #####################

def getItemsAsText(items:list) -> str:
    string = ''
    for index,item in enumerate(items):
        string += f"{item['amount']}{item['unit']} {item['name']}"
        if index < len(items) -2:
            string += ', '
        elif index < len(items) -1:
            string += ' & '
    return string

def getItemsValueInGold(items:list) -> float:
    total_value = 0.0
    
    for item in items:
        amount = item['amount']
        price_amount = item['price']['amount']
        price_type = item['price']['type']
        
        if price_type == 'copper':
            total_value += copper2gold(price_amount) * amount
        elif price_type == 'silver':
            total_value += silver2gold(price_amount) * amount
        elif price_type == 'gold':
            total_value += price_amount * amount
        elif price_type == 'platinum':
            total_value += platinum2gold(price_amount) * amount

    
    return round(total_value, 2)

##################### O09 #####################

def getCashInGoldFromPeople(people:list) -> float:
    totalCash = 0.0
    for person in people:
        if 'cash' in person:
            totalCash += getPersonCashInGold(person['cash'])
    return round(totalCash, 2)


##################### O10 #####################

def getInterestingInvestors(investors:list) -> list:
    interestedInvestors = []
    for investor in investors:
        if investor['profitReturn'] <= 10:
            interestedInvestors.append(investor)
    return interestedInvestors

def getAdventuringInvestors(investors:list) -> list:
    adventuringInvestors = []
    interestedInvestors = getInterestingInvestors(investors)
    
    for investor in interestedInvestors:
        if investor['adventuring']:
            adventuringInvestors.append(investor)
    return adventuringInvestors

def getTotalInvestorsCosts(investors:list, gear:list) -> float:
    if len(investors) > 0 and len(gear) > 0:
        interestedInvestors = len(getAdventuringInvestors(investors))
        tentsAmount = interestedInvestors
        horsesAmount = interestedInvestors
        rentalCost = getTotalRentalCost(horsesAmount, tentsAmount)
        foodCost = getJourneyFoodCostsInGold(interestedInvestors, horsesAmount)
        gearCost = getItemsValueInGold(gear) * interestedInvestors
        totalCost = gearCost + rentalCost + foodCost
    else:
        totalCost = 0.0
    return totalCost

##################### O11 #####################

def getMaxAmountOfNightsInInn(leftoverGold:float, people:int, horses:int) -> int:
    nights = 0
    while leftoverGold >= getJourneyInnCostsInGold(1, people, horses):
        leftoverGold -= getJourneyInnCostsInGold(1, people, horses)
        nights += 1
    return nights

def getJourneyInnCostsInGold(nightsInInn:int, people:int, horses:int) -> float:
    humanInnCost = silver2gold(COST_INN_HUMAN_SILVER_PER_NIGHT) * people 
    horsesInnCost = copper2gold(COST_INN_HORSE_COPPER_PER_NIGHT) * horses
    return round(nightsInInn * (humanInnCost + horsesInnCost), 2)

##################### O13 #####################

def getInvestorsCuts(profitGold:float, investors:list) -> list:
    cuts = []
    for investor in getInterestingInvestors(investors):
        cut = round((investor['profitReturn'] / 100) * profitGold, 2)
        cuts.append(cut)
    return cuts

def getAdventurerCut(profitGold:float, investorsCuts:list, fellowship:int) -> float:
    leftover = profitGold - sum(investorsCuts)
    if leftover <= 0 or fellowship <= 0:
        return 0.0
    return round(leftover / fellowship, 2)

##################### O14 #####################

def getEarnigs(profitGold:float, mainCharacter:dict, friends:list, investors:list) -> list:
    people = [mainCharacter] + friends + investors
    earnings = []

    # haal de juiste inhoud op
    adventuringFriends = getAdventuringFriends(friends)
    interestingInvestors = getInterestingInvestors(investors)
    adventuringInvestors = getAdventuringInvestors(investors)
    investorsCuts = getInvestorsCuts(profitGold, investors)
    goldCut = profitGold - sum(investorsCuts)
    cutforoneperson = goldCut / (len(adventuringFriends) + len(adventuringInvestors) + 1)
     # verdeel de uitkomsten
    for person in people:
        start = getPersonCashInGold(person['cash'])
        end = start
        if person == mainCharacter:
            end += cutforoneperson
            end += 10 * len(adventuringFriends)
        elif person in adventuringFriends:
            end += cutforoneperson
            end -= 10
        elif person in adventuringInvestors:
            end += cutforoneperson
            end += (profitGold * (person['profitReturn'] / 100))
        elif person in interestingInvestors:
            end += (profitGold * (person['profitReturn'] / 100))
        #code aanvullen

        earnings.append({
            'name'   : person['name'],
            'start'  : round(start, 2),
            'end'    : round(end, 2)
        })

    return earnings

##################### view functions #####################

def print_colorvars(txt:str='{}', vars:list=[], color:str='yellow') -> None:
    vars = map(lambda string, color=color: colored(str(string), color, attrs=['bold']) ,vars)
    print(txt.format(*vars))

def print_title(name:str) -> None:
    print_colorvars(vars=['=== [ {} ] ==='.format(name)], color='green')

def print_chapter(number:int, name:str) -> None:
    nextStep(2)
    print_colorvars(vars=['- CHAPTER {}: {} -'.format(number, name)], color='magenta')

def nextStep(secwait:int=1) -> None:
    print('')
    time.sleep(secwait)

def ifOne(amount:int, yes:str, no:str, single='een') -> str:
    text = yes if amount == 1 else no
    amount = single if amount == 1 else amount
    return '{} {}'.format(amount, text).lstrip()