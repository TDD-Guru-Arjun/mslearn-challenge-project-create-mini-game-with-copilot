import unittest
from unittest.mock import patch

from app import compare_choices, play_game, player_score, computer_score


class TestCompareChoices(unittest.TestCase):
    def setUp(self) -> None:
        self.player_choice = None
        self.computer_choice = None
        self.player_score = 0
        self.computer_score = 0
        self.game_status = None

    def assertResult(self, game_status, player_score, computer_score) -> None:
        """Test Assertion Helper Util method to assert the result of the game"""
        self.assertEqual(self.game_status, game_status)
        self.assertEqual(self.player_score, player_score)
        self.assertEqual(self.computer_score, computer_score)

    def test_tie_with_rock(self) -> None:
        # Arrange / Given
        self.player_choice = "rock"
        self.computer_choice = "rock"

        # Act / When
        self.game_status, self.player_score, self.computer_score =  compare_choices(
            player_choice=self.player_choice,
            computer_choice=self.computer_choice,
            player_score=self.player_score,
            computer_score=self.computer_score,
        )

        # Assert / Then
        self.assertResult("tie", 0, 0)

    def test_rock_vs_paper(self) -> None:
        # Arrange / Given
        self.player_choice = "rock"
        self.computer_choice = "paper"

        # Act / When
        self.game_status, self.player_score, self.computer_score =  compare_choices(
            player_choice=self.player_choice,
            computer_choice=self.computer_choice,
            player_score=self.player_score,
            computer_score=self.computer_score,
        )

        # Assert / Then
        self.assertResult("lose", 0, 1)

    def test_rock_vs_scissors(self) -> None:
        # Arrange / Given
        self.player_choice = "rock"
        self.computer_choice = "scissors"

        # Act / When
        self.game_status, self.player_score, self.computer_score =  compare_choices(
            player_choice=self.player_choice,
            computer_choice=self.computer_choice,
            player_score=self.player_score,
            computer_score=self.computer_score,
        )

        # Assert / Then
        self.assertResult("win", 1, 0)

    def test_paper_vs_rock(self) -> None:
        # Arrange / Given
        self.player_choice = "paper"
        self.computer_choice = "rock"

        # Act / When
        self.game_status, self.player_score, self.computer_score =  compare_choices(
            player_choice=self.player_choice,
            computer_choice=self.computer_choice,
            player_score=self.player_score,
            computer_score=self.computer_score,
        )

        # Assert / Then
        self.assertResult("win", 1, 0)

    def test_tie_with_paper(self) -> None:
        # Arrange / Given
        self.player_choice = "paper"
        self.computer_choice = "paper"

        # Act / When
        self.game_status, self.player_score, self.computer_score =  compare_choices(
            player_choice=self.player_choice,
            computer_choice=self.computer_choice,
            player_score=self.player_score,
            computer_score=self.computer_score,
        )

        # Assert / Then
        self.assertResult("tie", 0, 0)

    def test_paper_vs_scissors(self) -> None:
        # Arrange / Given
        self.player_choice = "paper"
        self.computer_choice = "scissors"

        # Act / When
        self.game_status, self.player_score, self.computer_score =  compare_choices(
            player_choice=self.player_choice,
            computer_choice=self.computer_choice,
            player_score=self.player_score,
            computer_score=self.computer_score,
        )

        # Assert / Then
        self.assertResult("lose", 0, 1)

    def test_scissors_vs_rock(self) -> None:
        # Arrange / Given
        self.player_choice = "scissors"
        self.computer_choice = "rock"

        # Act / When
        self.game_status, self.player_score, self.computer_score =  compare_choices(
            player_choice=self.player_choice,
            computer_choice=self.computer_choice,
            player_score=self.player_score,
            computer_score=self.computer_score,
        )

        # Assert / Then
        self.assertResult("lose", 0, 1)

    def test_scissors_vs_paper(self) -> None:
        # Arrange / Given
        self.player_choice = "scissors"
        self.computer_choice = "paper"

        # Act / When
        self.game_status, self.player_score, self.computer_score =  compare_choices(
            player_choice=self.player_choice,
            computer_choice=self.computer_choice,
            player_score=self.player_score,
            computer_score=self.computer_score,
        )

        # Assert / Then
        self.assertResult("win", 1, 0)

    def test_tie_with_scissors(self) -> None:
        # Arrange / Given
        self.player_choice = "scissors"
        self.computer_choice = "scissors"

        # Act / When
        self.game_status, self.player_score, self.computer_score =  compare_choices(
            player_choice=self.player_choice,
            computer_choice=self.computer_choice,
            player_score=self.player_score,
            computer_score=self.computer_score,
        )

        # Assert / Then
        self.assertResult("tie", 0, 0)


if __name__ == "__main__":
    unittest.main()