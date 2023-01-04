import glob, sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

names = ['Code Domaine', 'Domaine', 'Code Pays', 'Pays', 'Code Élément',
         'Élément', 'Code Produit', 'Produit', 'Code Année', 'Année', 'Unité',
         'Valeur', 'Symbole', 'Description du Symbole']

# CEREALS
fn_cereal='fao_2013/FAOSTAT_2013_cereal.csv'
df_cereal = pd.read_csv(fn_cereal, names=names, header=0)
df_cereal.index = df_cereal['Code Pays']

selection = df_cereal['Élément']=='Production'
#print(selection)
df_cereal = df_cereal[selection]
#print(df_cereal)
df_cereal = df_cereal[df_cereal['Produit']=='Blé']
df_cereal = df_cereal[['Valeur']]
print(df_cereal)

# POPULATION

fn_pop='fao_2013/FAOSTAT_2013_population.csv'
df_pop = pd.read_csv(fn_pop, names=names, header=0)
df_pop.index = df_pop['Code Pays']
#df_pop.set_index('Code Pays')
df_pop = df_pop[['Valeur', 'Pays']]
print(df_pop)

print('-------------------------------------')
df = df_cereal.join(df_pop, how='outer', lsuffix='_cereal', rsuffix='_population')
print(df)
df.to_csv('tmp.csv')

np.random.seed(19680801)
N = 50
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
area = (30 * np.random.rand(N))**2  # 0 to 15 point radii

x = np.log(df['Valeur_population'])
y = np.log(df['Valeur_cereal'])

plt.scatter(x, y)

for i,x in df.iterrows():
    #print(x['Pays'], (log(x['Valeur_population']), x['Valeur_cereal']))
    plt.annotate(x['Pays'], (np.log(x['Valeur_population']), np.log(x['Valeur_cereal'])))

plt.show()

quit()

print(f"parametres : {sys.argv[1:]}")

#fns = glob.glob('fao_2013/*.csv')
#fns = glob.glob('**/*.csv', recursive=True)
for fn in sys.argv[1:]:
    df = pd.read_csv(fn, names=names, header=0)
    df.index = df['Code Pays']
    print(f"- {fn:50} {df.shape}")
    print(df.columns)
    print(df)

