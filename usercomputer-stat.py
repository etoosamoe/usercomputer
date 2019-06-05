file1 = r'\\serv\log\User-Computer-SPB.txt'  # путь к файлу, по умолчанию только для чтения r = сырая строка


def create_table(): #создает таблицу из файла
    result = []
    file = open(file1)
    for line in file:
        splline = line.split()
        name = splline[0]
        hostname = splline[3]
        date = splline[1]
        time = splline[2]
        result.append([name, hostname, date, time])
    return result


def unique_hostnames(data): #создает таблицу уникальных хостнеймов
    result = []
    for row in data:
        if row[1] not in result:
            result.append(row[1])
    return result


def print_top10(data): #печатает таблицу
    print('Хостнейм           | Как часто        |')
    print('---------------------------------------')
    for row in data[:100]:
        print('{:>18} | {:>18} '.format(row[0], row[1]))


usercomp = create_table()
unique = unique_hostnames(usercomp)

full_table = []
for hostname in unique:
    host_sum = 0
    for row in usercomp:
        if row[1] == hostname:
            host_sum += 1
    full_table.append([hostname, host_sum])

full_table.sort(key=lambda row: row[1], reverse=True)
print_top10(full_table)
