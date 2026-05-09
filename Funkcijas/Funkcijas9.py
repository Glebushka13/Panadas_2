import pandas as pd

cities = ["Riga", "Liepaja", "Riga", "Ventspils"]

codes, uniques = pd.factorize(cities)

print("Codes:")
print(codes)

print("Unique values:")
print(uniques)
#Kodējiet objektu kā uzskaitītu tipu vai kategorisku mainīgo