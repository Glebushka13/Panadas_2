import pandas as pd

df1 = pd.DataFrame({
    "Name": ["Anna", "Janis"]
})

df2 = pd.DataFrame({
    "Name": ["Liga", "Karlis"]
})

result = pd.concat([df1, df2])

print(result)
#Savieno pandas objektus pa noteiktu asi. Ļauj iestatīt papildu loģiku pa pārējām asīm. Var arī pievienot hierarhiskas indeksēšanas slāni savienošanas asij, kas var būt noderīgi, ja etiķetes ir vienādas (vai pārklājas) uz nodotā ​​ass numura.
