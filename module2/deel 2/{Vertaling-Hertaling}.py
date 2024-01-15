original_text = "'Op een zonnige dag wandelde Lisa door het bloemrijke park. Plotseling kwam ze een nieuwsgierige egel tegen die haar begroette met een vrolijk gepiep. Ze besloten samen een avontuur te beleven en ontdekten een betoverend bos vol kleurrijke paddenstoelen en sprankelende feeën.'"

translation = {
    'zonnige' : 'regenachtige',
    'bloemrijke' : 'betonnen',
    'park' : 'parkeergarage',
    'nieuwsgierige' : 'slaperige',
    'egel' : 'schildpad',
    'vrolijk' : 'slaperig',
    'gepiep' : 'geblaf',
    'avontuur' : 'dutje',
    'betoverend' : 'verwarrend',
    'kleurrijke' : 'grijze',
    'paddenstoelen' : 'snoepjes',
    'sprankelende' : 'verdrietige',
    'feeën' : 'kabouters',
}

translated_text = str(original_text)

for key, value in translation.items():
    translated_text = translated_text.replace(key, value)

print(f"Original: {original_text}\n")

print(f"Translation: {translated_text}")