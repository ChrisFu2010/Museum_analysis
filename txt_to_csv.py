import pandas as pd

read_file = pd.read_csv(r'data_museum.txt')
read_file.to_csv(r'museum.csv', index=None)
