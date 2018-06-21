file1 = r'\\serv\log\User-computer.txt' #путь к файлу, по умолчанию только для чтения r = сырая строка
a = 1                                   # тупое решение, чтобы скрипт не закрывался
while a == 1:
    print('\n' + '-' * 30)
    word = input("Введите имя компа, учетку пользователя...: ")
    chik = open(file1)
    for line in chik:
        if word.lower() in line.lower():# опускание текста строки в нижний регистр, чтобы быть независимыми
            splittedline = line.split() # разделяет строку по пробелам

            # переменные с элементами списка, который создался после разделения по пробелам
            name = splittedline[0]
            hostname = splittedline[3]
            date = splittedline[1]
            time = splittedline[2]

            print ("{:>18} {:>18} {:>18} {:>18} ".format(name, hostname, date, time)) # разделяет по 18 символов
