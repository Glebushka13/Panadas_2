import pandas as pd
import numpy as np

arr = np.array([1, 2, 3, 4])

result = pd.util.hash_array(arr)

print(result)
#Uzminiet dotās datuma/laika virknes datuma/laika formātu. Šī funkcija mēģina izsecināt dotās datuma/laika virknes formātu. Tā ir noderīga situācijās, kad datuma/laika formāts nav zināms un ir jānosaka pareizai parsēšanai.
