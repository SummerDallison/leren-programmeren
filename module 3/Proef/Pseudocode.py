# Toon bericht: "Welkom bij Papi Gelato, je mag alle smaken kiezen zolang het maar vanille ijs is."

# Herhaal
    # Toon vraag: "Hoeveel bolletjes wilt u?"
    # Lees input: aantal_bolletjes

    # Als aantal_bolletjes tussen 1 en 3:
        # Toon vraag: "Wilt u deze {aantal_bolletjes} bolletje(s) in een hoorntje of een bakje?"

        # Herhaal:
            # Lees input: keuze
            # Als keuze is "bakje" of "hoorntje":
                # Toon bericht: "Hier is uw {keuze} met {aantal_bolletjes} bolletje(s)."
                # Ga naar 'Nog meer bestellen'
            # Anders:
                # Toon bericht: "Sorry, dat snap ik niet..."
                # Herhaal vraag keuze

    # Anders als aantal_bolletjes tussen 4 en 8:
        # Toon bericht: "Dan krijgt u van mij een bakje met {aantal_bolletjes} bolletjes."
        # Ga naar 'Nog meer bestellen'

    # Anders als aantal_bolletjes groter dan 8:
        # Toon bericht: "Sorry, zulke grote bakken hebben we niet."
        # Herhaal vraag aantal bolletjes

    # Anders:
        # Toon bericht: "Sorry, dat snap ik niet..."
        # Herhaal vraag aantal bolletjes

# 'Nog meer bestellen?'
# Toon vraag: "Wilt u nog meer bestellen?"

    # Herhaal:
        # Lees input: antwoord
        # Als antwoord is "Ja":
            # Ga terug naar stap 1
        # Als antwoord is "Nee":
            # Toon bericht: "bedankt en tot ziens!"
            # Stop programma
        # Als antwoord is anders:
            # Toon bericht: "Sorry, dat snap ik niet..."
            # Herhaal vraag meer bestellen