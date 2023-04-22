import re
log = './log1.txt'
lists = []
a = str(input("Введите первую циферку (5 нулей): "))
b = str(input("Введите вторую циферку (так же 5 нуликов): "))
with open(log, 'r', encoding='utf8') as f:
    for line in f:
        if re.search(r'XIMSS|CALLLEG', line):
            print(line)
        lists.append(line)


with open("ximss-a.txt", "w+", encoding='utf8') as file:
    for line in lists:
        if re.search(r'XIMSS-'+a, line):
            file.write(line)
with open("ximss-b.txt", "w+", encoding='utf8') as file:
    for line in lists:
        if re.search(r'XIMSS-'+b, line):
            file.write(line)