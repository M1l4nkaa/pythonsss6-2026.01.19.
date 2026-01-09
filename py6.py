with open("jegyek.txt", "w", encoding="utf-8") as f:
    f.write("5\n4\n3\n5\n2")

with open("jegyek.txt", "r", encoding="utf-8") as f:
    grades = [int(line.strip()) for line in f]

average = sum(grades) / len(grades)

with open("atlag.txt", "w", encoding="utf-8") as f:
    f.write(str(average))
