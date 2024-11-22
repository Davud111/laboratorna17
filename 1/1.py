import pandas as pd
import math
import csv

df = pd.read_csv("1/vectors.csv", sep=",")

vectorLengths = dict([{"Name", "Length"}])

for ind in df.index:
    vectorLengths[df["Name"][ind]] = math.sqrt(df["x"][ind]**2 + df["y"][ind]**2)
print(vectorLengths)

with open('1/vector_len.csv', 'w') as csv_file:  
    writer = csv.writer(csv_file)
    for key, value in vectorLengths.items():
       writer.writerow([key, value])
