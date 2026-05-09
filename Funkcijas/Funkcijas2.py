import pandas as pd

df = pd.DataFrame({
    "Name": ["Anna", "Anna", "Janis", "Janis"],
    "Subject": ["Math", "English", "Math", "English"],
    "Score": [90, 88, 85, 92]
})

result = df.pivot(index="Name", columns="Subject", values="Score")

print(result)
#Atgriezt pārveidotu DataFrame, kas sakārtots pēc dotajām indeksa/kolonnas vērtībām
