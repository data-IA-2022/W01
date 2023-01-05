import glob, sys, sqlite3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from colorama import Fore, Back, Style

conn = sqlite3.connect('bdd.sqlite')

df = pd.read_sql_query("""select "Code Pays",Pays,Valeur from population;""", conn)
print(df)