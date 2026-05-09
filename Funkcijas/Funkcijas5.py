import pandas as pd

df1 = pd.DataFrame({
    "Date": ["2024-01", "2024-02"],
    "Sales": [100, 150]
})

df2 = pd.DataFrame({
    "Date": ["2024-01", "2024-03"],
    "Profit": [20, 40]
})

result = pd.merge_ordered(df1, df2)

print(result)
#Veikt sakārtotu datu apvienošanu ar papildu aizpildīšanu/interpolāciju
