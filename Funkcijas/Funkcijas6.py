import pandas as pd

df1 = pd.DataFrame({
    "time": [1, 5, 10],
    "value": ["A", "B", "C"]
})

df2 = pd.DataFrame({
    "time": [2, 6, 12],
    "score": [100, 200, 300]
})

result = pd.merge_asof(df1, df2, on="time")

print(result)
#Veikt apvienošanu pēc atslēgas attāluma. Tas ir līdzīgi kā kreisās puses savienošana, izņemot to, ka mēs salīdzinām pēc tuvākās atslēgas, nevis vienādām atslēgām. Pirms šīs funkcijas izsaukšanas abi DataFrame vispirms ir jāsakārto pēc apvienošanas atslēgas augošā secībā. Kārtošana pēc jebkādām papildu grupēšanas kolonnām "pēc" nav nepieciešama.
