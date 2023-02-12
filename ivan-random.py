from random import randint

game = True
num = randint(1,100)
file = open('game_result', 'w', encoding="utf8")

print('Попробуй угадай число от 1 до 100')
file.write('Попробуй угадай число от 1 до 100\n')
while game:
    guess = int(input('Ваше предположение:'))
    file.write(f'Ваше предположение: {guess}\n')
    if guess == num:
        print('Вы угaдали!')
        file.write('Вы угaдали!\n')
        game = False
    elif guess < num:
        print('Вы не угадали, попробуйте число побольше')
        file.write('Вы не угадали, попробуйте число побольше\n')
    else:
        print('Вы не угадали, попробуйте число поменьше')
        file.write('Вы не угадали, попробуйте число поменьше\n')
file.close()
