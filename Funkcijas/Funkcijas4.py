import pandas as pd

df1 = pd.DataFrame({
    "ID": [1, 2, 3],
    "Name": ["Anna", "Janis", "Liga"]
})

df2 = pd.DataFrame({
    "ID": [1, 2, 3],
    "Score": [90, 85, 95]
})

result = pd.merge(df1, df2, on="ID")

print(result)
#Apvienojiet DataFrame vai nosauktos Series objektus ar datubāzes stila savienojumu