'''
1. Создать новый проект ""Консольный файловый менеджер"
2. В проекте реализовать следующий функционал:
После запуска программы пользователь видит меню, состоящее из следующих пунктов:
- создать папку;
- удалить (файл/папку);
- копировать (файл/папку);
- просмотр содержимого рабочей директории;
- посмотреть только папки;
- посмотреть только файлы;
- просмотр информации об операционной системе;
- создатель программы;
- играть в викторину;
- мой банковский счет;
- смена рабочей директории (*необязательный пункт);
- выход.
'''
from myLib import *
import victory as v
import persAccount as pa

curDir = os.getcwd()   # текущий директорий


goMenu=True
while goMenu:
    nMenu = menu()

    if nMenu ==   1:
        newDir()
    elif nMenu == 2:
        delDir()
    elif nMenu == 3:
        copyFil()
    elif nMenu == 4:
        viewDir()
    elif nMenu == 5:
        viewOnlyDir()
    elif nMenu == 6:
        viewOnlyFil()
    elif nMenu == 7:
        infoOS()
    elif nMenu == 8:
        infoMy()
    elif nMenu == 9:
        c.goGame()
        print('------------------')
    elif nMenu == 10:
        pa.goGame()
        print('------------------')
    elif nMenu == 11:
        chDir()
        print('------------------')
    elif nMenu == 12:
        goMenu = False
    else:
        print( 'Ошибка выбора!\n-------------')