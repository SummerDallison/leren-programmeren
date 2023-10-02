MAX_LENGTE = 220
MIN_LENGTE = 150
MAX_GEWICHT = 120
MIN_GEWICHT = 90
MIN_DRESSUUR = 4
MIN_JONGLEREN = 5
MIN_ACROBATIEK = 3
MIN_JAREN_ONDERNEMER = 3
MIN_WERKNEMERS = 5
MIN_BREEDTE_SNOR = 10
MIN_LENGTE_HAAR = 20
MIN_BREEDTE_GLIMLACH = 10

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
geslacht = input("Wat is uw geslacht? (man/vrouw/anders) ").lower()

if geslacht == "man":
    breedte_snor = int(input("Wat is de breedte van uw snor? "))
elif geslacht == "vrouw":
    rood_krulhaar = input("Heeft u rood krulhaar? (ja/nee) ").lower()
    if rood_krulhaar == "ja":
        haar_lengte = input("Wat is uw haarlengte? ")
else:
    breedte_glimlach = int(input("Hoe groot is de breedte of uw glimlach? "))

lengte = int(input("Wat is uw netto lichaamslengte in hele cm? "))
gewicht = int(input("Wat is uw lichaamsgewicht in hele kg? "))
mbo = input("Bent u in bezit van een MBO-4 diploma? (ja/nee)").lower()
ondernemer = int(input("Hoeveel jaar bent u al ondernemer? "))
werknemers = int(input("Hoeveel werknemers heeft u in loondienst? "))
Certificaat = input("Heeft u de Certificaat 'Overleven Met Gevaarlijk Personeel'? (ja/nee)").lower()
rijbewijs = input("Bent u in bezit van een geldige Vrachtwagen rijbewijs? (ja/nee) ").lower()
hoed = input("Bent u in bezit van een hoge hoed? (ja/nee) ").lower()
dieren_dressuur = int(input("Hoeveel jaar (afgerond) heeft u pratijkservaring met dieren-dressuur? "))
jongleren = int(input("Hoeveel jaar (afgerond) heeft u ervaring met jongleren? "))
acrobatiek = int(input("Hoeveel jaar (afgerond) heeft u pratijkservaring met acrobatiek? "))

afwijzigingsredenen = []

if not(
    mbo == "ja" or ondernemer >= MIN_JAREN_ONDERNEMER and werknemers >= MIN_WERKNEMERS
):
    afwijzigingsredenen.append("U voldoet niet aan een van de eisen: mbo 4 diploma of het aantal jaar ondernemer zijn of aantal werknemers.")

if not(
    (geslacht == "man" and breedte_snor >= MIN_BREEDTE_SNOR) or   
    (geslacht == "vrouw" and rood_krulhaar == "ja" and haar_lengte >= MIN_LENGTE_HAAR) or   
    geslacht == "anders" and breedte_glimlach >= MIN_BREEDTE_GLIMLACH
):
    afwijzigingsredenen.append("U voldoet niet aan de eisen die gediend zijn voor uw geslacht.")

if not (
    MIN_LENGTE <= lengte <= MAX_LENGTE
):
    afwijzigingsredenen.append("U voldoet niet aan uw aan lengte.")
    
if not(    
    MIN_GEWICHT <= gewicht <= MAX_GEWICHT
):
    afwijzigingsredenen.append("U voldoet niet aan uw gewicht.")
    
if not(    
    Certificaat == "ja"
):
    afwijzigingsredenen.append("U voldoet niet aan een Certificaat 'Overleven met Gevaarlijk personeel'.")

if not(    
    rijbewijs == "ja"
):
    afwijzigingsredenen.append("U voldoet niet aan een geldige vrachtwagen rijbewijs.")

if not(
    hoed == "ja"
):
    afwijzigingsredenen.append("U voldoet niet aan een hoge hoed.")

if not(    
    (MIN_DRESSUUR <= dieren_dressuur) or (MIN_JONGLEREN <= jongleren) or (MIN_ACROBATIEK <= acrobatiek)
):
    afwijzigingsredenen.append("U voldoet niet aan de hoeveelheid jaren voor dieren_dressuur, jongerleren of acrobatiek.")

if not afwijzigingsredenen:
    print(f"Gefeliciteerd {naam}! U komt in aanmerking voor een sollicitatie gesprek, stuur snel uw cv.")
else:
    print(f"Beste {naam}, u bent afgewezen om de volgende reden(en).")
    for reden in afwijzigingsredenen:
        print(reden)