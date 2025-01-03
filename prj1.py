import random
MAX_LINES=3
MAX_BET=100
MIN_BET=1
ROWS=3
COLS=3
symbol_count={
    "A":2,
    "B":4,
    "C":6,
    "D":8
}
symbol_values={
    "A":5,
    "B":4,
    "C":3,
    "D":2
}
def check_winnings(columns,lines,bet,values):
    winnings = 0
    winnings_lines=[]
    for line in range(lines):
        symbol=columns[0][line]
        for column in columns:
            symbol_to_check=column[line]
            if symbol!=symbol_to_check:
                break
        else:
            winnings+=values[symbol]*bet
            winnings_lines.append(line+1)
    return winnings,winnings_lines

def get_slot_machine_spin(rows,columns,symbols):
    all_symbols=[]
    for symbol,symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    columns = []
    for _ in range(COLS):
        column=[]
        current_symbols=all_symbols[:]
        for _ in range(rows):
            value = random.choice(all_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns 
def print_slot_machine(columns):
    for row in range(len(columns[0])):
            for i,column in enumerate(columns):
                if i!=len(columns)-1:
                    print(column[row],end=" | ")
                else:
                    print(column[row],end="")
            print()
def deposit():
    while True:
        amount=input("what would you like to deposit?")
        if amount.isdigit():
            amount = int(amount)
            if amount>0:
                break
            else:
                print("amount must be greater than   zero")

        else:
            print("please enter a number.")
    return amount

def get_number_of_lines():
    while True:
        lines=input("enter the number of lines (1-" + str(MAX_LINES)+") ")
        if lines.isdigit():
            lines = int(lines)
            if 1<=lines<=MAX_LINES:
                break
            else:
                print("enter a valid numebr of lines")

        else:
            print("please enter a number.")
    return lines
def get_bet():
    while True:
        bet=input("what would you like to bet?")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET<=bet<=MAX_BET:
                break
            else:
                print(f"amount must be between ${MIN_BET}-${MAX_BET}.")

        else:
            print("please enter a number.")
    return bet
def spin(balance):
    Lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet= bet*Lines
        if total_bet>balance:
            print("you do not have enough to bet on that amount,your current balance is ${balance}")
        else:
            break

    print(f"you are bettig ${bet} on {Lines} lines.total bet is ${total_bet}  ")
    slots = get_slot_machine_spin(ROWS,COLS,symbol_count)
    print_slot_machine(slots)
    winnings,winning_lines=check_winnings(slots,Lines,bet,symbol_values)
    print(f"you won ${winnings} .")
    print(f"you won on lines:",*winning_lines)
    return winnings-total_bet

def main():
    balance =deposit() 
    while True:
        print(f"current balance is ${balance}")
        answer=input("press enter the play(q to quit).")
        if answer=="q":
            break
        balance+=spin(balance)
    print(f"you left with ${balance}")
    
        
main()


        
