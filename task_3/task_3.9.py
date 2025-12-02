lines = []
while True:
    line = input()
    lines.append(line)
    if not line:
        break
for l in lines:
    A = []
    foundednums = ""
    for char in l:
        if char.isdigit():
            foundednums += char
        elif foundednums:
            A.append(foundednums)
            foundednums = ""
    if foundednums != "":
        A.append(foundednums)
    print(", ".join(A))