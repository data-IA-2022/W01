import glob, sys, sqlite3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Noms de colonnes à utiliser
names = ['Code Domaine', 'Domaine', 'Code Pays', 'Pays', 'Code Élément',
         'Élément', 'Code Produit', 'Produit', 'Code Année', 'Année', 'Unité',
         'Valeur', 'Symbole', 'Description du Symbole']

# Récupération de la liste de CSV si fournie
# Ou utilisation de glob
fns = sys.argv[1:]
if not fns:
    fns = glob.glob('*/*.csv') # 'fao_2013/*.csv'
print(f"parametres : {fns}")

#fns = glob.glob('fao_2013/*.csv')
#fns = glob.glob('**/*.csv', recursive=True)

# Lecture puis affichage des info taille des CSV
for fn in fns:
    df = pd.read_csv(fn, names=names, header=0)
    df.index = df['Code Pays']
    print(f"- {fn:^50s} ({df.shape[0]:6d}, {df.shape[1]:2d})")
    #print(df.columns)
    #print(df)

