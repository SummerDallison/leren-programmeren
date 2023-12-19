print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print(">          Amnesia in the Realm of Enchantment          >")
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

inventaris = []
companions = []
profiel_inhoud = []

print("Ik word langzaam wakker en knijp mijn ogen samen in een poging om te wennen aan het verblindende zonlicht dat mijn zicht overweldigt.")
print("Ik kijk verward om me heen en besef dat ik op een onbekende locatie bevind.")
print("Ik merk dat ik omringd ben door een prachtige, groene omgeving met hoge bomen.")
print("Ik hoor het zachte geritsel van bladeren dat wordt veroorzaakt door de wind.")
print("Nadenkend over mijn omgeving, vroeg ik me in verwarring af, 'Waar ben ik? Wat voor plek is dit?' \nHet voelde vreemd en onbekend.")
print("Terwijl ik bewust ben dat dit niet mijn vertrouwde thuis, kon ik me ook niet herinneren waar ik wel \nvandaan kwam.")
print("Ik probeer mijn naam te herinneren, maar er verschijnt niets in mijn gedachten.")
print("Terwijl ik worstel om mijn vage herinneringen op te frissen, komt er uiteindelijk een naam naar boven.\n")

def vraag_naam():
    while True:
        naam = input("Voer uw naam in: \n")
        while not naam.isalpha():
            print("Ongeldige invoer. Voer alleen letters in uw naam.\n")
            naam = input("Voer uw naam in: \n")

        bevestiging_naam = input(f"Uw naam is {naam}, klopt dit? (ja/nee): \n").lower()
        while bevestiging_naam not in ["ja", "nee"]:
            print("Antwoord alstublieft met 'ja' of 'nee'.\n")
            bevestiging_naam = input(f"Uw naam is {naam}, klopt dit? (ja/nee): \n").lower()

        if bevestiging_naam == "ja":
            return naam

naam = vraag_naam()

print(f"\n'{naam},' mompel ik, alsof ik het voor het eerst hoor, maar het klinkt ook zo vertrouwd.\n")

print("[Nieuwe informatie is toegevoegd aan uw profiel!]\n")

nieuwe_informatie = (f"[Naam: {naam}]\n")

while True:
    profiel = input("Open profiel? (ja/nee): \n")
    if profiel.lower() == "ja":
        profiel_inhoud.append(f"\n{nieuwe_informatie}")
        break
    elif profiel.lower() == "nee":
        print("\n[Je hebt ervoor gekozen je profiel niet te openen. Het verhaal gaat verder.]\n")
        break
    else:
        print("Antwoord alstublieft met 'ja' of 'nee'.\n")

for extra_info in profiel_inhoud:
    print(extra_info)

print("Ik neem het besluit om verder te lopen, vastbesloten om de mysteries van deze onbekende plek te ontrafelen.")
print("Ik ontdek een oude bibliotheek tussen de bomen. De deuren kraken en overal liggen stoffige boeken.\n")

while True:
    keuze_bibliotheek = input("Moet ik de tijd nemen om de boeken te bekijken, of snel doorgaan met mijn reis? (tijd/doorgaan): \n")

    if keuze_bibliotheek.lower() == "tijd":

        print("[Je besloot om de tijd te nemen om de boeken te bekijken.]")
        print("Ik werp een blik op de boekenplanken en besluit enkele boeken op te pikken om te verkennen.\n")
        
        print("Terwijl ik tussen de verweerde boekenplanken speur, stuit ik op verborgen compartimenten met twee \nmagische artefacten.")
        print("De eerste artefact is een zwart kristal met mysterieuze inscripties.")
        print("De tweede artefact is een gouden amulet met een glinsterende edelsteen.\n")

        while True:
            pick_artefacts = input("Wil je de magische artefacten oppakken? (ja/nee): \n")

            if pick_artefacts.lower() == "ja":
                while True:
                    beide_artefacten = input("\nWil je beide artefacten oppakken? (ja/nee): \n")

                    if beide_artefacten.lower() == "ja":
                        print("[Zwart kristal toegevoegd aan inventaris!]")
                        inventaris.append("Zwart kristal")
                        print("[Gouden amulet toegevoegd aan inventaris!]")
                        inventaris.append("Gouden amulet")
                       
                        print("Echter, op het moment dat je de artefacten aanraakt, voel je een onvoorstelbare kracht die je overweldigt.")
                        print("De magische energie reageert op je aanraking op een oncontroleerbare manier.")
                        print("Een krachtige uitbarsting van magie volgt, en je wordt door de ontembare krachten verteerd.")
                        print("[Gestorven door Overweldigende Magische Energie]")

                    elif beide_artefacten.lower() == "nee":
                        while True:
                            welk_artefact = input("Welke artefact wil je oppakken? (zwart/goud):\n")
                            
                            if welk_artefact.lower() == "zwart":
                                print("\n[Zwart kristal toegevoegd aan inventaris!]\n")
                                inventaris.append("Zwart kristal")

                                print("Het zwarte kristal begint een duistere kracht uit te stralen.")
                                print("Een onheilspellende gloed verspreidt zich langzaam om me heen.")
                                print("De lucht lijkt te verdikken, en een beklemmende duisternis sluit zich om me heen.")
                                print("Ik voel een onzichtbare kracht mijn lichaam omhullen, terwijl de realiteit vervaagt.\n")

                                print("Het lijkt alsof de tijd vertraagt. Ik voelt me zweven, omringd door een eindeloze leegte.")
                                print("Duistere schaduwen dansen voor mijn ogen, en het geluid van zachte fluisteringen vult de stilte.")
                                print("In deze onpeilbare duisternis vervagen grenzen en vervaagt de werkelijkheid.")
                                print("Ik bent niet langer gebonden aan de wereld zoals ik die kende.\n")

                                print("[In de greep van de duisternis!]")
                                break

                            elif welk_artefact.lower() == "goud":
                                print("\n[Gouden amulet toegevoegd aan inventaris!]\n")
                                inventaris.append("Gouden amulet")

                                print("Terwijl de gouden amulet plotseling begon te stralen, werd ik omhuld door het felle licht, waardoor ik niets meer kon zien.")
                                print("Toen het licht eindelijk verdween, bevond ik me niet langer in de bibliotheek.")
                                print("Ik bevond me op een drijvend eiland in de lucht, met zwevende stenen paden die allemaal leken te leiden naar verschillende delen van het eiland.\n")

                                while True:
                                    zwevende_pad = input("Welke pad wil je nemen? (links/midden/rechts): \n")

                                    if zwevende_pad.lower() == "links":
                                        print("\nIk besloot het pad aan mijn linkerkant te volgen.")
                                        print("Naarmate ik verder liep, begon het pad steeds smaller te worden.")
                                        print("Plotseling kwam ik bij een punt waar het pad abrupt eindigde, en de afgrond onder me was angstaanjagend diep.\n")
                                            
                                        print("Mijn aarzeling kostte me mijn evenwicht, en ik verloor de grip op het smalle pad.")
                                        print("In een wanhopige poging om mijn val te stoppen, greep ik naar de rand, maar tevergeefs.")
                                        print("Ik voelde de koude wind langs me suizen terwijl ik in de leegte viel.\n")

                                        print("[Gestorven door acrobatische mislukking!")

                                    elif zwevende_pad.lower() == "rechts":
                                        print("\nIk besloot het pad aan mijn rechterkant te volgen.\n")

                                        print("Na het volgen van het pad kom ik uiteindelijk uit op een schijnbaar oneindige uitgestrektheid van wolken.")
                                        print("De lucht is om me heen, en ik voel me licht als een veertje terwijl ik over de wolken loop.")
                                        print("Het uitzicht is adembenemend, met een oneindige horizon van lucht en wolken.")
                                        print("Plotseling merk ik dat de wolken onder me beginnen te vervagen.")
                                        print("Ik probeert mijn grip te houden, maar voor ik het weet, val ik door de zachte massa heen.\n")
                                        
                                        print("Terwijl ik door de wolken val en de grond onder me steeds dichterbij komt, verwacht ik de onvermijdelijke klap.")
                                        print("Maar op het laatste moment word ik ruw vastgegrepen.")
                                        print("Het is niet de zachte omhelzing van de lucht, maar de ijzige greep van scherpe klauwen.")
                                        print("Ik kijk omhoog en realiseer me dat ik gevangen ben in de klauwen van een gigantische adelaar, haar vlijmscherpe blik boort in de mijne.\n")

                                        print("De adelaar draagt me omhoog, ver boven de wolken, en ik voel de koude wind langs mijn gezicht suizen.")
                                        print("Angst verstikt me als ik bedenk wat er gaat gebeuren.")
                                        print("Plotseling landen we op een rotsachtige uitstulping hoog in de bergen.")
                                        print("De adelaar, met haar veren glanzend in het zonlicht, kijkt me dreigend aan.")
                                        print("Haar nest, vol hongerige jongen, is slechts een paar meter verderop.\n")

                                        print("Ik voel de trillende vleugels van de adelaar onder me als ze haar klauwen strakker aanspant.")
                                        print("Een rilling kruipt langs mijn ruggengraat terwijl ik besef dat ik niet langer een passagier ben, maar een potentieel hapje voor haar hongerige kroost.")
                                        print("De angstige realisatie van mijn benarde situatie vult mijn gedachten, en ik kan alleen maar hopen op een wonder om aan deze angstaanjagende ontmoeting te ontsnappen.\n")

                                        print("De adelaar fixeert me met haar indringende blik terwijl ik hulpeloos in haar klauwen hang.")
                                        print("Haar nest met hongerige jongen wacht geduldig op voedsel, en ik ben op dit moment niets meer dan een prooi in haar greep.")
                                        print("Terwijl ik mijn adem inhoud, voel ik de adelaar haar klauwen strakker aanspannen.")
                                        print("Haar ogen lijken me te doorboren, en ik realiseer me dat mijn lot op het spel staat.")
                                        print("In een flits bedenk ik me dat ik misschien een manier kan vinden om haar gunst te winnen en mijn leven te redden.\n")

                                        print("Ik staar naar de scherpe klauwen die me vasthouden en overweeg mijn opties:")
                                        while True:
                                            print(" - Probeer de adelaar gerust te stellen door rustig te blijven en haar niet aan te staren.")
                                            print(" - Schreeuw om hulp in de hoop dat er iemand in de buurt is.")
                                            print(" - Trek aan de veren van de adelaar om mezelf te verdedigen.\n")

                                            keuze_adelaar = input("Wat is mijn beslissing? (geruststellen/schreeuwen/veren): \n")

                                            if "geruststellen" in keuze_adelaar.lower():
                                                print("\nIk besluit ervoor om de adelaar gerust te stellen.")
                                                print("Langzaam adem ik in, probeer ik mijn hartslag te vertragen en vermijd ik oogcontact.")
                                                print("Ik probeer mijn angst te onderdrukken, hopend dat mijn kalme houding haar zal kalmeren.\n")

                                                print("Na een paar spannende seconden merk ik dat de adelaar haar klauwen ontspant en haar vurige blik afzwakt.")
                                                print("Langzaam laat ze me los, haar grote vleugels gespreid, en ik voel de druk van haar klauwen verminderen.")
                                                print("Haar nieuwsgierige ogen kijken me aan, alsof ze mijn intenties probeert te begrijpen.")
                                                print("Voorzichtig beweeg ik mijn ledematen, bang dat ik opnieuw haar woede zal opwekken.\n")

                                                print("De adelaar, haar vijandigheid nu verdwenen, spreidt haar vleugels en vliegt weg.")
                                                print("Ik blijf achter op de rotsachtige uitstulping, opgelucht dat ik deze confrontatie met de reusachtige adelaar heb doorstaan.\n")

                                                print("Nu de adelaar is vertrokken, overweeg ik mijn volgende stap.")
                                                print("Ik kijk naar de uitgestrekte bergen voor me en bedenk wat de beste route zou kunnen zijn.")
                                                print(" - Ga verder door de bergen, op zoek naar het onbekende.")
                                                print(" - Daal af naar beneden, mogelijk naar bewoonde gebieden.\n")

                                                while True:
                                                    keuze_bergen = input("Wat is mijn beslissing? (bergen/beneden): \n")

                                                    if "bergen" in keuze_bergen.lower():
                                                        print("Met mijn besluit genomen, vervolg ik mijn reis door de ruige bergpaden.")
                                                        print("De paden worden steiler; elke stap vergt meer moeite en vermoeidheid kruipt in mijn benen.")
                                                        print("Twijfel nestelt zich langzaam in mijn gedachten - heb ik wel de juiste route genomen?\n")

                                                        print("Juist op dat moment overstemt het vrolijke lied van fluitende vogels mijn twijfels.")
                                                        print("Ik kijk om me heen en ontdek een kleurrijke papegaai, haar veren schitterend als edelstenen. ")
                                                        print("Haar melodie vult de omgeving met een betoverende symfonie, en de papegaai kijkt me aan met fonkelende ogen, alsof ze me uitnodigt om haar te volgen.")
                                                        print("De vermoeidheid lijkt even vergeten te zijn, vervangen door nieuwsgierigheid.\n")

                                                        print("Aarzelend zet ik de eerste stap in haar richting.")
                                                        print("De papegaai fladdert een paar meter voor me uit en lijkt me te leiden naar een verborgen opening tussen de rotsen.")
                                                        print("Terwijl we naderen, voel ik een zachte bries die door de opening waait, vergezeld van de geur van bloemen.\n")

                                                        print("De opening onthult een prachtige vallei, gehuld in het zachte licht van de ondergaande zon.")
                                                        print("Een kristalheldere rivier slingert zich een weg door het landschap, omringd door kleurrijke bloemen en exotische planten.\n")

                                                        print("Plotseling voel ik een lichte druk op mijn schouder, en als ik opkijk, ontmoet ik de sprankelende ogen van de papegaai.")
                                                        print("Ze lijkt nieuwsgierig naar me te kijken, haar veren glinsterend in het zonlicht.")
                                                        print("Een vreemde, maar aangename band lijkt zich tussen ons te vormen.")
                                                        print("Haar aanwezigheid voelt vertrouwd, alsof ze altijd al bij me is geweest.\n")

                                                        print("Echter, terwijl ik gefascineerd naar de papegaai staar, wordt de lucht plotseling doordrongen door een oorverdovend gekrijs.")
                                                        print("De papegaai verandert van gedaante en onthult scherpe klauwen en een kille, moordlustige blik.")
                                                        print("In een flits valt ze me aan, haar bek scherp als een mes, en ik besef te laat dat dit kleurrijke schepsel slechts een bedrieglijke verschijning was.")
                                                        print("Haar aanval is genadeloos, en ik val levenloos neer in de vallei, mijn avontuur eindigend te midden van de bloemen die eens mijn laatste aanblik waren.\n")

                                                        print("Gestorven door een papegaai met een killer fashion sense!")
                                                        
                                                    elif "beneden" in keuze_bergen.lower():
                                                        print("Met aarzelende treden zet ik de afdaling voort, mijn ogen scherp gericht op de onbekende diepten onder me.")
                                                        print("De paden worden steiler, en de weerstand van de ruige ondergrond voel ik tot in mijn voeten.")
                                                        print("Elke stap lijkt de twijfel in mijn gedachten te vergroten - heb ik werkelijk de juiste keuze gemaakt?\n")

                                                        print("Naarmate ik verder afdaal, omringt een mysterieuze mist me en vervaagt de grens tussen de werkelijkheid en de betovering van deze wereld.")
                                                        print("Het geluid van krakende takken en het ruisen van de wind vullen de lucht.\n")

                                                        print("Uit de mist doemt langzaam een verlaten dorp op.")
                                                        print("De huizen lijken eeuwenoud en overwoekerd met klimplanten.")
                                                        print("Als ik door de verlaten straten dwaal, voel ik een vreemde connectie, alsof ik hier eerder ben geweest.\n")

                                                        print("Plotseling verschijnt er een figuur aan het einde van de straat.")
                                                        print("Mijn hart bonst in mijn borstkas als ik dichterbij kom.")
                                                        print("Tranen stromen over mijn wangen zonder dat ik weet waarom.\n")

                                                        print("Terwijl de mist langzaam optrekt, wordt de verschijning helderder, en een onverwachte stilte vult de lucht.")
                                                        print("Ik hoor mezelf zacht mompelen: 'Mam...?'")
                                                        print("De naam komt als vanzelf uit mijn mond, hoewel ik niet begrijp waarom.\n")

                                                        print("Terwijl mijn blik de hare ontmoet, dringen flarden van herinneringen uit mijn verleden mijn bewustzijn binnen.")
                                                        print("De mist lijkt de grenzen tussen ons te vervagen, net als de werkelijkheid en betovering om ons heen.")
                                                        print("Ik laat de tranen hun weg vinden, een mengeling van verwarring en een onbenoembare band die ons verbindt.\n")

                                                        print("Als ik in haar ogen, krijgen ik flarden van herinneringen in mijn hoofd uit mijn verleden.")
                                                        print("Ondanks dat de herinneringen binnenkomen, blijft het mysterie van hoe ik hier terecht ben gekomen en wat er met dit dorp is gebeurd, onopgelost.")
                                                        print("Een mist begint zich te vormen en blijft toenemen totdat mijn zicht volledig verduisterd is.")
                                                        print("De mist trekt langzaam op, onthullend wat er zich voor mijn ogen afspeelt.\n")

                                                        print("------------BEGIN HERINNERING------------\n")

                                                        print("Plotseling bevind ik me te midden van een nachtmerrieachtige scène.")
                                                        print("Het geluid van huilende wind, brandende vlammen en het geschreeuw van mensen vullen de lucht.")
                                                        print("'Is dit nog dezelfde dorp?' vraag ik me af terwijl ik angstig om me heen kijk.")
                                                        print("Alles is verwoest, en ik zie dat mijn lichaam bedekt is met bloed van mijn eigen verwondingen.\n")

                                                        print("Verbijsterd staar ik naar mijn gewonde zelf, machteloos overgeleverd aan deze gruwelijke omgeving.")
                                                        print("Mijn lichaam begint uit zichzelf op te staan, alsof het wordt voortgestuwd door een onzichtbare kracht.")
                                                        print("Het lijkt wel alsof ik op zoek ben naar iemand in deze chaos, zonder controle over mijn eigen bewegingen.")
                                                        print("Ik ren door de verwoeste omgeving, probeer de gruwelijkheden te negeren en mijn weg te vinden te midden van de ruïnes.\n")

                                                        print("Terwijl ik probeer te begrijpen wat er gaande is, hoor ik plotseling mijn naam die wordt geroepen.")
                                                        print("Verward en geschrokken, probeer ik de stem te plaatsen.")
                                                        print("Langzaam verschijnt er een bekende gestalte te midden van de verwoesting.")
                                                        print("Ondanks de vervaging herken ik haar als mijn moeder.")
                                                        print("De locatie wordt langzaam duidelijk; dit is mijn eigen dorp, de plek waar ik was voordat ik in deze verontrustende herinnering belandde.\n")

                                                        print("'Ga snel! Je moet hier weg!' roept mijn moeder met urgentie in haar stem.")
                                                        print("Plotseling strekt ze haar hand uit, en een glinsterend portaal ontstaat voor me.")
                                                        print("'Het is de enige manier om je te beschermen,' voegt ze eraan toe, haastig en bezorgd.\n")

                                                        print("Dan voel ik dat het portaal mij erin wil trekken.")
                                                        print("Voordat ik volledig in het portaal verdwijn, werp ik nog een laatste blik op mijn moeder.")
                                                        print("Tranen vullen mijn ogen terwijl ik me afvraag waarom deze herinnering zo pijnlijk is.")
                                                        print("En dan wordt alles weer zwart voor mijn ogen.\n")

                                                        print("------------EINDE HERINNERING------------\n")

                                                        print("Terug in mijn verwoeste dorp, sta ik daar, omringd door de ruïnes van wat eens mijn thuis was.")
                                                        print("Mijn moeder staat naast me, haar aanwezigheid voelt vertrouwd, maar de nasleep van de herinnering hangt nog steeds in de lucht. ")
                                                        print("Ik kijk om me heen, mijn ogen gevuld met tranen terwijl ik de vernietiging in me opneem.\n")

                                                        print("'Mam...' fluister ik, mijn stem bijna gebroken.")
                                                        print("De pijn van de herinnering weegt zwaar op mijn hart, maar tegelijkertijd voel ik een diepe connectie met de vrouw die voor me staat.")
                                                        print("Ik omhels haar stevig, alsof ik haar nooit meer los wil laten.\n")

                                                        print("'Je bent terug,' zegt mijn moeder met zachte geruststelling.")
                                                        print("Ze legt haar hand op mijn schouder terwijl ze me probeert te troosten.")
                                                        print("De verwoesting om ons heen lijkt even te vervagen, en ik zoek naar woorden om mijn emoties uit te drukken.\n")

                                                        print("'Ik herinner me... alles,' mompel ik, mijn gedachten nog steeds verstrikt in de recente ervaring.")
                                                        print("'Het was alsof ik vastzat in een nachtmerrie, maar jij... jij was er.'\n")

                                                        print("Mijn moeder knikt begrijpend, alsof ze de last van mijn herinneringen deelt.")
                                                        print("Samen staan we in de verlaten straten, en hoewel het verleden pijnlijk is, voel ik een hernieuwde kracht in onze baand.")
                                                        print("Het besef dat mijn moeder er altijd voor me is geweest, zelfs te midden van chaos en verlies, geeft me een gevoel van troost.")
                                                        print("De zon begint langzaam door de overgebleven wolken te breken, waardoor een zacht licht de verwoesting verlicht.\n")

                                                        print("Plotseling, in de doffe stilte van de verlaten straten, begint de grond te trillen.")
                                                        print("Een onheilspellend gevoel grijpt me bij de keel terwijl donkere schaduwen zich langzaam over de ruïnes verspreiden.")
                                                        print("In het donker verschijnt een gestalte, een figuur gehuld in duisternis en omgeven door een aura van dreiging.")
                                                        print(" Mijn moeder voelt de spanning in de lucht en haar ogen vernauwen zich terwijl ze de gestalte herkent.\n")

                                                        print("'Mam... wie is dat?' vraag ik, mijn blik gefixeerd op de mysterieuze verschijning.\n")

                                                        print("Het gezicht van mijn moeder vertrekt van pijn en herinnering.")
                                                        print("'Het is hem... diegene die ons dorp heeft vernietigd. Zijn naam weerklinkt als een donderslag, beladen met de verantwoordelijkheid voor de verwoesting van alles hier.'")
                                                        print("'Hij staat bekend als Malachai,' fluistert mijn moeder, haar stem doordrenkt met afschuw.")
                                                        print("Zijn naam echoot door de verlaten straten.")
                                                        print("'Een naam die in de schaduwen van ons lijden is gegrift, een naam die we nooit hadden verwacht hier weer te horen.'\n")

                                                        print("De duistere figuur komt langzaam dichterbij, zijn aanwezigheid doordrenkt met duisternis.")
                                                        print("In dit kritieke moment, waar de schaduwen van het verleden zich vermengen met het heden, tekenen zich twee paden af, elk beladen met zijn eigen onzekerheden en consequenties.\n")
                                                        
                                                        print("Mijn moeder kijkt me aan, haar ogen gevuld met een mengeling van vastberadenheid en bezorgdheid.")
                                                        print(f"'{naam}, we hebben twee keuzes,' zegt ze, haar stem gedempt maar vastberaden.")
                                                        print("'We kunnen proberen te ontsnappen, of we confronteren Malachai en eisen gerechtigheid voor wat hij heeft aangericht.'\n")

                                                        while True:
                                                            print("Het lot hangt als een fragiele draad in de lucht, wachtend om geweven te worden door de keuzes die we zullen maken.")
                                                            print("Ik voel een innerlijke tweestrijd, wetende dat de confrontatie onvermijdelijk is.")
                                                            keuze_vijand = input("Twee paden openen zich voor me, elk met zijn eigen risico's. (vluchten/confrontatie): \n")

                                                            if keuze_vijand.lower() == "vluchten":
                                                                print("\nDe angst overweldigt me, en impulsief besluit ik weg te rennen, mijn voeten slaan een onregelmatig ritme op de verwoeste straten.")
                                                                print("Mijn hart bonst in mijn keel, als een snelle drumbeat die de intensiteit van het moment weerspiegelt.")
                                                                print("De schaduwen dansen om me heen terwijl ik wanhopig probeer te ontsnappen aan de duisternis die me genadeloos achtervolgt.")

                                                                print("Elke ademhaling lijkt zwaarder dan de vorige, mijn voeten struikelen over losliggende stenen en verwoeste puin.")
                                                                print("De verwoeste gebouwen getuigen van de chaos die hier heeft plaatsgevonden, en ik vraag me af of er ooit hoop zal zijn in deze duisternis.\n")

                                                                print("Mijn achtervolger, Malachai, lijkt geen genade te kennen.")
                                                                print("Zijn donkere gestalte blijft dreigend op de achtergrond terwijl ik mijn uiterste best doe om uit zijn greep te blijven.")
                                                                print("De angstige gedachten malen in mijn hoofd, maar ik moet doorzetten, ik moet ontsnappen.\n")

                                                                print("Uiteindelijk bereik ik een punt waar de duisternis me opslokt, als een onontkoombare schaduw die me in zijn greep houdt.")
                                                                print("Mijn bewustzijn vervaagt geleidelijk, de grenzen tussen realiteit en droom vervagen terwijl ik in een nevelige mist van onzekerheid verdwijn.")
                                                                print("De wereld om me heen lijkt te vervagen, en ik verlies grip op de werkelijkheid.\n")

                                                                print("Gestorven door een schaduwyoga-sessie gone wrong!")

                                                            if keuze_vijand.lower() == "confrontatie":
                                                                print("De duistere gestalte, Malachai, komt langzaam dichterbij, zijn schreden dreunen als een onheilspellend ritme op de verwoeste straten.")
                                                                print(" Mijn moeder en ik staan klaar, vastberaden om de confrontatie aan te gaan.\n")

                                                                print("'Je kunt niet ontsnappen aan de schaduwen van je verleden,' gromt Malachai, zijn stem doordringt de stilte.")
                                                                print("'Jullie dorp was slechts het begin.'\n")

                                                                print("De lucht lijkt te trillen van spanning terwijl we ons schrap zetten voor de komende strijd.")
                                                                print("Onze vastberadenheid brandt helder, als een laatste vonk van hoop te midden van de verwoesting.\n")

                                                                print("Malachai's duistere aanwezigheid vult de ruimte, en we voelen de druk van de geschiedenis die op onze schouders rust.")
                                                                print("De verlaten straten getuigen van de gevolgen van zijn eerdere verwoestingen, \nen nu staan we op het punt om te ontdekken of gerechtigheid mogelijk is.")
                                                                print("De confrontatie begint, een dans van schaduwen en licht, waarbij de uitkomst onzeker blijft.")
                                                                print("We hebben gekozen om te staan tegenover de duisternis, in de hoop dat ergens in dit verwoeste landschap een sprankje rechtvaardigheid kan ontspruiten.\n")

                                                                print("Malachai ontketent duistere krachten, een wirwar van schaduwen die ons dreigen te verzwelgen.")
                                                                print("Op dat cruciale moment, wanneer de duisternis op het punt staat toe te slaan en ik dreig ten onder te gaan, plaatst mijn moeder zich moedig tussen ons.\n")

                                                                print("'Je zult niet verder komen,' fluistert ze, haar stem doordrenkt van vastberadenheid.")
                                                                print("Haar aanwezigheid straalt een beschermende kracht uit, als een laatste bastion tegen de opkomende duisternis.")
                                                                print("De lucht trilt van spanning, terwijl we standhouden te midden van Malachai's duistere aanval.\n")

                                                                print("Een plotselinge gloed omhult haar, en ik voel een krachtige energie die de lucht doordringt.")
                                                                print("Malachai wordt teruggedrongen door de onzichtbare kracht die van mijn moeder uitgaat.")
                                                                print("In haar laatste daad van opoffering, beschermt ze mij tegen de duistere krachten van Malachai.\n")

                                                                print("Terwijl de energieën botsen, vervagen zowel Malachai als mijn moeder in het licht dat uit hun botsing voortkomt.")
                                                                print("De strijd eindigt abrupt, en de verlaten straten vullen zich weer met een doffe stilte.\n")

                                                                print("Wanneer het licht is verdwenen, sta ik daar alleen, omringd door de ruïnes van wat eens mijn thuis was.")
                                                                print("De confrontatie heeft een einde gemaakt aan de dreiging van Malachai, maar het heeft ook mijn moeder naar het hiernamaals gevoerd.\n")

                                                                print("Met gemengde gevoelens van verdriet en overwinning kijk ik naar de plek waar Malachai stond.")
                                                                print("De verwoesting is voorbij, maar de prijs die we hebben betaald, weegt zwaar op mijn hart.")
                                                                print(" Ik blijf achter in de stille straten, wetende dat gerechtigheid is gediend, maar tegelijkertijd met een diep gevoel van verlies.\n")

                                                                print("[---THE END---]")

                                                            else:
                                                                print("\nAntwoord alstublieft met 'vluchten' of 'confrontatie'.\n")
                                                                continue
                                                            break

                                                    else:
                                                        print("\nAntwoord alstublieft met 'bergen' of 'beneden'.\n")
                                                        continue
                                                    break

                                            elif "schreeuwen" in keuze_adelaar.lower():
                                                print("\nIk besluit om om hulp te schreeuwen, in de hoop dat iemand mijn noodkreet zal horen en hulp zal bieden.")
                                                print("Mijn schreeuw om hulp lijkt onbedoelde gevolgen te hebben.\n")

                                                print("De adelaar, in een mengeling van beschermende instincten en honger van haar jongen, grijpt me vast met haar scherpe klauwen en vliegt met grote vleugelslagen naar haar nest.")                                               
                                                print("Eenmaal aangekomen bij het nest, voel ik de nieuwsgierige blikken van de hongerige jongen die me omringen.")
                                                print("De adelaar, vastberaden om haar kroost te voeden, plaatst me midden in het nest.\n")

                                                print("De jongen stoten elkaar aan de kant om bij hun onverwachte maaltijd te komen.")
                                                print("Hun snavels en klauwen trekken mijn aandacht, en het besef dat ik geen ontsnappingsroute heb, dringt door.")
                                                print("Terwijl ik machteloos toekijk, beginnen de jongen gulzig aan me te pikken en te scheuren.")
                                                print("Mijn schreeuw om hulp heeft me in de hoogste regionen van de voedselketen geplaatst, maar niet op de manier die ik had gehoopt.\n")
                                                
                                                print("Het wordt snel donker voor mijn ogen terwijl ik dien als offer voor de hongerige jongen van de adelaar.")
                                                print("Mijn noodkreet heeft mijn lot bezegeld, en ik verdwijn in de maag van de bergbewoners hoog boven de wolken.\n")
                                                print("[Gestorven door een plotselinge carrièreswitch naar adelaarvoer!]")

                                            elif "veren" in keuze_adelaar.lower():
                                                print("\nMijn handen trillen terwijl ik in paniek aan de veren van de adelaar trek, een impulsieve reactie op de dreigende situatie waarin ik me bevind.")
                                                print("De veren geven mee onder mijn greep, en ik voel de zachte textuur ervan in mijn handen.\n")

                                                print("Echter, mijn poging tot zelfverdediging lijkt weinig effect te hebben.")
                                                print("De adelaar reageert op mijn actie met een scherpe kreet, haar grote ogen bliksemen van verontwaardiging.")
                                                print("In plaats van dat ze schrikt, lijkt mijn handeling haar eerder boos te maken.\n")

                                                print("Met een snelle beweging draait de adelaar zich naar me toe, haar klauwen uitgestrekt.")
                                                print("Ik besef dat ik mijn situatie alleen maar erger heb gemaakt.")
                                                print("De adelaar slaat me met haar vleugel, waardoor ik uit balans raak en tegen de rotsachtige ondergrond stort.")
                                                print("De harde klap veroorzaakt pijn in mijn lichaam, en alles wordt zwart om me heen.\n")
                                                print("[Gestorven door een overdosis veren!]")

                                            else:
                                                print("\nAntwoord alstublieft met 'geruststellen', 'schreeuwen' of 'veren'.\n")
                                                continue
                                            break

                                    elif zwevende_pad.lower() == "midden":
                                        print("\nIk besloot het pad in het midden te volgen.")
                                        print("Het pad leidde me naar een ogenschijnlijk eindeloze mistige vlakte.")
                                        print("Terwijl ik verder liep, verloor ik alle oriëntatie en raakte ik volledig verdwaald.\n")

                                        print("De mist omhult me en elke stap lijkt me verder van de realiteit te voeren.")
                                        print("Uiteindelijk raak ik volledig verdwaald, zonder hoop op een terugweg.\n")

                                        print("[Verdwaald in een droomachtig niemandsland!]")
                                        break

                                    else:
                                        print("\nAntwoord alstublieft met 'links', 'midden' of 'rechts'.\n")
                                        continue
                                    break
                            
                            else:
                                print("\nAntwoord alstublieft met 'zwart' of 'goud'.\n")
                                continue
                            break

                    else:
                        print("\nAntwoord alstublieft met 'ja' of 'nee'.\n")
                        continue
                    break

            elif pick_artefacts.lower() == "nee":
                print("\n[Je besluit om de magische artefacten met rust te laten.]\n")

                print("Terwijl je aarzelde, voelde je plotseling een vreemde trilling in de lucht.")
                print("De magische artefacten reageren onrustig op je weigering.")
                print("Een krachtige energieomslag vindt plaats, en voordat je het weet, word je overspoeld door een magische explosie.")
                print("De boekenplanken schudden, en je wordt weggeblazen door een onzichtbare kracht.")
                print("Als de stofwolken optrekken, bevind je je op mysterieuze wijze op een andere locatie, ver weg van de magische bibliotheek.")
                print("Het lijkt erop dat het negeren van de magische artefacten niet zonder gevolgen is gebleven.")
                print("Je hebt de magische dimensie betreden, en de weg terug lijkt onmogelijk te vinden.\n")

                print("[Verdwaald door de Magische Meltdown!]")

            else:
                print("\nAntwoord alstublieft met 'ja' of 'nee'.\n")
                continue
            break          

    elif keuze_bibliotheek.lower() == "doorgaan":
        print("[Je besloot om snel door te gaan met jouw reis.]")
        print("Mijn stappen leiden me weg van de bibliotheek, op zoek naar onontdekte geheimen in dit magische wereld.\n")

        print("Nadat ik een tijdje door het bos heb gelopen, ontdek ik een schattig dorpje tussen de bomen.")
        print("Kleine huisjes met mooie decoraties trekken mijn aandacht, en het geluid van hamers en smeedwerk komt naar voren.")
        print("En zonder enige aarzeling besluit ik mijn weg naar het dorpje te vervolgen.")
        print("Terwijl ik verder door het dorp loop, begin ik steeds meer op te merken.")
        print("De ambachtelijke winkeltjes zitten propvol met prachtig smeedwerk, en de geur van gesmolten metaal zweeft in de lucht.")
        print("Terwijl ik om me heen kijk, zie ik mensen van een wat kleinere gestalte, stevig gebouwd en duidelijk bedreven in hun ambacht.")
        print("Langzaam dringt het tot me door: dit is geen gewoon dorp; ik ben te midden van dwergen.") 
        print("Een golf van zowel verrassing als nieuwsgierigheid spoelt over me heen.\n")

        print("Ik besluit een van de ambachtelijke winkeltjes binnen te stappen.") 
        print("Het is gevuld met prachtige smeedkunst en unieke voorwerpen.")
        print("Als ik binnenstap, verwelkomt me de geur van gesmolten metaal en het geluid van zachte hamerslagen.")
        print("Ik kijk rond en zie blinkende amuletten, interessante edelstenen en goed gemaakte wapens op de planken.\n")

        print("Terwijl mijn blik zich laat afdwalen door de variatie aan voorwerpen, wordt mijn aandacht getrokken naar een dwerg gehuld in een leren schort.")
        print("De smid lijkt diep verzonken in zijn werk bij de smidse.")
        print("Nieuwsgierig blijf ik staan, terwijl de dwerg bedreven bezig is bij de smidse.")
        print("'Met een vriendelijke groet kijkt hij op en begroet me. 'Welkom, reiziger! Ik ben Thorin, de smid van dit dorp.'")
        print("Hij neemt een moment van aarzeling voordat hij vervolgt,")
        print("'Ik heb een speciale smeedopdracht voor je. Voor het maken van een uniek wapen heb ik een bepaalde hoeveelheid zeldzame stenen nodig, die je kunt vinden in een grot hier in de buurt.")
        print("Als je bereid bent deze uitdaging aan te nemen, zal ik je voorzien van de benodige gereedschappen.' Thorin kijkt me verwachtingsvol aan, in afwachting van mijn antwoord.\n")

        while True:
            print("[Thorin, de bekwame smid van het dorp, heeft een uitdaging voor je!]\n")
            quest_stenen = input("Ben je bereid om de uitdaging van de 'Stenen van Schittering' aan te nemen? (ja/nee): \n")

            if quest_stenen.lower() == "ja":
                print("\n[Je hebt de uitdaging 'Stenen van Schittering' aangenomen!]\n")

                print("Na mijn instemming glijdt er een veelbetekenende glimlach over het gezicht van Thorin. Hij haalt een oude kaart van de grot en een stevige houweel tevoorschijn en overhandigt ze aan mij.\n")
                print("[Versleten map van Donkere Diepten toegevoegd aan inventaris!]")
                inventaris.append("Versleten map van Donkere Diepten")
                print("[Houweel toegevoegd aan inventaris!]")
                inventaris.append("Houweel")

                print("\nJouw taak is om die stenen te verzamelen.")
                print("Hoeveel je precies nodig hebt, vertel ik je niet.")
                print("Breng gewoon alles wat je kunt vinden terug.")
                print("Als je precies genoeg hebt, smeed ik dat speciale wapen voor je.")
                print("En als je meer hebt dan nodig, mag je het overschot verkopen voor extra winst.'")
                print("Thorin wijst vervolgens op de kaart en licht toe waar de Donkere Diepten, de grot die je zoekt, zich bevindt.")
                print("Nadat ik beleefd afscheid had genomen van Thorin, zette ik koers naar de plaats waar de grot zich bevond.\n")

                print("Na een wandeling van ongeveer een half uur, bereik ik de ingang van de grot.")
                print("Voorzichtig zette ik mijn eerste stappen naar binnen, waar het duister mijn omgeving in een mysterieuze gloed hulde. ")
                print("De wanden glinsterden door de weerkaatsing van onbekende mineralen, en de echo van druppelend water vulde de lucht.")
                print("De grot onthulde een doolhof van tunnels.\n")

                print("De grot vertakt zich nu in vijf verschillende tunnels. Welke tunnel zou het beste zijn om te kiezen?")

                while True:
                    vijf_tunnels = input("Welke van deze tunnels lijkt de meest veelbelovende route te zijn? (eerste/tweede/derde/vierde/vijfde): \n")
                    
                    if vijf_tunnels.lower() == "tweede" or vijf_tunnels.lower() == "vijfde":
                        print(f"\n[Je hebt voor de {vijf_tunnels} tunnel gekozen!]\n")

                        print("Plotseling voel ik de aarde onder mijn voeten schudden en de tunnel begint te trillen.")
                        print("Een onheilspellend gerommel vult de lucht en stofwolken stijgen op terwijl de grot begint in te storten.")
                        print("Paniek grijpt me bij de keel terwijl ik ren voor mijn leven, maar de instortende rotsen halen me in.")
                        print("In een ogenblik van duisternis wordt alles stil.\n")

                        print("[Gestorven door een rockconcert zonder de juiste toegangskaart!]")

                    elif vijf_tunnels.lower() == "eerste" or vijf_tunnels.lower() == "derde":
                        print(f"\n[Je hebt voor de {vijf_tunnels} tunnel gekozen!]\n")

                        print("Naarmate je dieper de tunnel in gaat, merk je dat de lucht zwaarder wordt en een verstikkende geur zich verspreidt.")
                        print("Waarschuwingssignalen gaan af in je hoofd, maar het is te laat om om te keren.")
                        print("Plotseling word je overweldigd door giftige gassen die uit de tunnel ontsnappen, en je voelt je bewustzijn vervagen.")
                        print("Je valt op de grond, worstelend voor adem, en de duisternis sluit zich om je heen.\n")

                        print("[Gestorven door een plotselinge verstikkingsangst voor tunnels!]")

                    elif vijf_tunnels.lower() == "vierde":
                        print(f"\n[Je hebt voor de {vijf_tunnels} tunnel gekozen!]\n")

                        print("De tunnel begint breed, maar naarmate je dieper gaat, wordt het pad steeds smaller en benauwder.")
                        print("Je voelt een ongemakkelijke beklemming in de lucht terwijl je verder gaat, maar je zet vastberaden door.")
                        print("Plotseling hoor je een diep rommelend geluid en voel je de trillingen onder je voeten.")
                        print("De rotsen boven je beginnen te schudden en brokstukken vallen naar beneden, blokkerend wat eens de weg naar buiten was.")
                        print("Paniek overvalt je terwijl je beseft dat je geen kant op kunt. De tunnel stort in en je zit gevangen.")
                        print("In de duisternis van de ingestorte tunnel is er geen ontsnappen meer mogelijk.\n")

                        print("[Vastgezeten door een ongeplande grotrenovatie!]")

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
                        print("\nAntwoord alstublieft met 'eerste', 'tweede','derde', 'vierde' of 'vijfde'.\n")
                        continue  
                    break
    
            elif quest_stenen.lower() == "nee":
                print("\n[Je hebt de uitdaging 'Stenen van Schittering' niet aangenomen!]\n")

                print("Na de weigering van de uitdaging 'Stenen van Schittering' besloot ik mijn verkenningstocht door het dwergendorp voort te zetten.")
                print("Terwijl ik door de kronkelende steegjes dwaalde, ontdekte ik een levendige handelsmarkt die het centrum van het dwergendorp verlichtte.")
                print("Kleurrijke kramen stonden vol met exotische waren, van fonkelende edelstenen tot zorgvuldig vervaardigde wapens en handgemaakte voorwerpen.")
                print("Mijn nieuwsgierigheid groeide en ik besloot de markt verder te verkennen.\n")

                print("Terwijl ik tussen de kraampjes liep, werd ik aangesproken door een dwerg genaamd Gimli, een ervaren handelaar uit het dorp.")
                print("Hij was druk bezig met de voorbereidingen voor een handelsmissie naar het elfenkoninkrijk Eldoria.")
                print("Ze waren op zoek naar mensen met diverse vaardigheden om waardevolle goederen vanuit het dwergendorp naar Eldoria te transporteren.\n")

                print("'Heb je ooit gedacht aan het deelnemen aan een handelsmissie naar het elfenkoninkrijk?' vroeg Gimli.")
                print("'We hebben een groep avonturiers verzameld om waardevolle goederen zoals onze prachtige ambachtelijke producten, edelstenen en speciale wapens naar Eldoria te brengen.")
                print("Ze hebben een grote vraag naar onze ambachten en smeedwerk daar.'\n")

                print("Nieuwsgierig naar het aanbod vroeg ik Gimli wat de handelsmissie precies inhield.")
                print("Hij legde uit dat we ambachtelijke producten, edelstenen en speciale wapens van het dwergendorp naar Eldoria zouden brengen.")
                print("Onze taak was om deze goederen te presenteren aan de inwoners van Eldoria en te handelen voor waardevolle elfenproducten.")
                print("Als beloning voor onze inspanningen zouden we worden betaald in verschillende valuta, waaronder gouden, zilveren en bronzen munten.")
                print("Bovendien zouden we de kans krijgen om enkele van de unieke elfenproducten voor onszelf te verkrijgen.\n")

                while True:
                    handels_missie = input("\nWil je de handelsmissie aannemen? (ja/nee): \n")

                    if handels_missie.lower() == "ja":
                        print("\n[Je hebt de handelsmissie aangenomen!]\n")
                        
                        print("Met de handelsmissie geaccepteerd, maak ik mijn weg naar de sfeervolle stallen, waar tot mijn verrassing een prachtig, zwarte rijpaard op me stond te wachten.")
                        print("Zijn glanzende zwarte vacht straalt kracht uit, en zijn gespierde lichaamsbouw belooft zowel snelheid als uithoudingsvermogen.")
                        print("Een witte bles siert zijn hoofd, terwijl zijn ogen nieuwsgierig oplichten bij mijn nadering.\n")

                        def vraag_paard():
                            while True:
                                paard_naam = input("Welke naam wil je aan jouw paard geven? \n")
                                while not paard_naam.isalpha():
                                    print("\nOngeldige invoer. Voer alleen letters in de naam van uw paard.\n")
                                    paard_naam = input("Welke naam wil je aan jouw paard geven? \n")

                                bevestiging_paard = input(f"\nWeet je zeker dat je jouw paard {paard_naam} wilt noemen? (ja/nee): \n").lower()
                                while bevestiging_paard not in ["ja", "nee"]:
                                    print("\nAntwoord alstublieft met 'ja' of 'nee'.\n")
                                    bevestiging_paard = input(f"\nWeet je zeker dat je jouw paard {paard_naam} wilt noemen? (ja/nee): \n").lower()

                                if bevestiging_paard == "ja":
                                    return paard_naam
                                
                        paard_naam = vraag_paard()

                        print(f"\nMet enthousiasme voorzie ik mijn nieuwe metgezel, {paard_naam}, van een zadel.\n")

                        print(f"Samen met mijn prachtige metgezel, {paard_naam}, begin ik aan de avontuurlijke reis naar het elfenkoninkrijk Eldoria.")
                        print("De zon staat hoog aan de hemel terwijl we door weelderige bossen en uitgestrekte velden trekken, de frisse wind waait door mijn haren.")
                        print("Onderweg ontmoeten we reizigers en handelaren die de levendigheid van de handelsroute benadrukken.")
                        print("De geur van bloemen vermengt zich met het getjilp van vogels, en de wereld lijkt te bruisen van leven en magie.\n")

                        print("Na een dag reizen bereiken we de grens van Eldoria, bewaakt door majestueuze bomen en bewegende wachters.")
                        print("Hun sierlijke bewegingen stralen een kalme kracht uit, en hun ogen schitteren met wijsheid.")
                        print("Met een vriendelijke groet laten ze ons door, en we betreden het elfenkoninkrijk.\n")

                        print("Eldoria begroet ons met betoverende architectuur en sprankelende fonteinen.")
                        print("De straten zijn gevuld met elfen van alle leeftijden, hun sierlijke tred en gracieuze houding verraden de verbondenheid met de natuur om hen heen.")
                        print("We worden geleid naar het marktplein, waar kleurrijke kraampjes en delicate handelswaren de rijkdom van Eldoria weerspiegelen.\n")

                        print("Gimli begint met het tonen van onze handelswaren, en ik observeer de reacties van de elfen.")
                        print("Plotseling verschijnen er echter elvenwachters om ons heen, hun gezichten ernstig en hun ogen doordringend.")
                        print("Ze beschuldigen ons van spionage en ongeoorloofde handelsactiviteiten in Eldoria.")
                        print("In verwarring en geschokt door de onverwachte wending van gebeurtenissen, worden we gearresteerd en weggeleid naar de koninklijke rechtbank voor verhoor.")
                        print("Onze handelsmissie neemt een onverwachte wending, en de toekomst lijkt plotseling onzeker.\n")

                        print("[Elfengevangenis: handelde te serieus, niet cool!]")

                    elif handels_missie.lower() == "nee":
                        print("\nNa het afzeggen van de handelsmissie merk ik dat de sfeer in het dwergendorp steeds grimmiger wordt.")
                        print("De dwergen zien mij als degenen die hun kansen op welvaart en vrede met de elfen hebben verspeeld.")
                        print("Als ik door de smalle straatjes loop, hoor ik gefluister en krijg ik vuile blikken toegeworpen.\n")

                        print("Op een dag word ik benaderd door een groep verbitterde dwergen, vastbesloten om mij de schuld te geven van de mislukte handelsmissie.")
                        print("De confrontatie escaleert snel en resulteert in een gewelddadige confrontatie.")
                        print("Ondanks mijn moedige pogingen om te verdedigen, word ik overweldigd door hun aantal en raak ik ernstig gewond.\n")

                        print("De dwergen, woedend door de gevolgen van mijn beslissing, besluiten dat ik een bedreiging vormt voor de harmonie van het dorp.")
                        print("Ze verbannen me naar de donkere, gevaarlijke wildernis buiten het dwergendorp.")
                        print("In deze meedogenloze omgeving sta ik voor talloze gevaren, variërend van hongerige roofdieren tot onbekende vijandige wezens.\n")

                        print("Gedurende mijn verbanning worstel ik om te overleven.")
                        print("Ik zoekt wanhopig naar een veilige uitweg, maar de wildernis is meedogenloos.")
                        print("Uiteindelijk, verzwakt en uitgeput, kom ik oog in oog te staan met een mysterieuze, duistere kracht die me gevangen neemt.\n")

                        print("[Harmonie? Dwergendorp denkt van niet - Exit 'harmonie'!]")

                    else:
                        print("\nAntwoord alstublieft met 'ja' of 'nee'.\n")
                        continue
                    break

            else:
                print("\nAntwoord astublieft met 'ja' of 'nee'.\n")
                continue
            break       

    else:
        print("\nAntwoord alstublieft met 'tijd' of 'doorgaan'.\n")
        continue
    break