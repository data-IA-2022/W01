import glob
import pandas as pd

#fns = glob.glob('fao_2013/*.csv')
fns = glob.glob('**/*.csv', recursive=True)

for fn in fns:
    df = pd.read_csv(fn)
    print(f"- {fn:50} {df.shape}")
