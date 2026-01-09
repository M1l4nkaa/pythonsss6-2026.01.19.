with open("szamok.txt", "r") as be:
    szamok = be.readlines()

with open("paros.txt", "w") as ki:
    for sor in szamok:
        szam = int(sor.strip())
        if szam % 2 == 0:
            ki.write(str(szam) + "\n")
