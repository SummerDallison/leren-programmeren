# name of student: Summer Dallison
# number of student: 99068199
# purpose of program: Dit programma helpt met het bereken van het wisselgeld in de vorm van munten.
# function of program: Het programma neemt het te betalen bedrag en het betaalde bedrag als input, berekent het wisselgeld en vraagt vervolgens de gebruiker om het aantal munten terug te geven.
# structure of program: Het programma heeft een structuur die om input vraagt en verzamelt, wisselgeld berekent en een loop heeft om de verdeling van munten af te handelen. Vervolgens wordt er een overzicht van de teruggegeven munten afgedrukt en laat ook weten als niet alle wisselgeld is teruggegeven.

toPay = int(float(input('Amount to pay: '))* 100) # Vraagt naar het te betalen bedrag en verandert de invoer naar centen.
paid = int(float(input('Paid amount: ')) * 100) # Vraagt naar het betaalde bedrag en verandert de invoer naar centen.
change = paid - toPay #

if change > 0: # Controleer of het wisselgeld groter is dan 0, wat betekent is dat er wisselgeld wordt gegeven.
  coinValue = 500

  returned_coins = {}
  
  while change > 0 and coinValue > 0: #
    nrCoins = change // coinValue #

    if nrCoins > 0: #
      if coinValue >= 100:
        euroCoins = coinValue // 100
        print('return maximal ', nrCoins, ' coins of ', euroCoins, ' euros!' ) #

        nrCoinsReturned = int(input('How many coins of ' + str(coinValue//100) +  ' euros did you return? ')) 
        change -= nrCoinsReturned * coinValue

        returned_coins[str(euroCoins) + ' euros'] = nrCoinsReturned

      else:
        print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) #

        nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) #
        change -= nrCoinsReturned * coinValue #

        returned_coins[str(coinValue) + ' cents'] = nrCoinsReturned

# comment on code below: 
    if coinValue == 500:
      coinValue = 200
    elif coinValue == 200:
      coinValue = 100
    elif coinValue == 100:
      coinValue = 50
    elif coinValue == 50:
      coinValue = 20
    elif coinValue == 20:
      coinValue = 10
    elif coinValue == 10:
      coinValue = 5
    elif coinValue == 5:
      coinValue = 2
    elif coinValue == 2:
      coinValue = 1
    else:
      coinValue = 0

print("\nOverview of returned coins: ")
for coin, count in returned_coins.items():
  print(f"{count} x {coin}")

if change > 0: #
  print('Sorry, not all required change has been returned with coins.')
  print('Change not returned: ', str(change) + ' cents')
else:
  print('done')