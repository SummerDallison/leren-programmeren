import time, math
from termcolor import colored
from data import JOURNEY_IN_DAYS
from data import COST_FOOD_HUMAN_COPPER_PER_DAY, COST_FOOD_HORSE_COPPER_PER_DAY
from data import COST_TENT_GOLD_PER_WEEK, COST_HORSE_SILVER_PER_DAY
from data import COST_INN_HUMAN_SILVER_PER_NIGHT, COST_INN_HORSE_COPPER_PER_NIGHT

##################### O03 #####################

def copper2silver(amount:int) -> float:
    return round(amount / 10, 2)

def silver2gold(amount:int) -> float:
    return round(amount / 5, 2)

def copper2gold(amount:int) -> float:
    return silver2gold(copper2silver(round(amount, 2)))

def platinum2gold(amount:int) -> float:
    return round(amount * 25, 2)

#Deze functie berekent de totale waarde in goud op basis an de hoeveelheden koper, zilver, goud en platinum van een persoon
def getPersonCashInGold(personCash:dict) -> float:
    total_gold = 0
    total_gold += copper2gold(personCash['copper'])
    total_gold += silver2gold(personCash['silver'])
    total_gold += personCash['gold']
    total_gold += platinum2gold(personCash['platinum'])
    return round(total_gold, 2)

##################### O05 #####################

def getJourneyFoodCostsInGold(people: int, horses: int) -> float:
    total_cost_people = people * COST_FOOD_HUMAN_COPPER_PER_DAY * JOURNEY_IN_DAYS
    total_cost_horses = horses * COST_FOOD_HORSE_COPPER_PER_DAY * JOURNEY_IN_DAYS
    total_cost_gold = copper2gold(total_cost_people + total_cost_horses)
    return total_cost_gold

##################### O06 #####################

#Deze functie selecteert items uit een lijst van dictionaries op basis van een specifieke key-value
def getFromListByKeyIs(list:list, key:str, value:any) -> list:
    result = []
    for item in list:
        if key in item and item[key] == value:
            result.append(item)
    return result

def getAdventuringPeople(people:list) -> list:
    return getFromListByKeyIs(people, 'adventuring', True)

def getShareWithFriends(friends:list) -> list:
    return getFromListByKeyIs(friends, 'shareWith', True)

#Deze functie filtert een lijst van vrienden en geeft alleen de vrienden terug die avontuurlijk zijn en waarmee gedeeld wordt
def getAdventuringFriends(friends:list) -> list:
    adventuring_people = getAdventuringPeople(friends)
    share_with_friends = getShareWithFriends(friends)

    adventuring_friends = []
    for friend in adventuring_people:
        if friend in share_with_friends:
            adventuring_friends.append(friend)

    return adventuring_friends

##################### O07 #####################

def getNumberOfHorsesNeeded(people:int) -> int:
    return math.ceil(people / 2)

def getNumberOfTentsNeeded(people:int) -> int:
    return math.ceil(people / 3)

#Bereken de kosten (in goud) van de huur van de paarden en de tenten
def getTotalRentalCost(horses:int, tents:int) -> float:
    horse_cost = JOURNEY_IN_DAYS * horses * silver2gold(COST_HORSE_SILVER_PER_DAY)
    tent_cost = math.ceil(JOURNEY_IN_DAYS / 7) * tents * COST_TENT_GOLD_PER_WEEK
    total_cost_gold = horse_cost + tent_cost
    return round(total_cost_gold, 2)

##################### O08 #####################

#Deze functie zet een lijst van items om naar een tekst(str)
def getItemsAsText(items: list) -> str:
    item_texts = []
    for item in items:
        item_text = f"{item['amount']}{item['unit']} {item['name']}"
        item_texts.append(item_text)

    if len(item_texts) > 1: 
        last_item = item_texts.pop()
        return ', '.join(item_texts) + f" & {last_item}" 
    else:
        return item_texts[0]

#Deze functie berekent de totale waarde van de items in goud
def getItemsValueInGold(items:list) -> float:
    total_value_gold = 0.0
    for item in items:
        if item['price']['type'] == 'gold':
            total_value_gold += item['price']['amount'] * item['amount']
        elif item['price']['type'] == 'silver':
            total_value_gold += silver2gold(item['price']['amount'] * item['amount'])
        elif item['price']['type'] == 'copper':
            total_value_gold += copper2gold(item['price']['amount'] * item['amount'])
        elif item['price']['type'] == 'platinum':
            total_value_gold += platinum2gold(item['price']['amount'] * item['amount'])
    return round(total_value_gold, 2)

##################### O09 #####################

#Bereken het totale goud van de groep op basis van de individuele geldhoeveelheden van elke persoon
def getCashInGoldFromPeople(people:list) -> float:
    total_gold = 0.0
    for person in people:
        cash = person.get('cash', {}) #Haal het geld van de persoon op, als het niet bestaat, neem een lege dictionary
        total_gold += getPersonCashInGold(cash)
    return round(total_gold, 2)

##################### O10 #####################

#Selecteer interessante investeerders die minder dan 10% van de opbrengst vragen
def getInterestingInvestors(investors:list) -> list:
    interesting_investors = []
    for investor in investors:
        if investor['profitReturn'] < 10:
            interesting_investors.append(investor)
    return interesting_investors

#Selecteert investeerders die geïnteresseerd zijn in avonturieren (adventuring=True)
def getAdventuringInvestors(investors:list) -> list:
    interesting_investors = getInterestingInvestors(investors)
    adventuring_investors = getAdventuringPeople(interesting_investors)
    return adventuring_investors

#Berekent de totale kosten voor investeerders die mee gaan op avontuur
def getTotalInvestorsCosts(investors:list, gear:list) -> float:
    total_costs = 0.0

    adventuring_investors = getAdventuringInvestors(investors)

    for investor in adventuring_investors:
        investor_gear_cost = getItemsValueInGold(gear)
        total_costs += investor_gear_cost

        horses_costs = JOURNEY_IN_DAYS * silver2gold(COST_HORSE_SILVER_PER_DAY)
        tents_costs = math.ceil(JOURNEY_IN_DAYS / 7) * COST_TENT_GOLD_PER_WEEK
        tents_horses_costs = horses_costs + tents_costs
        total_costs += tents_horses_costs

        food_cost = getJourneyFoodCostsInGold(1, 1)
        total_costs += food_cost

    return round(total_costs, 2)

##################### O11 #####################

#Deze functie rekent uit hoevel nachten er maximaal in een herberg overnacht kan worden
def getMaxAmountOfNightsInInn(leftoverGold:float, people:int, horses:int) -> int:
    pass

#Deze functie rekent uit hoeveel alle nachten samen die in een herberg gespendeerd worden kosten
def getJourneyInnCostsInGold(nightsInInn:int, people:int, horses:int) -> float:
    pass

##################### O13 #####################

def getInvestorsCuts(profitGold:float, investors:list) -> list:
    pass

def getAdventurerCut(profitGold:float, investorsCuts:list, fellowship:int) -> float:
    pass

##################### O14 #####################

def getEarnigs(profitGold:float, mainCharacter:dict, friends:list, investors:list) -> list:
    pass

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