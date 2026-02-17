# Text-Based Slot Machine

A slot machine game that runs in the terminal. Built with Python as a learning
project to practice functions, loops, dictionaries, and input validation.

---

## Features

- Deposit a starting balance before playing
- Choose how many lines to bet on (1 to 3)
- Set a bet amount per line between $1 and $100
- Spin the reels and win based on matching symbols
- Tracks balance across multiple spins
- Ends the game automatically when balance hits zero

---

## How to Run

1. Clone the repository
   git clone https://github.com/raymondqthai/python-projects.git
2. Navigate to the project folder
   cd python-projects/slot-machine
3. Run the script
   python slot_machine.py

No external libraries required. Uses Python's built-in random module.

---

## Usage

    $ python slot_machine.py

    What would you like to deposit? $100
    Current balance is $100

    Press enter to play (q to quit).
    Enter the number of lines to bet on (1-3)? 2
    What would you like to bet on each line? $10
    You are betting $10 on 2 lines. Total bet is equal to: $20

    D | B | D
    D | D | D
    C | A | B

    You won $80.
    You won on lines: 2
    Current balance is $160

---

## Symbols and Payouts

| Symbol | Frequency   | Multiplier |
|--------|-------------|------------|
| A      | Rare        | 400x       |
| B      | Uncommon    | 80x        |
| C      | Common      | 16x        |
| D      | Very Common | 4x         |

Rarer symbols pay more. Winnings equal the symbol multiplier times your bet per line.

---

## What I Learned

- How to use while loops to keep prompting until the user enters valid input
- How dictionaries store symbol frequencies and payout values
- How to separate logic into small, focused functions
- How the random module selects values without repetition using list removal
- How to transpose a column-based grid to display rows in the terminal

---

## Credits

Based on a tutorial by Tech With Tim
https://www.youtube.com/watch?v=th4OBktqK1I
