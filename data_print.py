def data_print(line):
    with open('phone.csv', 'r') as file:
        print('ФИО'.center(20),'Имя'.center(20),'Тел'.center(15))
        for line in file:
            print (line)