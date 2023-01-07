def find():
    param = input('\nИщем абонента по Фамилии\n')
    with open('phone.csv', 'r') as file:
        for line in file:
            if param in line:
                print (line)