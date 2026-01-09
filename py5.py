hiba_db = 0

with open("naplo.txt", "r", encoding="utf-8") as f:
    for sor in f:
        if "HIBA" in sor:
            hiba_db += 1

print("HIBA bejegyzések száma:", hiba_db)
