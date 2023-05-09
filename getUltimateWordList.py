import pandas as pd

with open("ULTIMATE_WORDS.txt") as f:
    Ultimate_Word_database = []
    for line in f:
        Ultimate_Word_database.append(line.strip())

#print(Ultimate_Word_database)
print(len(Ultimate_Word_database))



UltimateWord_DataFrame=[]
df = pd.DataFrame(UltimateWord_DataFrame,columns = ['Words'])

z=0

while z < len(Ultimate_Word_database):
    df.loc[len(df)] = Ultimate_Word_database[z]
    z=z+1
    print(z)

print(df['Words'].size)

df = df.drop_duplicates(keep='first')

print(df['Words'].size)

print("end")