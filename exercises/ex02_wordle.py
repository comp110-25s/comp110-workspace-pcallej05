"""Wordle Exercise!"""

__author__: str = "730658315"


def main(secret_word: str) -> None:
    """The entrypoint of the program and main game loop."""
    maximum_turns = 6  # user is given 6 turns
    turn_count = 1  # game starts on first turn
    won = False  # states that intially, user has not won
    while (
        turn_count <= maximum_turns and not won
    ):  # loop runs until won or reached max turns
        print(
            f"=== Turn {turn_count}/{maximum_turns} ==="
        )  # prints current turn number
        guess_word = input_guess(
            len(secret_word)
        )  # use will be prompted for their guess
        result = emojified(guess_word, secret_word)
        print(result)  # prints emoji str since it was stored in result variable
        if guess_word == secret_word:
            won = True  # loop exits if guess_word matches secret_word
        else:
            turn_count += 1  # if incorrect, turn is incrimented and user tries again
    if won:
        print(
            f"You won in {turn_count}/{maximum_turns} turns!"
        )  # message printed if won
    else:
        print(
            f"x/{maximum_turns} - Sorry, try again tomorrow!"
        )  # message printed if player runs out of turns


def contains_char(guess_word: str, single_char: str) -> bool:
    """Checks if the single character is found at an index of guess_word"""
    assert (
        len(single_char) == 1
    ), f"len('{single_char}') is not 1"  # Error is raised if one char isn't entered
    idx = 0  # first idx of guess_word starts at 0
    while idx < len(guess_word):  # iterates throuhg each character in guess_word
        if guess_word[idx] == single_char:
            return True  # single_char is found in guess_word
        idx += 1  # if no match found, next letter is checked
    return False  # single_char is not found in guess_word


def emojified(guess_word: str, secret_word: str) -> str:
    """Returns str of emojis based on how the letters in guess match secret"""
    assert len(guess_word) == len(secret_word), "Guess must be same length as secret"
    WHITE_BOX: str = "\U00002B1C"  # The letter is not in the secret word
    GREEN_BOX: str = "\U0001F7E9"  # The letter is in the correct position
    YELLOW_BOX: str = "\U0001F7E8"  # The letter is in the wrong position
    idx = 0  # This variable is stored and value starts as 0
    result = ""  # This variable will store the final emoji result
    while idx < len(guess_word):  # loop continues until all letters checked
        if guess_word[idx] == secret_word[idx]:
            result += GREEN_BOX
        elif contains_char(secret_word, guess_word[idx]):
            result += YELLOW_BOX
        else:
            result += WHITE_BOX
        idx += 1  # loop will check next letter
    return result  # after looping all letters, emoji str returned


def input_guess(expected_length: int) -> str:
    """Ensures user provides a guess of expected length"""
    guess_word = input(
        f"Enter a {expected_length} character word: "
    )  # variable holds users input as str
    while (
        len(guess_word) != expected_length
    ):  # if length is not what is expected, user gets prompted again
        guess_word = input(f"That wasn't {expected_length} chars! Try again: ")
    return guess_word  # loop exits when user provides correctly sized word


if __name__ == "__main__":
    main(secret_word="codes")
