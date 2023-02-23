import pandas as pd
import numpy as np
from sqlalchemy import create_engine, types
import os, yaml # credentials:

with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)
print(config)

cfg=config['mysql-datalab']
print(cfg)

url = "{driver}://{user}:{password}@{host}/{database}?autocommit=true".format(**cfg)
print('URL', url)

engine = create_engine(url)

yearConv=lambda x: (int(x) if x.isnumeric() else None)
bnConv=lambda x: (x if x!="\\N" else None)

def load_tbl(name):
    print(f"Chargement {name}")
    tbl=name.replace('.', '_')
    nl=0
    engine.execute(f"DELETE FROM {tbl};")
    reader = pd.read_csv(f"data/{name}.tsv.gz",
                     sep='\t',
                     compression='gzip',
                     #nrows=5000,
                     chunksize=1E6,
                     #dtype={'birthYear': np.int32},
                     # https://stackoverflow.com/questions/34139102/whats-the-difference-between-dtype-and-converters-in-pandas-read-csv
                     converters={'birthYear': yearConv,
                                 'deathYear': yearConv,
                                 'seasonNumber': yearConv,
                                 'episodeNumber': yearConv,
                                 'endYear': yearConv,
                                 'startYear': yearConv,
                                 'runtimeMinutes': yearConv,
                                 'directors': bnConv,
                                 'writers': bnConv,
                                 },
                     )
    for df in reader:
        nl+=df.shape[0]
        print(f"  {nl} lines")
        df.to_sql(tbl, engine,
              if_exists='append',
              index=False,
              chunksize=10000,
              )

load_tbl('title.basics')
load_tbl('title.crew')
load_tbl('title.episode')

quit()

files=['title.basics', 'title.crew', 'name.basics', 'title.akas', 'title.episode', 'title.principals', 'title.ratings']
#files=['name.basics']

'''for fn in files:
    print(fn)
    tbl=fn.replace('.', '_')
    df = pd.read_csv(f"data/{fn}.tsv.gz",
                     sep='\t',
                     compression='gzip',
                     nrows=5000,
                     #chunksize=1000000
                     )
    print(df.shape)
    df.to_sql(tbl, engine,
              if_exists='replace',
              index=False,
              chunksize=5000,
              ) # , index=False
    del df
'''



for name in files:
    print(f"Chargement {name}")
    tbl=name.replace('.', '_')
    #engine.execute(f"DELETE FROM {tbl};")

    df = pd.read_csv(f"data/{name}.tsv.gz",
                     sep='\t',
                     compression='gzip',
                     nrows=5000,
                     #dtype={'birthYear': np.int32},
                     # https://stackoverflow.com/questions/34139102/whats-the-difference-between-dtype-and-converters-in-pandas-read-csv
                     converters={'birthYear': yearConv,
                                 'deathYear': yearConv,
                                 },
                     )
    print(df.shape)
    df.to_sql(tbl, engine,
              if_exists='replace',
              index=False,
              dtype={'birthYear': types.INTEGER(),
                     'deathYear': types.INTEGER()}
              ) # , index=False
