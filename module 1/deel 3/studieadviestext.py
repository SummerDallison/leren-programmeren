print("*********************** STUDIEADVIES ***********************")
print("Ik ga jou helpen met jouw opleiding. Jij krijgt een aantal stellingen te zien.")
print("Voor elke stelling moet je zeggen hoeveel dat bij jou voorkomt. Je kunt steeds")
print("antwoorden: 0 is 'altijd'; 1 is 'vaak'; 2 is 'regelmatig'; 3 is 'soms'; 4 is 'nooit'.")
print("Het is belangrijk om eerlijk te zijn. Op basis van jouw antwoorden krijg je advies.")

AANTAL_OPTIES = "Kies 0: altijd; 1: vaak; 2: regelmatig; 3: soms; 4: nooit"

aantal_weken_opleiding = int(input('Hoeveel weken ben je al bezig met de opleiding? '))

antwoorden = []

antwoorden.append(int(input('Ik voel stress of blokkades bij het maken van programmeeropdrachten. ')))
antwoorden.append(int(input('Ik stel programmeeropdrachten en -uitdagingen uit. ')))
antwoorden.append(int(input('Ik denk dat ik geen talent heb voor de opleiding. ')))
antwoorden.append(int(input('Ik vermijd assessments (CJV) en feedback van kritische docenten. ')))
antwoorden.append(int(input('Ik vergelijk mezelf met anderen die beter lijken te zijn. ')))

if aantal_weken_opleiding >= 10:
    antwoorden.append(int(input('Ik voel geen interesse in nieuwe programmeertechnieken. ')))
    antwoorden.append(int(input('Ik kopieer code van anderen en lever dat in alsof het helemaal van mij is. ')))

gemiddelde_score = sum(antwoorden)/len(antwoorden)

COMPETENTIE_ADVIES_TITEL = ("*********************** STUDIEADVIES ***********************")

COMPETENTIE_ADVIES_ZORGELIJK = ("Het lijkt erop dat je nog weinig zelfvertrouwen, voldoening en plezier ervaart in het leren programmeren. Er zijn altijd mogelijkheden om je te helpen de draad op te pakken met de opleiding. Praat met jouw SLB-er over extra begeleiding en oefeningen.")

COMPETENTIE_ADVIES_TWIJFELACHTIG = ("Het lijkt erop dat je af en toe weinig zelfvertrouwen, voldoening of plezier ervaart in het leren programmeren. Houd je zelfvertrouwen en motivatie in de gaten!")

COMPETENTIE_ADVIES_GERUSTSTELLEND = ("Het lijkt erop dat je voldoende zelfvertrouwen, voldoening en plezier ervaart in het leren programmeren. Mocht het een keer minder gaan, maak je geen zorgen. Have fun!")

print(COMPETENTIE_ADVIES_TITEL)

if gemiddelde_score <= 2:
    print(COMPETENTIE_ADVIES_ZORGELIJK)
elif gemiddelde_score <= 3:
    print(COMPETENTIE_ADVIES_TWIJFELACHTIG)
else:
    print(COMPETENTIE_ADVIES_GERUSTSTELLEND)