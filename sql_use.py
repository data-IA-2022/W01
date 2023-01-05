import glob, sys, sqlite3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from colorama import Fore, Back, Style

conn = sqlite3.connect('bdd.sqlite')

df = pd.read_sql("""select "Code Pays",Pays,Valeur  AS Valeur_population from population;""", conn)
#print(df)

df = pd.read_sql("""select "Code Pays",Pays,Valeur AS Valeur_cereal from cereal WHERE Élément='Production' AND Produit="Blé" ORDER BY "Code Pays";""", conn)
#print(df)

SQL = '''
SELECT population."Code Pays", population."Pays", population.Valeur AS population, cereal.Valeur AS cereal
FROM population INNER JOIN cereal
ON (population."Code Pays" = cereal."Code Pays")
WHERE (cereal.Élément='Production' AND cereal.Produit="Blé")
ORDER BY population."Code Pays"
; 
'''

df = pd.read_sql(SQL, conn)
print(df)