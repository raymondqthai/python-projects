# Slot Machine


# import modules
import random


# universal numbers
max_lines = 3
# user bet
max_bet = 100
min_bet = 1
# slot machine grid
rows = 3
cols = 3
# symbols dictionary and the chance of landing the symobol
symbol_count = {
    "A":5,
    "B":15,
    "C":30,
    "D":50
}
# points dictionary, the lower the chance the higher the points
symbol_value = {
    "A":400,
    "B":80,
    "C":16,
    "D":4
}


# analyze for wins
def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines): # loop through every line and check on bet on every line
        symbol = columns[0][line] # check first column of current row
        for column in columns: # loop through every column and check for symbol
            symbol_to_check = column[line] # check symbol at the column of the current row
            if symbol != symbol_to_check: # check if symbols are not the same
                break
        else:
            winnings += values[symbol]*bet # winnings point rarity of the symbol multiply by bet of each line
            winning_lines.append(line + 1)
    return winnings, winning_lines


# slot machine mechanics
def get_slot_machine_spin(rows, cols, symbols):
    # list
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    # storing the columns
    columns = [] # set column list
    for _ in range(cols): # generate a column for every column
        column = [] # set empty column list inside columns list
        current_symbols = all_symbols[:] # set generating symbols to a copy of all symbols # store the copy not the reference
        for _ in range(rows): # loop values need to generate equal to the numbers of rows 
            value = random.choice(current_symbols) # generate random symbols
            current_symbols.remove(value) # remove repeated symbols
            column.append(value) # insert random symbols to column 
        columns.append(column) # insert into columns list
    return columns


# printing transposing results
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end= " | ")
            else:
                print(column[row])


# user inputs deposit
def deposit(): 
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")
    return amount


# user input number of lines to bet
def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(max_lines) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= max_lines:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")
    return lines


# user input bet on each line
def get_bet(): 
    while True:
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if min_bet <= amount <= max_bet:
                break
            else:
                print(f"Amount must be between ${min_bet} - ${max_bet}.")
        else:
            print("Please enter a number.")
    return amount


# create a loop to continue betting on the game
def spin(balance):
    lines = get_number_of_lines()
    # balance check
    while True:
        bet = get_bet()
        total_bet = bet*lines
        if total_bet > balance:
            print(f"You do not have enough to bet that amount.\nYour current balance is ${balance}.")
        else:
            break
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")
    #print(balance, lines) # debug balance and lines
    slots = get_slot_machine_spin(rows, cols, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines:", *winning_lines) # using splat/unpack operator, it passes the variable
    return winnings - total_bet


def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play (q to quit).")
        if answer == "":
            pass
        elif answer == "q":
            break
        else:
            print("INCORRECT INPUT!")
            continue
        balance += spin(balance)
        if balance == 0:
            print("GAME OVER!")
            break
    print(f"You left with ${balance}")
main()
