print("***********************STUDIEADVIES***********************")
print("Ik ga jou helpen met jouw opleiding.")
print("Jij krijgt een aantal stellingen te zien.")
print("Voor elke stelling moet je zeggen hoeveel dat bij jou voorkomt.")
print("Je kunt steeds antwoorden:")
print("0 is 'altijd'")
print("1 is 'vaak'")
print("2 is 'regelmatig'") 
print("3 is 'soms'") 
print("4 is 'nooit'.")
print("Het is belangrijk om eerlijk te zijn.")
print("Op basis van jouw antwoorden krijg je advies.")

weken_opleiding = int(input("Hoeveel weken doe je de opleiding al?"))

antwoorden = []

antwoorden.append(int(input("Stelling 1: 'Ik voel stress of blokkades bij het maken van programmeeropdrachten.'")))
antwoorden.append(int(input("Stelling 2: 'Ik vergelijk mezelf met anderen die beter lijken te zijn.'")))
antwoorden.append(int(input("Stelling 3: 'Ik denk dat ik geen talent heb voor de opleiding.'")))
antwoorden.append(int(input("Stelling 4: 'Ik stel programmeeropdrachten en -uitdagingen uit.'")))
antwoorden.append(int(input("Stelling 5: 'Ik vermijd assessments (CJV) en feedback van kritische docenten.'")))

if weken_opleiding >= 10:
    antwoorden.append(int(input("Stelling 6: 'Ik voel geen interesse in nieuwe programmeertechnieken.'")))
    antwoorden.append(int(input("Stelling 7: 'Ik kopieer code van anderen en lever dat in alsof het helemaal van mij is.'")))

gemiddelde_score = sum(antwoorden)/len(antwoorden)

if gemiddelde_score <= 2:
    advies = "Advies is 'zorgelijk'."
elif gemiddelde_score <= 3:
    advies = "Advies is 'Twijfelachtig'."
else:
    advies = "Advies is 'geruststellend'."

print(f"Jouw gemiddelde score is: {gemiddelde_score:.2f}")
print(advies)