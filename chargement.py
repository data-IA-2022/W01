import pandas as pd
import numpy as np
from sqlalchemy import create_engine
import os, yaml # credentials:

with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)
#print(config)

cfg=config['PG']
print(cfg)

url = "{driver}://{user}:{password}@{host}/{database}".format(**cfg)
print('URL', url)

engine = create_engine(url)

files=['name.basics', 'title.akas', 'title.basics', 'title.crew', 'title.episode', 'title.principals', 'title.ratings']

for name in files:
    print(f"Chargement {name}")
    df = pd.read_csv(f"data/{name}.tsv.gz", sep='\t', compression='gzip', nrows=1000)
    print(df.shape)
    df.to_sql(name.replace('.', '_'), engine, if_exists='replace') # , index=False

