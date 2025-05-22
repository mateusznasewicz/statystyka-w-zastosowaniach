# Mateusz Nasewicz
import pandas as pd

df = pd.read_csv('Dane_zadanie_1.txt', delimiter='\t')

for col in df.columns[3:]:
    df[col] = df[col].str.replace(',', '.').astype(float)

df_osoba = df[['Imię','Nazwisko']].copy()
df_osoba['Średnia'] = df.iloc[:, 3:].mean(axis=1)
df_osoba['Wariancja'] = df.iloc[:, 3:].var(axis=1)
df_osoba['Odchylenie'] = df.iloc[:, 3:].std(axis=1)

df_przedmiot = df.iloc[:, 3:].agg(['mean', 'var', 'std']).transpose().reset_index()
df_przedmiot.columns = ['Przedmiot', 'Średnia', 'Wariancja', 'Odchylenie']

klasy = df['Klasa'].unique()
df_klasa = pd.DataFrame({'Klasa':klasy})
for index, klasa in enumerate(klasy):
    oceny = df[df['Klasa'] == klasa].iloc[:, 3:].values.flatten()
    df_klasa.loc[index,'Średnia'] = oceny.mean()
    df_klasa.loc[index,'Wariancja'] = oceny.var()
    df_klasa.loc[index,'Odchylenie'] = oceny.std()

print(df_osoba, end='\n\n')
print(df_przedmiot, end='\n\n')
print(df_klasa)






