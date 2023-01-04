import glob, sys
import pandas as pd

print(f"parametres : {sys.argv[1:]}")

#fns = glob.glob('fao_2013/*.csv')
#fns = glob.glob('**/*.csv', recursive=True)
names = ['Code Domaine', 'Domaine', 'Code Pays', 'Pays', 'Code Élément',
         'Élément', 'Code Produit', 'Produit', 'Code Année', 'Année', 'Unité',
         'Valeur', 'Symbole', 'Description du Symbole']

for fn in sys.argv[1:]:
    df = pd.read_csv(fn, names=names, header=0)
    df.index = df['Code Pays']
    print(f"- {fn:50} {df.shape}")
    print(df.columns)
    print(df)

