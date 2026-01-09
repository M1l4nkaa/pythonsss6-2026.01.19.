with open("eredeti.txt", "r", encoding="utf-8") as f:
    sorok = f.readlines()

with open("forditott.txt", "w", encoding="utf-8") as f:
    for sor in reversed(sorok):
        f.write(sor.strip()[::-1] + "\n")
