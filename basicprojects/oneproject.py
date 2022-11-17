import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1


ROWS = 3
COLS = 3

symbol_count = {
    "A" : 2,
    "B" : 4,
    "C" : 6,
    "D" : 8
}

def slot_machine_spin(rows,cols,symbols):
    all_symbols = []
    for symbol,symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        
        columns.append(column)

    return columns


'''-------------Validating amount ------------'''

def deposit():
    while True:
        amount = input("please enter amount you want to deposit?: ")
        
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("please enter amount greater than 0. ")
        else:
            print("please enter a number.")

    return amount


'''--------------Validating lines----------------'''
def get_lines():
    while True:
        lines = input("please enter number of lines to bet  on (1-" + str(MAX_LINES) +  ")? ")

        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("please enter a valid number.")

    return lines

'''---------------Validating bet-------------------'''
def get_bet():
    while True:
        bet = input("what amount you want to bet?: ")
        
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"please enter amount between {MIN_BET} - {MAX_BET}")
        
        else:
            print("please enter valid number.")

    return bet

def oneproject():
    
    balance = deposit()

    lines = get_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enough balance to bet, your current amount is {balance}")
        else:
            break
        
    if lines == 1:
        print(f"You are betting {bet} on {lines} line. Total bet is equal to: {total_bet}")
    else:
        print(f"You are betting {bet} on {lines} lines. Total bet is equal to: {total_bet}")

oneproject()
