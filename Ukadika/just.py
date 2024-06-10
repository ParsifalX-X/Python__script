from random import *
print('Добро пожаловать в числовую угадайку')
number = randint(1, 100)
flag = True
def is_valid(user_number):
    if user_number.isdigit():
        if 1 <= int(user_number) <= 100:
            return True
    else:
        return False

def ukadika_cycle(flag):
    user_number = input('Введите число от 1 до 100: ')
    cnt_user_number = 0
    while flag:
        if is_valid(user_number):
            user_number = int(user_number)
            cnt_user_number += 1
            if user_number > number:
                print('Ваше число больше загаданного, попробуйте еще разок: ', end='')
                user_number = input()
                continue
            elif user_number < number:
                print('Ваше число меньше загаданного, попробуйте еще разок: ', end='')
                user_number = input()
                continue
            else:
                print('Вы угадали, поздравляем!',f"ИТОГО - вам бонадобилось {cnt_user_number} попыток ", sep='\n')
                flag = False
                break
        else:
            user_number = input('А может быть все-таки введем целое число от 1 до 100? ')
            
flag__ukadika = True
while flag__ukadika:
    ukadika_cycle(flag)
    yes_or_no = input('Если хотите повторить то напишите ( да/д ), а если нет то ( нет/н ): ').lower()

    if yes_or_no == 'да' or yes_or_no == 'д':
        number = randint(1, 100)
        flag = True
    elif yes_or_no == 'нет' or yes_or_no == 'н':
        flag__ukadika = False
        flag = False
        print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
    else:
        flag = False
        while flag == False:
            yes_or_no = input('Пожалуйста введите (да/д) или (нет/н): ')
            if yes_or_no == 'да' or yes_or_no == 'д':
                number = randint(1, 100)
                flag = True
            elif yes_or_no == 'нет' or yes_or_no == 'н':
                flag__ukadika = False
                flag = False
                print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
                break