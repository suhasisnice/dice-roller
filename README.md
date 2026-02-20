Dice Roll Simulator

Description
-----------
A simple Python command-line program that simulates rolling two dice.
The program generates a random tuple representing the values of two dice (1–6).
Users can repeatedly roll the dice until they choose to exit.

Features
--------
- Generates two random dice values using Python's random module
- Case-insensitive input handling (Y/y to roll, N/n to exit)
- Input validation for incorrect entries
- Continuous loop until user chooses to quit

How It Works
------------
- The program uses random.randint(1, 6) to simulate each die.
- A tuple is returned containing two values.
- The user is prompted to:
    y → Roll the dice
    n → Exit the program
    Any other input → Invalid choice message

Requirements
------------
- Python 3.x
- No external libraries required

How to Run
----------
1. Save the file as dice.py
2. Open terminal in the project directory
3. Run:
   python dice.py

Example Output
--------------
Do you want to roll a pair of die : y to agree or n to exit : y
(3, 6)

Do you want to roll a pair of die : y to agree or n to exit : n
Exiting....

Concepts Practiced
------------------
- Functions
- While loops
- Conditional statements
- User input handling
- Random number generation
- Tuples

Possible Improvements
---------------------
- Add ASCII dice visuals
- Track roll history
- Add statistics (average roll, frequency distribution)
- Convert into a simple terminal-based game
