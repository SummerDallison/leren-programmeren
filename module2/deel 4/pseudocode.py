#Score begint bij 0

#Er zijn 20 rondes in totaal:
    #Een willekeurige getal (geheimGetal) tussen de 1 en de 1000 wordt gekozen
    #Print de huidige ronde
    
    #10 pogingen om het getal juist te raden:
        #Zolang de ingevoerde waarde geen geldig getal is of buiten het bereik van 1 tot 1000 valt:
            #De speler moet een getal raden tussen de 1 en de 1000 
            #Als het ingevoerde getal kleiner is dan 1 of groter dan 1000:
                #Toon de boodschap: "Voer alstublieft een getal in tussen de 1 en de 1000."
            #Als het ingevoerde getal een ongeldige invoer (geen getal):
                #Toon de boodschap: "Voer alstublieft een geldig getal in tussen de 1 en de 1000."
            #Vraag opnieuw om een getal te raden
            #Als het ingevoerde getal geldig is:
                #Breek de lus

        #Als het ingevoerde getal gelijk is aan het geheime getal:
            #Toon de boodschap: "Gefeliciteerd! Je hebt het juiste getal geraden."
            #Verhoog de score met 1
            #Breek de lus

        #Als het ingevoerde getal kleiner is dan het geheime getal:
            #Toon de boodschap: "Hoger!"
        #Als het ingevoerde getal groter is dan het geheime getal:
            #Toon de boodschap: "lager!"

        #Bereken het verschil tussen het ingevoerde getal en het geheime getal:
        #Als het verschil kleiner is dan 20:
            #Toon de boodschap: "Je bent heel warm!"
        #Als het verschil kleiner is dan 50:
            #Toon de boodschap: "Je bent warm!"

    #Toon het geheime getal
    #Toon de score tot nu toe

    #Als het niet de laatste ronde (ronde 20) is:
        #Zolang de ingevoerde waarde geen geldig antwoord is:
            #Vraag de speler of ze een nieuwe ronde willen starten
            #Als de ingevoerde antwoord geen ja of nee is:
                #Toon de boodschap: "Voer alstublieft 'ja' of 'nee' in."
            #Vraag opnieuw om ja of nee in te voeren
            #Als de ingevoerde antwoord ja of nee is:
                #breek de lus
    
    #Als de speler geen nieuwe ronde wilt spelen:
        #Stop met spelen (breek uit de lus van rondes)

#Toon de eindscore