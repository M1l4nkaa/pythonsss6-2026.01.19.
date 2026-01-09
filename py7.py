diakok = {}

with open("diakok.txt", "r", encoding="utf-8") as f:
    for sor in f:
        nev, jegy = sor.strip().split(";")
        diakok[nev] = int(jegy)

legjobb = max(diakok, key=diakok.get)
atlag = sum(diakok.values()) / len(diakok)

print("Legjobb tanuló:", legjobb)
print("Osztályátlag:", round(atlag, 2))
