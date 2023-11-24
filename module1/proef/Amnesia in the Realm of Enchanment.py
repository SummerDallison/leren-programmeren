print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print(">          Amnesia in the Realm of Enchantment          >")
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

inventaris = []
companions = []
profiel_inhoud = []

gouden_munten = 0
zilveren_munten = 0
bronzen_munten = 0

print("Ik word langzaam wakker en knijp mijn ogen samen in een poging om te wennen aan het verblindende zonlicht dat mijn zicht overweldigt.")
print("Ik kijk verward om me heen en besef dat ik op een onbekende locatie bevind.")
print("Ik merk dat ik omringd ben door een prachtige, groene omgeving met hoge bomen. Ik hoor het zachte geritsel van bladeren dat wordt veroorzaakt door de wind.")
print("Nadenkend over mijn omgeving, vroeg ik me in verwarring af, 'Waar ben ik? Wat voor plek is dit?' Het voelde vreemd en onbekend.")
print("Terwijl ik bewust ben dat dit niet mijn vertrouwde thuis, kon ik me ook niet herinneren waar ik wel vandaan kwam.")
print("Ik probeer mijn naam te herinneren, maar er verschijnt niets in mijn gedachten.")
print("Terwijl ik worstel om mijn vage herinneringen op te frissen, komt er uiteindelijk een naam naar boven.")

def vraag_naam():
    while True:
        naam = input("Voer uw naam in: ")
        while not naam.isalpha():
            print("Ongeldige invoer. Voer alleen letters in uw naam.")
            naam = input("Voer uw naam in: ")

        bevestiging_naam = input(f"Uw naam is {naam}, klopt dit? (ja/nee): ").lower()
        while bevestiging_naam not in ["ja", "nee"]:
            print("Antwoord alstublieft met 'ja' of 'nee'.")
            bevestiging_naam = input(f"Uw naam is {naam}, klopt dit? (ja/nee): ").lower()

        if bevestiging_naam == "ja":
            return naam

naam = vraag_naam()

print(f"'{naam},' mompel ik, alsof ik het voor het eerst hoor, maar het klinkt ook zo vertrouwd. ")

print("[Nieuwe informatie is toegevoegd aan uw profiel!]")

nieuwe_informatie = (f"[Naam: {naam}]")

while True:
    profiel = input("Open profiel? (ja/nee) ")
    if profiel.lower() == "ja":
        profiel_inhoud.append(f"{nieuwe_informatie}")
        break
    elif profiel.lower() == "nee":
        print("[Je hebt ervoor gekozen je profiel niet te openen. Het verhaal gaat verder.]")
        break
    else:
        print("Antwoord alstublieft met 'ja' of 'nee'.")

for extra_info in profiel_inhoud:
    print(extra_info)

print("Ik neem het besluit om verder te lopen, vastbesloten om de mysteries van deze onbekende plek te ontrafelen.")
print("Ik ontdek een oude bibliotheek tussen de bomen. De deuren kraken en overal liggen stoffige boeken.")

while True:
    keuze_bibliotheek = input("Moet ik de tijd nemen om de boeken te bekijken, of snel doorgaan met mijn reis?\n(tijd/doorgaan): ")

    if keuze_bibliotheek.lower() == "tijd":

        print("[Je besloot om de tijd te nemen om de boeken te bekijken.]")
        print("Ik werp een blik op de boekenplanken en besluit enkele boeken op te pikken om te verkennen.")
        
        print("Terwijl ik tussen de verweerde boekenplanken speur, stuit ik op verborgen compartimenten met twee magische artefacten.")
        print("De eerste artefact is een zwart kristal met mysterieuze inscripties.")
        print("De tweede artefact is een gouden amulet met een glinsterende edelsteen.")

        while True:
            pick_artefacts = input("Wil je de magische artefacten oppakken? (ja/nee): ")

            if pick_artefacts.lower() == "ja":
                while True:
                    beide_artefacten = input("Wil je beide artefacten oppakken? (ja/nee): ")

                    if beide_artefacten.lower() == "ja":
                        print("[Zwart kristal toegevoegd aan inventaris!]")
                        inventaris.append("Zwart kristal")
                        print("[Gouden amulet toegevoegd aan inventaris!]")
                        inventaris.append("Gouden amulet")

                    elif beide_artefacten.lower() == "nee":
                        while True:
                            welk_artefact = input("Welke artefact wil je oppakken? (zwart/goud): ")
                            
                            if welk_artefact.lower() == "zwart":
                                print("[Zwart kristal toegevoegd aan inventaris!]")
                                inventaris.append("Zwart kristal")

                            elif welk_artefact.lower() == "goud":
                                print("[Gouden amulet toegevoegd aan inventaris!]")
                                inventaris.append("Gouden amulet")

                                print("Terwijl de gouden amulet plotseling begon te stralen, werd ik omhuld door het felle licht, waardoor ik niets meer kon zien.")
                                print("Toen het licht eindelijk verdween, bevond ik me niet langer in de bibliotheek.")
                                print("Ik bevond me op een drijvend eiland in de lucht, met zwevende stenen paden die allemaal leken te leiden naar verschillende delen van het eiland.")

                                while True:
                                    zwevende_pad = input("Welke pad wil je nemen? (links/midden/rechts): ")

                                    if zwevende_pad.lower() == "links":
                                        print("Ik besloot het pad aan mijn linkerkant te volgen.")
                                        print("Naarmate ik verder liep, begon het pad steeds smaller te worden.")
                                        print("Plotseling kwam ik bij een punt waar het pad abrupt eindigde, en de afgrond onder me was angstaanjagend diep. ")
                                        print("Mijn aarzeling kostte me mijn evenwicht, en ik viel in de leegte.")
                                        print("[Gestorven door acrobatische mislukking!")

                                    elif zwevende_pad.lower() == "rechts":
                                        print("Ik besloot het pad aan mijn rechterkant te volgen.")

                                        print("Na het volgen van het pad kom ik uiteindelijk uit op een schijnbaar oneindige uitgestrektheid van wolken.")
                                        print("De lucht is om me heen, en ik voel me licht als een veertje terwijl ik over de wolken loop.")
                                        print("Het uitzicht is adembenemend, met een oneindige horizon van lucht en wolken.")
                                        print("Plotseling merk ik dat de wolken onder me beginnen te vervagen.")
                                        print("Ik probeert mijn grip te houden, maar voor ik het weet, val ik door de zachte massa heen.")
                                        
                                        print("Terwijl ik door de wolken val en de grond onder me steeds dichterbij komt, verwacht ik de onvermijdelijke klap.")
                                        print("Maar op het laatste moment word ik ruw vastgegrepen.")
                                        print("Het is niet de zachte omhelzing van de lucht, maar de ijzige greep van scherpe klauwen.")
                                        print("Ik kijk omhoog en realiseer me dat ik gevangen ben in de klauwen van een gigantische adelaar, haar vlijmscherpe blik boort in de mijne.")

                                        print("De adelaar draagt me omhoog, ver boven de wolken, en ik voel de koude wind langs mijn gezicht suizen.")
                                        print("Angst verstikt me als ik bedenk wat er gaat gebeuren.")
                                        print("Plotseling landen we op een rotsachtige uitstulping hoog in de bergen.")
                                        print("De adelaar, met haar veren glanzend in het zonlicht, kijkt me dreigend aan.")
                                        print("Haar nest, vol hongerige jongen, is slechts een paar meter verderop.")

                                        print("Ik voel de trillende vleugels van de adelaar onder me als ze haar klauwen strakker aanspant.")
                                        print("Een rilling kruipt langs mijn ruggengraat terwijl ik besef dat ik niet langer een passagier ben, maar een potentieel hapje voor haar hongerige kroost.")
                                        print("De angstige realisatie van mijn benarde situatie vult mijn gedachten, en ik kan alleen maar hopen op een wonder om aan deze angstaanjagende ontmoeting te ontsnappen.")

                                        print("De adelaar fixeert me met haar indringende blik terwijl ik hulpeloos in haar klauwen hang.")
                                        print("Haar nest met hongerige jongen wacht geduldig op voedsel, en ik ben op dit moment niets meer dan een prooi in haar greep.")
                                        print("Terwijl ik mijn adem inhoud, voel ik de adelaar haar klauwen strakker aanspannen.")
                                        print("Haar ogen lijken me te doorboren, en ik realiseer me dat mijn lot op het spel staat.")
                                        print("In een flits bedenk ik me dat ik misschien een manier kan vinden om haar gunst te winnen en mijn leven te redden.")

                                        print("Ik staar naar de scherpe klauwen die me vasthouden en overweeg mijn opties:")
                                        while True:
                                            print(" - Probeer de adelaar gerust te stellen door rustig te blijven en haar niet aan te staren.")
                                            print(" - Schreeuw om hulp in de hoop dat er iemand in de buurt is.")
                                            print(" - Trek aan de veren van de adelaar om jezelf te verdedigen.")

                                            keuze_adelaar = input("Wat is mijn beslissing? (geruststellen/schreeuwen/veren): ")

                                            if "geruststellen" in keuze_adelaar.lower():
                                                print("Ik besluit ervoor om de adelaar gerust te stellen.")
                                                print("Langzaam adem ik in, probeer ik mijn hartslag te vertragen en vermijd ik oogcontact.")

                                            elif "schreeuwen" in keuze_adelaar.lower():
                                                print("Ik besluit om om hulp te schreeuwen, in de hoop dat iemand mijn noodkreet zal horen en hulp zal bieden.")
                                                print("Mijn schreeuw om hulp lijkt onbedoelde gevolgen te hebben.")

                                                print("De adelaar, in een mengeling van beschermende instincten en honger van haar jongen, grijpt me vast met haar scherpe klauwen en vliegt met grote vleugelslagen naar haar nest.")                                               
                                                print("Eenmaal aangekomen bij het nest, voel ik de nieuwsgierige blikken van de hongerige jongen die me omringen.")
                                                print("De adelaar, vastberaden om haar kroost te voeden, plaatst me midden in het nest.")

                                                print("De jongen stoten elkaar aan de kant om bij hun onverwachte maaltijd te komen.")
                                                print("Hun snavels en klauwen trekken mijn aandacht, en het besef dat ik geen ontsnappingsroute heb, dringt door.")
                                                print("Terwijl ik machteloos toekijk, beginnen de jongen gulzig aan me te pikken en te scheuren.")
                                                print("Mijn schreeuw om hulp heeft me in de hoogste regionen van de voedselketen geplaatst, maar niet op de manier die ik had gehoopt.")
                                                
                                                print("Het wordt snel donker voor mijn ogen terwijl ik dien als offer voor de hongerige jongen van de adelaar.")
                                                print("Mijn noodkreet heeft mijn lot bezegeld, en ik verdwijn in de maag van de bergbewoners hoog boven de wolken.")
                                                print("[Gestorven door een plotselinge carrièreswitch naar adelaarvoer!]")

                                            elif "veren" in keuze_adelaar.lower():
                                                print("Mijn handen trillen terwijl ik in paniek aan de veren van de adelaar trek, een impulsieve reactie op de dreigende situatie waarin ik me bevind.")
                                                print("De veren geven mee onder mijn greep, en ik voel de zachte textuur ervan in mijn handen.")

                                                print("Echter, mijn poging tot zelfverdediging lijkt weinig effect te hebben.")
                                                print("De adelaar reageert op mijn actie met een scherpe kreet, haar grote ogen bliksemen van verontwaardiging.")
                                                print("In plaats van dat ze schrikt, lijkt mijn handeling haar eerder boos te maken.")

                                                print("Met een snelle beweging draait de adelaar zich naar me toe, haar klauwen uitgestrekt.")
                                                print("Ik besef dat ik mijn situatie alleen maar erger heb gemaakt.")
                                                print("De adelaar slaat me met haar vleugel, waardoor ik uit balans raak en tegen de rotsachtige ondergrond stort.")
                                                print("De harde klap veroorzaakt pijn in mijn lichaam, en alles wordt zwart om me heen.")
                                                print("[Gestorven door een overdosis veren!]")

                                            else:
                                                print("Mijn gedachten raken verward door de dreigende situatie. Ik moet een beslissing nemen.")
                                                continue
                                            break

                                    elif zwevende_pad.lower() == "midden":
                                        print("Ik besloot het pad in het midden te volgen.")

                                    else:
                                        print("Antwoord alstublieft met 'links', 'midden' of 'rechts'.")
                                        continue
                                    break
                            
                            else:
                                print("Antwoord alstublieft met 'zwart' of 'goud'.")
                                continue
                            break

                    else:
                        print("Antwoord alstublieft met 'ja' of 'nee'.")
                        continue
                    break

            elif pick_artefacts.lower() == "nee":
                print("[Je besluit om de magische artefacten met rust te laten.]")

            else:
                print("Antwoord alstublieft met 'ja' of 'nee'.")
                continue
            break          

    elif keuze_bibliotheek.lower() == "doorgaan":
        print("[Je besloot om snel door te gaan met jouw reis.]")
        print("Mijn stappen leiden me weg van de bibliotheek, op zoek naar onontdekte geheimen in dit magische wereld.")

        print("Nadat ik een tijdje door het bos heb gelopen, ontdek ik een schattig dorpje tussen de bomen.")
        print("Kleine huisjes met mooie decoraties trekken mijn aandacht, en het geluid van hamers en smeedwerk komt naar voren.")
        print("En zonder enige aarzeling besluit ik mijn weg naar het dorpje te vervolgen.")
        print("Terwijl ik verder door het dorp loop, begin ik steeds meer op te merken.")
        print("De ambachtelijke winkeltjes zitten propvol met prachtig smeedwerk, en de geur van gesmolten metaal zweeft in de lucht.")
        print("Terwijl ik om me heen kijk, zie ik mensen van een wat kleinere gestalte, stevig gebouwd en duidelijk bedreven in hun ambacht.")
        print("Langzaam dringt het tot me door: dit is geen gewoon dorp; ik ben te midden van dwergen.") 
        print("Een golf van zowel verrassing als nieuwsgierigheid spoelt over me heen.")

        print("Ik besluit een van de ambachtelijke winkeltjes binnen te stappen.") 
        print("Het is gevuld met prachtige smeedkunst en unieke voorwerpen.")
        print("Als ik binnenstap, verwelkomt me de geur van gesmolten metaal en het geluid van zachte hamerslagen.")
        print("Ik kijk rond en zie blinkende amuletten, interessante edelstenen en goed gemaakte wapens op de planken.")

        print("Terwijl mijn blik zich laat afdwalen door de variatie aan voorwerpen, wordt mijn aandacht getrokken naar een dwerg gehuld in een leren schort.")
        print("De smid lijkt diep verzonken in zijn werk bij de smidse.")
        print("Nieuwsgierig blijf ik staan, terwijl de dwerg bedreven bezig is bij de smidse.")
        print("'Met een vriendelijke groet kijkt hij op en begroet me. 'Welkom, reiziger! Ik ben Thorin, de smid van dit dorp.'")
        print("Hij neemt een moment van aarzeling voordat hij vervolgt,")
        print("'Ik heb een speciale smeedopdracht voor je. Voor het maken van een uniek wapen heb ik een bepaalde hoeveelheid zeldzame stenen nodig, die je kunt vinden in een grot hier in de buurt.")
        print("Als je bereid bent deze uitdaging aan te nemen, zal ik je voorzien van de benodige gereedschappen.' Thorin kijkt me verwachtingsvol aan, in afwachting van mijn antwoord.")

        while True:
            print("[Thorin, de bekwame smid van het dorp, heeft een uitdaging voor je!]")
            quest_stenen = input("Ben je bereid om de uitdaging van de 'Stenen van Schittering' aan te nemen? (ja/nee): ")

            if quest_stenen.lower() == "ja":
                print("[Je hebt de uitdaging 'Stenen van Schittering' aangenomen!]")

                print("Na mijn instemming glijdt er een veelbetekenende glimlach over het gezicht van Thorin. Hij haalt een oude kaart van de grot en een stevige houweel tevoorschijn en overhandigt ze aan mij.")
                print("[Versleten map van Donkere Diepten toegevoegd aan inventaris!]")
                inventaris.append("Versleten map van Donkere Diepten")
                print("[Houweel toegevoegd aan inventaris!]")
                inventaris.append("Houweel")

                print("Jouw taak is om die stenen te verzamelen.")
                print("Hoeveel je precies nodig hebt, vertel ik je niet.")
                print("Breng gewoon alles wat je kunt vinden terug.")
                print("Als je precies genoeg hebt, smeed ik dat speciale wapen voor je.")
                print("En als je meer hebt dan nodig, mag je het overschot verkopen voor extra winst.'")
                print("Thorin wijst vervolgens op de kaart en licht toe waar de Donkere Diepten, de grot die je zoekt, zich bevindt.")
                print("Nadat ik beleefd afscheid had genomen van Thorin, zette ik koers naar de plaats waar de grot zich bevond.")

                print("Na een wandeling van ongeveer een half uur, bereik ik de ingang van de grot.")
                print("Voorzichtig zette ik mijn eerste stappen naar binnen, waar het duister mijn omgeving in een mysterieuze gloed hulde. ")
                print("De wanden glinsterden door de weerkaatsing van onbekende mineralen, en de echo van druppelend water vulde de lucht.")
                print("De grot onthulde een doolhof van tunnels.")

                print("De grot vertakt zich nu in vijf verschillende tunnels. Welke tunnel zou het beste zijn om te kiezen?")

                while True:
                    vijf_tunnels = input("Welke van deze tunnels lijkt de meest veelbelovende route te zijn? (eerste/tweede/derde/vierde/vijfde): ")
                    
                    if vijf_tunnels.lower() == "tweede" or vijf_tunnels.lower() == "vijfde":
                        print(f"[Je hebt voor de {vijf_tunnels} tunnel gekozen!]")

                    elif vijf_tunnels.lower() == "eerste" or vijf_tunnels.lower() == "derde":
                        print(f"[Je hebt voor de {vijf_tunnels} tunnel gekozen!]")

                    elif vijf_tunnels.lower() == "vierde":
                        print(f"[Je hebt voor de {vijf_tunnels} tunnel gekozen!]")

                        while True:
                            twee_tunnels = input("Welke van de twee tunnels lijkt de meest veelbelovende route te zijn? (eerste/tweede): ")

                            if twee_tunnels.lower() == "eerste":
                                print(f"[Je hebt voor de {twee_tunnels} tunnel gekozen!]")

                                print("Terwijl ik verder door de tunnel van de grot loop, ontdek ik glinsterende mineralen aan de wanden en hoor ik het geluid van druppelend water.")
                                print("Plotseling kom ik uit in een grote ondergrondse ruimte, verlicht door fosforescerende kristallen die aan het plafond hangen.")
                                print("In het midden van de ruimte staat een mysterieus altaar, omringd door symbolen die ik niet kan ontcijferen.")

                                print("Ik bevind me nu voor het altaar, waar een oude steen met mysterieuze inscripties mijn aandacht trekt.")
                                print("De inscripties lijken haast tot me te fluisteren.")
                                print("Zonder bewuste gedachten laat ik mezelf naar de steen leiden, mijn focus volledig op het artefact gericht.")
                                print("Het is alsof de wereld om me heen vervaagt en ik me in een betoverende trance bevind, ")
                                print("geleid door een onzichtbare kracht die me naar de oude steen leidt.")
                                print("Mijn hand reikt uit, bijna automatisch, en ik voel de koele aanraking van de steen.")
                                print("Op het moment van contact lijkt een golf van energie door me heen te stromen.")
                                print("De inscripties op de steen beginnen te gloeien, en de wereld om me heen vervaagt.")

                                print("------------BEGIN HERINNERING------------")

                                print("Plotseling bevind ik me te midden van een nachtmerrieachtige scène.")
                                print("Het geluid van huilende wind, brandende vlammen en het geschreeuw van mensen vullen de lucht.")
                                print("'Waar ben ik?' vraag ik me af terwijl ik angstig om me heen kijk.")
                                print("Alles is verwoest, en ik zie dat mijn lichaam bedekt is met bloed van mijn eigen verwondingen.")

                                print("Verbijsterd staar ik naar mijn gewonde zelf, machteloos overgeleverd aan deze gruwelijke omgeving.")
                                print("Mijn lichaam begint uit zichzelf op te staan, alsof het wordt voortgestuwd door een onzichtbare kracht.")
                                print("Het lijkt wel alsof ik op zoek ben naar iemand in deze chaos, zonder controle over mijn eigen bewegingen.")
                                print("Ik ren door de verwoeste omgeving, probeer de gruwelijkheden te negeren en mijn weg te vinden te midden van de ruïnes.")

                                print("Terwijl ik probeer te begrijpen wat er gaande is, hoor ik plotseling mijn naam die wordt geroepen.")
                                print("Verward en geschrokken, probeer ik de stem te plaatsen.")
                                print("Langzaam verschijnt er een bekende gestalte te midden van de verwoesting.")
                                print("De details vervagen, maar ik herken de persoon ergens van, hoewel ik er nog niet achter kan komen wie het eigenlijk is.")
                                print("Het enige wat ik kan onderscheiden, is dat het om een vrouw gaat.")

                                print("'Ga snel! Je moet hier weg!' roept de vrouw met urgentie in haar stem.")
                                print("Plotseling strekt ze haar hand uit, en een glinsterend portaal ontstaat voor me.")
                                print("'Het is de enige manier om je te beschermen,' voegt ze eraan toe, haastig en bezorgd.")

                                print("Dan voel ik dat het portaal mij erin wil trekken.")
                                print("Voordat ik volledig in het portaal verdwijn, werp ik nog een laatste blik op de vrouw.")
                                print("Tranen vullen mijn ogen terwijl ik me afvraag waarom deze herinnering zo pijnlijk is.")
                                print("En dan wordt alles weer zwart voor mijn ogen.")

                                print("------------EINDE HERINNERING------------")

                            elif twee_tunnels.lower() == "tweede":
                                print(f"[Je hebt voor de {twee_tunnels} tunnel gekozen!]")

                                print("Ik vervolg mijn weg door de grot en kom plotseling terecht in een ruimte, gevuld met een overvloed aan goud, edelstenen en andere kostbare schatten.")
                                print("Echter, mijn aandacht wordt abrupt getrokken door een gigantische draak die op de schatten waakt.")
                                print("Een diepe grom ontsnapt uit zijn keel als teken dat mijn aanwezigheid niet onopgemerkt blijft.")
                                print("'Wat moet ik nu doen?' vraag ik me in paniek af. Ik zit te twijfelen of ik moet rennen of vechten. ")
                                print("In beide scenario's bevind ik me in een nadelige positie.")

                                while True:
                                    draak_keuze = input("Welke actie ben je van plan om te doen? (rennen/vechten)")
                                    if draak_keuze.lower() == "rennen":
                                        print("Ik besluit om zo snel mogelijk weg te rennen, mijn hart bonkt in mijn keel terwijl ik de grot probeer te ontvluchten.")
                                        print("Ondanks mijn inspanningen voel ik de hete adem van de draak in mijn nek, en voordat ik het besef, word ik ondergedompeld in een zee van goud.")
                                        print("Het glanzende metaal bedekt me volledig en verstikt me, waardoor ik een verstikkende dood tegemoet ga.")
                                        print("[Gestorven door de gouden omhelzing van de draak!]")

                                    elif draak_keuze.lower() == "vechten":
                                        print("Ik zoek naar een wapen in de omgeving en sta klaar om me te verdedigen tegen de draak.")
                                        print("De draak overweldigt me met zijn krachtige aanvallen en voor ik het weet, word ik verzwolgen door zijn vlammen.")
                                        print("[Gestorven door warm welkom!]")

                                    else:
                                        print("Antwoord alstublieft met 'rennen' of 'vechten'.")
                                        continue
                                    break

                            else:
                                print("Antwoord alstublieft met '1' of '2'.")
                                continue
                            break

                    else:
                        print("Antwoord alstublieft met '1', '2','3', '4' of '5'.")
                        continue  
                    break
    
            elif quest_stenen.lower() == "nee":
                print("[Je hebt de uitdaging 'Stenen van Schittering' niet aangenomen!]")

                print("Na de weigering van de uitdaging 'Stenen van Schittering' besloot ik mijn verkenningstocht door het dwergendorp voort te zetten.")
                print("Terwijl ik door de kronkelende steegjes dwaalde, ontdekte ik een levendige handelsmarkt die het centrum van het dwergendorp verlichtte.")
                print("Kleurrijke kramen stonden vol met exotische waren, van fonkelende edelstenen tot zorgvuldig vervaardigde wapens en handgemaakte voorwerpen.")
                print("Mijn nieuwsgierigheid groeide en ik besloot de markt verder te verkennen.")

                print("Terwijl ik tussen de kraampjes liep, werd ik aangesproken door een dwerg genaamd Gimli, een ervaren handelaar uit het dorp.")
                print("Hij was druk bezig met de voorbereidingen voor een handelsmissie naar het elfenkoninkrijk Eldoria.")
                print("Ze waren op zoek naar mensen met diverse vaardigheden om waardevolle goederen vanuit het dwergendorp naar Eldoria te transporteren.")

                print("'Heb je ooit gedacht aan het deelnemen aan een handelsmissie naar het elfenkoninkrijk?' vroeg Gimli.")
                print("'We hebben een groep avonturiers verzameld om waardevolle goederen zoals onze prachtige ambachtelijke producten, edelstenen en speciale wapens naar Eldoria te brengen.")
                print("Ze hebben een grote vraag naar onze ambachten en smeedwerk daar.'")

                print("Nieuwsgierig naar het aanbod vroeg ik Gimli wat de handelsmissie precies inhield.")
                print("Hij legde uit dat we ambachtelijke producten, edelstenen en speciale wapens van het dwergendorp naar Eldoria zouden brengen.")
                print("Onze taak was om deze goederen te presenteren aan de inwoners van Eldoria en te handelen voor waardevolle elfenproducten.")
                print("Als beloning voor onze inspanningen zouden we worden betaald in verschillende valuta, waaronder gouden, zilveren en bronzen munten.")
                print("Bovendien zouden we de kans krijgen om enkele van de unieke elfenproducten voor onszelf te verkrijgen.")

                while True:
                    handels_missie = input("Wil je de handelsmissie aannemen? (ja/nee): ")

                    if handels_missie.lower() == "ja":
                        print("[Je hebt de handelsmissie aangenomen!]")
                        
                        print("Met de handelsmissie geaccepteerd, maak ik mijn weg naar de sfeervolle stallen, waar tot mijn verrassing een prachtig, zwarte rijpaard op me stond te wachten.")
                        print("Zijn glanzende zwarte vacht straalt kracht uit, en zijn gespierde lichaamsbouw belooft zowel snelheid als uithoudingsvermogen.")
                        print("Een witte bles siert zijn hoofd, terwijl zijn ogen nieuwsgierig oplichten bij mijn nadering.")

                        def vraag_paard():
                            while True:
                                paard_naam = input("Welke naam wil je aan jouw paard geven? ")
                                while not paard_naam.isalpha():
                                    print("Ongeldige invoer. Voer alleen letters in de naam van uw paard.")
                                    paard_naam = input("Welke naam wil je aan jouw paard geven? ")

                                bevestiging_paard = input(f"Weet je zeker dat je jouw paard {paard_naam} wilt noemen? (ja/nee): ").lower()
                                while bevestiging_paard not in ["ja", "nee"]:
                                    print("Antwoord alstublieft met 'ja' of 'nee'.")
                                    bevestiging_paard = input(f"Weet je zeker dat je jouw paard {paard_naam} wilt noemen? (ja/nee): ").lower()

                                if bevestiging_paard == "ja":
                                    return paard_naam
                                
                        paard = vraag_paard()

                    elif handels_missie.lower() == "nee":
                        print("[Je hebt de handelsmissie niet aangenomen!]")

                    else:
                        print("Antwoord alstublieft met 'ja' of 'nee'.")
                        continue
                    break

            else:
                print("Antwoord astublieft met 'ja' of 'nee'.")
                continue
            break       

    else:
        print("Antwoord alstublieft met 'tijd' of 'doorgaan'.")
        continue
    break