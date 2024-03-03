import random
player = 0
bot = 0
list = ['к', 'н', 'б']
while True:
    choice = input("Играть(да, нет): ")
    if (choice == "нет"):
        break
    choice = input("Выбери (к, н, б): ")
    bot_choice = list[random.randint(0, 2)]
    if (choice == 'к'):
        if (bot_choice == 'к'):
            print("Выбор бота: " + bot_choice)
            print("Выбор игрока: " + choice)
            print("Ничья")
        elif (bot_choice == 'н'):
            print("Выбор бота: " + bot_choice)
            print("Выбор игрока: " + choice)
            print("Выигрыш")
            player += 1
        elif (bot_choice == 'б'):
            print("Выбор бота: " + bot_choice)
            print("Выбор игрока: " + choice)
            print("Проигрыш")
            bot += 1
    if (choice == 'н'):
        if (bot_choice == 'н'):
            print("Выбор бота: " + bot_choice)
            print("Выбор игрока: " + choice)
            print("Ничья")
        elif (bot_choice == 'б'):
            print("Выбор бота: " + bot_choice)
            print("Выбор игрока: " + choice)
            print("Выигрыш")
            player += 1
        elif (bot_choice == 'к'):
            print("Выбор бота: " + bot_choice)
            print("Выбор игрока: " + choice)
            print("Проигрыш")
            bot += 1
    if (choice == 'б'):
        if (bot_choice == 'б'):
            print("Выбор бота: " + bot_choice)
            print("Выбор игрока: " + choice)
            print("Ничья")
        elif (bot_choice == 'к'):
            print("Выбор бота: " + bot_choice)
            print("Выбор игрока: " + choice)
            print("Выигрыш")
            player += 1
        elif (bot_choice == 'н'):
            print("Выбор бота: " + bot_choice)
            print("Выбор игрока: " + choice)
            print("Проигрыш")
            bot += 1
print("Очки игрока:", player)
print("Очки бота:", bot)
