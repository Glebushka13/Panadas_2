import pandas as pd

df = pd.DataFrame({
    "City": ["Riga", "Liepaja", "Riga"]
})

result = pd.get_dummies(df)

print(result)
#Konvertēt kategoriskos mainīgos par fiktīviem/indikatoru mainīgajiem. Katrs mainīgais tiek konvertēts tik daudzos 0/1 mainīgajos, cik ir dažādu vērtību. Katras izvades kolonnas nosaukums ir norādīts pēc vērtības; ja ievade ir DataFrame, sākotnējā mainīgā nosaukums tiek pievienots vērtībai.
