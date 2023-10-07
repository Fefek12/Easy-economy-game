import random
from time import sleep
import os

wallet = 1
bank = 0
all_money = 0
backpack = []

crime_controler = 0
work_controler = 0

save_file_name = "game_save.py"

def save_game():
    global wallet, bank, backpack, crime_controler, work_controler

    game_state = {
        "wallet": wallet,
        "bank": bank,
        "crime_controler": crime_controler,
        "work_controler": work_controler,
        "backpack": backpack,
    }

    with open(save_file_name, "w") as save_file:
        save_file.write(str(game_state))
        print("Game saved.")
    question()

def load_game():
    global wallet, bank, backpack, crime_controler, work_controler
    try:
        with open(save_file_name, "r") as save_file:
            game_state = eval(save_file.read())
            wallet = game_state["wallet"]
            bank = game_state["bank"]
            work_controler = game_state["work_controler"]
            crime_controler = game_state["crime_controler"]
            backpack = game_state["backpack"]
        print("Game loaded.")
    except FileNotFoundError:
        print("No save file found.")
    question()

#shop commands
pc1 = 3000
pc2 = 5000
pc3 = 6700
pc4 = 10500
pc5 = 13000
pc6 = 16000

def work():
    global wallet
    global work_controler

    work_controler = work_controler + 1

    earned = random.randint(100, 250)
    wallet = wallet + earned

    print("You erned " + str(earned) + " from working")

    question()

def bal():
    print('Wallet: '+ str(wallet))
    print("Bank: " + str(bank))
    all_money = wallet + bank
    print('All money: ' + str(all_money))

    question()

def crime():
    global wallet
    global crime_controler

    chance = random.randint(0, 1)
    erned = random.randint(350, 1500)

    crime_controler = crime_controler + 1
    if chance == 0:
        wallet = wallet + erned

        print("You erned " + str(erned) + " from criming")

        question()
    elif chance == 1:
        wallet = wallet - erned

        print("You lost " + str(erned) + " from criming")

        question()


def shop():
    print("Shop")
    print("PC 1980s - 3000 [tag: pc1]")
    print("PC 1995s - 5000 [tag: pc2]")
    print("PC 2000s - 6700 [tag: pc3]")
    print("PC 2010s - 10500 [tag: pc4]")
    print("PC 2015s - 13000 [tag: pc5]")
    print("PC 2020s - 16000 [tag: pc6]")
    print(" ")
    print("To buy something write 'buy'")

    question()

def buy():
    global wallet
    item = input("buy-command # ")

    if item == "pc1":
      if wallet >= 3000:
          wallet = wallet - 3000
          backpack.append("PC 1980s")
      else:
            print("You do not have enought money")
    elif item == "pc2":
      if wallet >= 5000:
        wallet = wallet - 5000
        backpack.append("PC 1995s")
    elif item == "pc3":
      if wallet >= 6700:
        wallet = wallet - 6700
        backpack.append("PC 2000s")
      else:
            print("You do not have enought money")
    elif item == 'pc4':
      if wallet >= 10500:
        wallet = wallet - 10500
        backpack.append("PC 2010s")
      else:
            print("You do not have enought money")
    elif item == 'pc5':
      if wallet >= 13000:
        wallet = wallet - 13000
        backpack.append("PC 2015s")
    elif item == 'pc6':
      if wallet >= 16000:
        wallet = wallet - 16000
        backpack.append("PC 2020s")

    question()

def showbg():
  print(backpack)

  question()

def dep():
  global bank
  global wallet

  money = int(input("dep-command # "))


  wallet = wallet - money
  bank = bank + money

  question()

def withdraw():
  global wallet
  global bank

  cost = int(input('withdraw-command # '))


  bank = bank - cost
  wallet = wallet + cost

  question()

def roulette():
  global wallet
  strike = 2

  cost = int(input("roulette1-command # "))
  color = input("roulette-command # ")

  if cost <= wallet:
    choice = random.randint(0,1)

    if color == 'red':
      strike = 0
    elif color == 'black':
      strike = 1

    if choice == strike:
      wallet = wallet + (cost *  2)
      earned = (cost * 2)

      print("You erned " + str(earned))

      question()
    elif choice != strike:
      wallet = wallet - (cost * 2)
      earned = (cost * 2)

      print("You lost " + str(earned))

      question()
  else:
    print("You do not have enought money")
    question()

def help():
   print("Command list")
   print("work")
   print("crime")
   print("roulette [WARNING: first type cost then type color!]")
   print("dep")
   print('withdraw')
   print('bal')
   print('help')
   print('shop')
   print('buy')
   print('showb')
   print('clear')
   print("save")

   print(' ')

   question()

def save():
    data = open('Data.py', 'w')
    data.write('wallet = ' + str(wallet) + '\n')
    data.write('bank = ' + str(bank) + '\n')

    data.close

    question()

def question():
    global work_controler
    global crime_controler
    command = input("question-command # ")

    if command == "work":
      if work_controler > 0:
        print("Wait 10 seconds")
        sleep(10)
        work()
      else:
        work()
    elif command == "bal":
        bal()
    elif command == "crime":
      if crime_controler > 0:
        print("Wait 30 seconds")
        sleep(30)
        crime()
      else:
        crime()
    elif command == 'shop':
        shop()
    elif command == 'buy':
      buy()
    elif command == 'showb':
      showbg()
    elif command == 'dep':
      dep()
    elif command == 'withdraw':
      withdraw()
    elif command == 'roulette':
      roulette()
    elif command == 'clear':
       os.system('cls')
    elif command == 'help':
       help()
    elif command == 'save':
       save_game()
    elif command == 'load':
      load_game()
    else:
       print('This command does not exist')
       question()

load_game()
question()