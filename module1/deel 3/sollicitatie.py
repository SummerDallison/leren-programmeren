print("++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("+     Sollicitatieformulier: 'Ruimte-vuilnisman'     +")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("Er wordt u een aantal relevante vragen gesteld...")
print("Gelieve die naar eer en geweten in te vullen.")
print("Als blijkt dat u aan de criteria voldoet dan komt u in")
print("aanmerking voor een serieus sollicitatiegesprek!")
print("Ontspan maar blijf wakker, hier komen de vragen.")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++")

naam = input("Wat is uw naam? ").lower()

lengte = int(input("Wat is uw netto lichaamslengte in hele cm? "))
MAX_LENGTE = 220
MIN_LENGTE = 150

gewicht = int(input("Wat is uw lichaamsgewicht in hele kg? "))
MAX_GEWICHT = 120
MIN_GEWICHT = 90

Certificaat = input("Heeft u de Certificaat 'Overleven Met Gevaarlijk Personeel'? (ja/nee)").lower()

rijbewijs = input("Bent u in bezit van een geldige Vrachtwagen rijbewijs? (ja/nee) ").lower()

hoed = input("Bent u in bezit van een hoge hoed? (ja/nee) ").lower()

dieren_dressuur = int(input("Hoeveel jaar (afgerond) heeft u pratijkservaring met dieren-dressuur? "))
MIN_DRESSUUR = 4

jongleren = int(input("Hoeveel jaar (afgerond) heeft u ervaring met jongleren? "))
MIN_JONGLEREN = 5

acrobatiek = int(input("Hoeveel jaar (afgerond) heeft u pratijkservaring met acrobatiek? "))
MIN_ACROBATIEK = 3

geschikt = (
    MIN_LENGTE <= lengte <= MAX_LENGTE and
    MIN_GEWICHT <= gewicht <= MAX_GEWICHT and
    Certificaat == "ja" or Certificaat == "j" and
    rijbewijs == "ja" or rijbewijs == "j" and
    hoed == "ja" or hoed == "j" and
    (MIN_DRESSUUR <= dieren_dressuur) or (MIN_JONGLEREN <= jongleren) or (MIN_ACROBATIEK <= acrobatiek)
    )

if geschikt:
    print(f"Gefeliciteerd {naam}! U komt in aanmerking voor een sollicitatie gesprek, stuur snel uw cv.")
else:
    print(f"Beste {naam}, u voldoet niet aan onze strenge eisen voor de functie Ruimte-vuilnisman, het spijt ons!")