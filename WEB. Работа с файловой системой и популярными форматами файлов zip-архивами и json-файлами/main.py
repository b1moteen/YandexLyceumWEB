f = open("Задача.csv", "r")
s = f.readlines()
s = [line.rstrip() for line in s]
chisla = []
for line in s:
    line = list(map(int, line.split(";")))
    chisla.append(line)
f.close()
for ie in range(len(chisla[0])):
    ie
weewe




