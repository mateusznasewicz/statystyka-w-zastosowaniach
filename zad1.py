# Mateusz Nasewicz
import pandas as pd

df = pd.read_csv("Dane_zadanie_1", sep="\t")
estymatory = ["Średnia","Wariancja","Odchylenie"]
klasy = list(set(df["Klasa"]))
przedmioty = df.drop(columns=["Imię","Nazwisko","Klasa"]).columns.values

osoby_df = pd.DataFrame(columns=["Imię","Nazwisko"]+estymatory)
przedmioty_df = pd.DataFrame(columns=["Przedmiot"]+estymatory)
klasy_df = pd.DataFrame(columns=["Klasa"]+estymatory)

osoby_df["Imię"] = df["Imię"]
osoby_df["Nazwisko"] = df["Nazwisko"]
przedmioty_df["Przedmiot"] = przedmioty
klasy_df["Klasa"] = klasy

# Przedmioty
for przedmiot in przedmioty:
    przedmioty_df[przedmiot]["Średnia"] = df[przedmiot].mean()
    przedmioty_df[przedmiot]["Wariancja"] = 0
    przedmioty_df[przedmiot]["Odchylenie"] = 0

# Klasy
for klasa in klasy:
    pass


# Osoby


