# 1 открыть файл
# 2 сохранить файл
# 3 показать контакты
# 4 добавить контакт
# 5 найти контакт
# 6 изменить контакт
# 7 удалить контакт
# 8 выход
dict = {1: ['венг', 'вне', 'fkdhj'], 2: ['взн', 'хещ'], 3: ['кхщнш', 'ркоык'], 4: ['хкзш', 'пыокр'], 5: ['хкер', 'ерое'], 6: ['хф0к', 'роехр']}

def open_file():
    with open('text.txt', 'r', encoding="UTF-8") as data:
        directory = data.readlines()
    handbk = {}
    for i in directory:
        i = i.rstrip()
        direct = i.split(';')
        handbk[int(direct[0])] = [direct[j] for j in range(1, len(direct))]
    # print(handbk)
    return handbk
# open_file()


def save_file(directory):
    direct = ''
    for key, value in directory.items():
        direct += F" {key};{';'.join(str(num) for num in value)} \n"
    with open('text.txt', 'w', encoding="UTF-8") as data:
        data.write(str(direct))
# save_file(dict)

def add_contact(directory):
    data = []
    data.append(input('введите имя'))
    data.append(input('введите телефон'))
    data.append(input('введите комментарий'))
    directory[1 + len(list(directory.keys()))] = data
    # print(directory)
# add_contact(dict)

def print_contacts(directory):
    print('начало')
    for key, value in directory.items():
        print(key, ': ', '; '.join(str(num) for num in value), sep='')
    print('конец')
# print_contacts(dict)





while True:
    action = int(input(' 1 открыть файл \n 2 сохранить файл \n 3 показать контакты \n 4 добавить контакт \n 5 найти контакт \n 6 изменить контакт \n 7 удалить контакт \n 8 выход \n выберите действие: '))
    if action == 1:
        dictionary = open_file()
        print('файл открыт')
    elif action == 2:
        save_file(dictionary)
        print('файл сохранен')
    elif action == 3:
        print_contacts(dictionary)
    elif action == 4:
        add_contact(dictionary)
        print('контакт добавлен')
    elif action == 5:
        break
    elif action == 6:
        break
    elif action == 7:
        break
    else:
        break







