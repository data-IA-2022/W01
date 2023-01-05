import glob, sys, sqlite3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Noms de colonnes à utiliser
names = ['Code Domaine', 'Domaine', 'Code Pays', 'Pays', 'Code Élément',
         'Élément', 'Code Produit', 'Produit', 'Code Année', 'Année', 'Unité',
         'Valeur', 'Symbole', 'Description du Symbole']

# CSV CEREALS
fn_cereal='fao_2013/FAOSTAT_2013_cereal.csv'
df_cereal = pd.read_csv(fn_cereal, names=names, header=0)
df_cereal.index = df_cereal['Code Pays'] # écrase l'index

# Filtration des colonnes
selection = df_cereal['Élément']=='Production'
#print(selection)
df_cereal = df_cereal[selection]
#print(df_cereal)
df_cereal = df_cereal[df_cereal['Produit']=='Blé']
df_cereal = df_cereal[['Valeur']]
# Suppression des valeurs nulles
df_cereal = df_cereal[df_cereal['Valeur']>0]

print(df_cereal)

# CSV POPULATION

fn_pop='fao_2013/FAOSTAT_2013_population.csv'
df_pop = pd.read_csv(fn_pop, names=names, header=0)
df_pop.index = df_pop['Code Pays']
#df_pop.set_index('Code Pays')
# On garde les colonnes Valeur & Pays
df_pop = df_pop[['Valeur', 'Pays']]
print(df_pop)

print('-------------------------------------')
# Jointure entre population & céréales avec utilisation de suffixes
df = df_cereal.join(df_pop, how='outer', lsuffix='_cereal', rsuffix='_population')
print(df)
# Enregistrement dans un CSV
df.to_csv('tmp.csv')

# Récupère mes X et Y, en LOG
x = np.log(df['Valeur_population'])
y = np.log(df['Valeur_cereal'])

plt.scatter(x, y) # le graph

# Ajout des labels pour chaque ligne (coordonnées en LOG)
for i,x in df.iterrows():
    plt.annotate(x['Pays'], (np.log(x['Valeur_population']), np.log(x['Valeur_cereal'])))

# Affichage
plt.show()

#plt.scatter(x, y) # le graph
#plt.show()

