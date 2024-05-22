import pandas as pd

students = ['Andrew', 'Brie', 'Kanika']

estudantes = pd.Series(students)

ages = [27, 49, 37]

idades = pd.Series(ages)

heights = [167.4, 173.2, 190.0]

alturas = pd.Series(heights)

mixed = [True, 'say', {'my_mood': 100}]

mistura = pd.Series(mixed)

print(mistura)