class flog:
    def print_console(self):
        log = '/Users/a111/Developer/Programming/Parser/log1.txt'
        lists = []
        with open(log, 'r', encoding='utf8') as f:
            for line in f:
                if re.search(r'XIMSS|CALLLEG', line):
                    print(line)
                lists.append(line)
    def save_logs():
        log = '/Users/a111/Developer/Programming/Parser/log1.txt'
        lists = []
        with open(log, 'r', encoding='utf8') as f:
            for line in f:
                lists.append(line)
        a = int(input("Введите число: "))
        for i in range(a):
            numbers = input(f"Введите какой код для {i+1}-го XIMISS нужно сохранить (Например XIMISS-000003): ")
            with open(f"{i+1}.txt", "w+", encoding='utf8') as file:
                for line in lists:
                    if re.search(r'XIMSS-' + numbers, line):
                        file.write(line)
flog.save_logs()
