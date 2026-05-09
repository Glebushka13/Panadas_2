import pandas as pd

df = pd.DataFrame({
    "Name": ["Anna", "Janis"],
    "Math": [90, 85],
    "English": [88, 92]
})

result = pd.melt(df, id_vars=["Name"])

print(result)
#Šī funkcija ir noderīga, lai pārveidotu DataFrame formātā, kurā viena vai vairākas kolonnas ir identifikatora mainīgie (id_vars), bet visas pārējās kolonnas tiek uzskatītas par izmērītajiem mainīgajiem (value_vars) un ir “nepagrieztas” rindas asī, atstājot tikai divas kolonnas bez identifikatora — “variable” un “value”.
