# Mateusz Nasewicz
import pandas as pd

df = pd.read_csv('Dane_zadanie_1.txt', delimiter='\t')

for col in df.columns[3:]:
    df[col] = df[col].str.replace(',', '.').astype(float)

df_osoba = df.copy()
df_osoba['Średnia'] = df_osoba.iloc[:, 3:].mean(axis=1)
df_osoba['Wariancja'] = df_osoba.iloc[:, 3:-1].var(axis=1)
df_osoba['Odchylenie'] = df_osoba.iloc[:, 3:-2].std(axis=1)
df_osoba = df_osoba[['Imię','Nazwisko','Średnia','Wariancja','Odchylenie']]

df_przedmiot = df.iloc[:, 3:].agg(['mean', 'var', 'std']).transpose().reset_index()
df_przedmiot.columns = ['Przedmiot', 'Średnia', 'Wariancja', 'Odchylenie']

klasy_oceny = dict.fromkeys(df['Klasa'].unique())
df_klasa = pd.DataFrame({'Klasa':klasy_oceny.keys()})
for index, klasa in enumerate(klasy_oceny.keys()):
    oceny = df[df['Klasa'] == klasa].iloc[:, 3:].values.flatten()
    df_klasa.at[index,'Średnia'] = oceny.mean()
    df_klasa.at[index,'Wariancja'] = oceny.var()
    df_klasa.at[index,'Odchylenie'] = oceny.std()

print(df_osoba, end='\n\n')
print(df_przedmiot, end='\n\n')
print(df_klasa)






