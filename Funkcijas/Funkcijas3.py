import pandas as pd

scores = [50, 60, 70, 80, 90, 100]

result = pd.qcut(scores, q=3)

print(result)
#Diskretizēt mainīgo vienāda lieluma segmentos, pamatojoties uz rangu vai izlases kvantilēm. Piemēram, 1000 vērtības 10 kvantilēm ģenerētu kategorisku objektu, kas norāda kvantiles piederību katram datu punktam.
