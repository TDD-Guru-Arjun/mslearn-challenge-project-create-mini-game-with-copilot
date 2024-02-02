"""
goal is to develop the logic of the Python mini-game with the help of GitHub Copilot based in the specifications bellow.

Specification
As we learned in the introduction to this challenge, the winner of the game is determined by three simple rules:

Rock beats scissors.
Scissors beat paper.
Paper beats rock.
What you should consider in the game interactions
Let's add some more excitement to this challenge and make the game multiplayer, where the computer will be your opponent and can randomly choose one of the elements (rock, paper, or scissors) for each move, just like you. Your interaction in the game will be through the console (Terminal).

The player can choose one of the three options rock, paper, or scissors and should be warned if they enter an invalid option.
At each round, the player must enter one of the options in the list and be informed if they won, lost, or tied with the opponent.
By the end of each round, the player can choose whether to play again.
Display the player's score at the end of the game.
The minigame must handle user inputs, putting them in lowercase and informing the user if the option is invalid.
"""

# The game will be developed in the app.py file

# First, we need to import the random module to generate the computer"s choice
import random
from typing import Literal

# Then, we need to create a list with the options
options: list[str] = ["rock", "paper", "scissors"]

# Now, we need to create variables to store the player"s and computer"s scores
player_score, computer_score = 0, 0


# Now, we need to create a function to get the player"s choice
def get_player_choice() -> None:
    """
    Prompts the player to choose between rock, paper, or scissors, and returns the player's choice.

    Args:
        None

    Returns:
        str: The choice made by the player.
    """
    player_choice: str = input("Choose between rock, paper or scissors: ").lower()
    if player_choice not in options:
        print("Invalid option. Please, try again.")
        get_player_choice()
    return player_choice


# Now, we need to create a function to get the computer"s choice
def get_computer_choice() -> None:
    """
    Generates a random choice for the computer.

    Args:
        None

    Returns:
        str: The randomly generated choice for the computer.
    """
    computer_choice: str = random.choice(options)
    return computer_choice


# Now, we need to create a function to compare the choices and determine the winner
def compare_choices(
    player_choice: str,
    computer_choice: str,
    player_score: int,
    computer_score: int,
) -> None:
    """
    Compares the choices made by the player and the computer, and updates the scores accordingly.

    Args:
        player_choice (str): The choice made by the player.
        computer_choice (str): The choice made by the computer.
        player_score (int): The current score of the player.
        computer_score (int): The current score of the computer.

    Returns:
        Tuple[str, int, int]: A tuple containing the game status ("tie", "win", or "lose"),
        the updated player score, and the updated computer score.
    """
    game_status: Literal[""] = ""

    if player_choice == computer_choice:
        game_status = "tie"
    elif player_choice == "rock":
        if computer_choice == "paper":
            game_status = "lose"
            computer_score += 1
        else:
            game_status = "win"
            player_score += 1
    elif player_choice == "paper":
        if computer_choice == "scissors":
            game_status = "lose"
            computer_score += 1
        else:
            game_status = "win"
            player_score += 1
    elif player_choice == "scissors":
        if computer_choice == "rock":
            game_status = "lose"
            computer_score += 1
        else:
            game_status = "win"
            player_score += 1

    return game_status, player_score, computer_score


# Now, we need to create a function to display the results
def display_results(player_choice: str, computer_choice: str, game_status: str) -> None:
    """
    Prints the player's choice, the computer's choice, and the result of the game.

    Args:
        player_choice (str): The choice made by the player.
        computer_choice (str): The choice made by the computer.
        game_status (str): The result of the game. Possible values are "tie", "win", or "lost".

    Returns:
        None
    """
    print(f"You chose {player_choice} and the computer chose {computer_choice}.")
    if game_status == "tie":
        print("It's a tie.")
    elif game_status == "win":
        print("You won!")
    else:
        print("You lost.")

# Now, we need to create a function to display the scores
def display_scores() -> None:
    """
    Prints the scores of the player and the computer.

    Args:
        None

    Returns:
        None
    """
    print(f"You scored {player_score} points and the computer scored {computer_score} points.")

def good_bye() -> None:
    """
    Prints a farewell message to the player.

    Args:
        None

    Returns:
        None
    """
    print("Thanks for playing. Good Bye!")

# Now, we need to create a function to ask the player if they want to play again
def play_again() -> None:
    """
    Prompts the player to choose whether to play again or not.
    If the player chooses to play again, the game is restarted.
    If the player chooses not to play again, the scores are displayed and a farewell message is printed.

    Args:
        None

    Returns:
        None
    """
    player_choice: str = input("Do you want to play again? (y/n) ").lower()
    if player_choice == "y":
        play_game()
    elif player_choice == "n":
        display_scores()
        good_bye()
    else:
        print("Invalid option. Please, try again.")
        play_again()

# Now, we need to create a function to play the game
def play_game() -> None:
    """
    Plays a round of the game.
    Gets the player's choice and the computer's choice, compares them, and updates the scores.
    Displays the results of the round and prompts the player to play again.

    Args:
        None

    Returns:
        None
    """
    global player_score, computer_score
    player_choice : str = get_player_choice()
    computer_choice: str = get_computer_choice()

    game_status, player_score, computer_score = compare_choices(
        player_choice=player_choice,
        computer_choice=computer_choice,
        player_score=player_score,
        computer_score=computer_score,
    )
    display_results(player_choice, computer_choice, game_status)
    play_again()


# Now, we need to call the play_game function
if __name__ == "__main__":
    play_game()
