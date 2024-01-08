dagen_van_de_week = ('maandag','dinsdag','woensdag','donderdag','vrijdag','zaterdag','zondag')

print('Alle dagen van de week zijn:')
for dag in dagen_van_de_week:
    print(dag)

print("\nDe werkdagen zijn:")
for dag in dagen_van_de_week[:5]:
    print(dag)

print("\nDe weekenddagen zijn:")
for dag in dagen_van_de_week[5:]:
    print(dag)

print("\nDe werkdagen zijn in omgekeerde volgorde:")
for dag in reversed(dagen_van_de_week[:5]):
    print(dag)

print("\nDe weekenddagen zijn in omgekeerde volgorde:")
for dag in reversed(dagen_van_de_week[5:]):
    print(dag)