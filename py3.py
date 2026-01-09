with open("szoveg.txt", "w", encoding="utf-8") as f:
    f.write("Python egy programozási nyelv\nNagyon népszerű\nKönnyen tanulható")

with open("szoveg.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

line_count = len(lines)
word_count = sum(len(line.split()) for line in lines)

print("Sorok száma:", line_count)
print("Szavak száma:", word_count)