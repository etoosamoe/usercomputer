class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'


file1 = r'\\serv\log\User-computer.txt' #путь к файлу, по умолчанию только для чтения r = сырая строка
a = 1                                   # тупое решение, чтобы скрипт не закрывался
while a == 1:
    print(bcolors.HEADER + '\n' + '-' * 30 + bcolors.ENDC)
    word = input("Введите имя компа, учетку пользователя...: ")
    print()
    chik = open(file1)
    for line in chik:
        if word.lower() in line.lower():# опускание текста строки в нижний регистр, чтобы быть независимыми
            splittedline = line.split() # разделяет строку по пробелам

            # переменные с элементами списка, который создался после разделения по пробелам
            name = splittedline[0]
            hostname = splittedline[3]
            date = splittedline[1]
            time = splittedline[2]

            print (bcolors.OKGREEN + "{:>18}".format(name) + bcolors.OKBLUE + " {:>18}".format(hostname) + bcolors.FAIL + " {:>18}".format(date) + bcolors.FAIL + " {:>18}".format(time)) # разделяет по 18 символов
