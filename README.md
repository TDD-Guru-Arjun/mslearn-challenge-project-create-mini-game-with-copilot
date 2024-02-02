# Challenge project - Build a minigame console app with GitHub Copilot

Starter and Final code for the Challenge project: "Challenge project - Build a minigame console app with GitHub Copilot". To check the solution, change the branch to **Solution**.

## Usage

To run the app

```bash
python app.py
```

Demo

```bash
# Example game flow:
"""
Round 1
Choose between rock, paper or scissors: rock
You chose rock and the computer chose paper.
You lost.
Do you want to play again? (y/n) y
Round 2
Choose between rock, paper or scissors: paper
You chose paper and the computer chose rock.
You won!
Do you want to play again? (y/n) y
Round 3
Choose between rock, paper or scissors: scissors
You chose scissors and the computer chose scissors.
It's a tie.
Do you want to play again? (y/n) y
Round 4
Choose between rock, paper or scissors: rock
You chose rock and the computer chose paper.
You lost.
Do you want to play again? (y/n) n
You scored 1 points and the computer scored 2 points in total rounds=4.
Thanks for playing. Good Bye!
"""
```

To run unit tests

```bash
python -m unittest discover -s . -v
```

You can pass the following arguments to the pyunitx command:

```bash
-s or --start-directory: Specify the directory to start test discovery (default is '.').
-p or --pattern: Specify the test file pattern (default is 'test*.py').
-v or --verbosity: Specify the verbosity level (default is 1).
For more options and details, use the python -m unittest --help.
```
