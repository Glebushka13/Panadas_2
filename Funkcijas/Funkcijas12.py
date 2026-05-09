import pandas as pd

df = pd.DataFrame({
    "id": [1, 2],
    "Math_2023": [90, 85],
    "Math_2024": [95, 88]
})

result = pd.lreshape(df, {
    "Math": ["Math_2023", "Math_2024"]
})

print(result)
#Novērtējiet Python izteiksmi kā virkni, izmantojot dažādas aizmugures sistēmas