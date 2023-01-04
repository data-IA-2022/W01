import glob, sys
import pandas as pd

print(f"parametres : {sys.argv[1:]}")

#fns = glob.glob('fao_2013/*.csv')
#fns = glob.glob('**/*.csv', recursive=True)

for fn in sys.argv[1:]:
    df = pd.read_csv(fn)
    print(f"- {fn:50} {df.shape}")
