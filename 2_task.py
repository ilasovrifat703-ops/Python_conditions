num_year = int(input('ВВедите номер года: '))

cycle_index = (num_year-1996)%12

match cycle_index:
    case 0:
        print('Год крысы')
    case 1:
        print('Год коровы')
    case 2:
        print('Год тигра')
    case 3:
        print('Год зайца')
    case 4:
        print('Год дракона')
    case 5:
        print('Год змеи')
    case 6:
        print('Год лошади')
    case 7:
        print('Год овцы')
    case 8:
        print('Год обезбяны')
    case 9:
        print('Год петуха')
    case 10:
        print('Год собаки')
    case 11:
        print('Год свиньи')