# Задание№3 Сформировать из введенного числа обратное по порядку введенного в него цифр и вывести на экран.
# Например, если введено число 3486, то надо вывести число 6843.

def  зеркало ():
    inp  =  input ( 'Введите многозначное число \ n ' )
    print ( f'Отзеркаленое число { inp [:: - 1 ] } ' )


зеркало ()