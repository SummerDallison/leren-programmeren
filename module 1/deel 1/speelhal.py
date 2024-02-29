personen = 4

toegangsticket_prijs = 7.45

tijd_in_VR_per_person = 45
kosten_per_minuut_per_persoon = 37

totaal_bedrag_toegangsticket = toegangsticket_prijs * personen

totaal_bedrag_VR = (tijd_in_VR_per_person/5) * kosten_per_minuut_per_persoon * personen/100

totaal_bedrag = totaal_bedrag_VR + totaal_bedrag_toegangsticket

print(f"Je moet in totaal {totaal_bedrag:.2f} euro betalen.")

print(f"Dit geweldige dagje-uit met {personen} mensen in de Speelhal met {tijd_in_VR_per_person} minuten VR kost je maar {totaal_bedrag:.2f} euro")