"""Number Quest - a CLI number-guessing game with increasing difficulty.

Guess the secret number before you run out of attempts. Every round you win
raises the level: the range gets bigger and the attempts get fewer.
Run: python main.py
"""

import random
import re
from typing import Callable, Optional, Tuple

CORRECT, TOO_LOW, TOO_HIGH = "correct", "low", "high"


def round_settings(level: int) -> Tuple[int, int, int]:
    """Return (low, high, attempts) for the given level."""
    low, high = 1, 10 + level * 5
    attempts = max(3, 8 - level // 2)
    return low, high, attempts


def parse_guess(raw: str, low: int, high: int) -> int:
    """Convert raw input to an int inside [low, high], or raise ValueError."""
    if not re.fullmatch(r"[0-9]+", raw):
        raise ValueError("Please enter a valid number.")
    guess = int(raw)
    if guess < low or guess > high:
        raise ValueError(f"Out of range! Choose between {low} and {high}.")
    return guess


def evaluate_guess(guess: int, secret: int) -> str:
    if guess == secret:
        return CORRECT
    return TOO_LOW if guess < secret else TOO_HIGH


def play_round(
    level: int,
    rng=random,
    input_fn: Callable[[str], str] = input,
    output: Callable[[str], None] = print,
) -> Optional[bool]:
    """Play one round. Returns True (won), False (lost) or None (player quit)."""
    low, high, attempts = round_settings(level)
    secret = rng.randint(low, high)

    output(f"--- Round {level} ---")
    output(f"Range: {low} to {high}")
    output(f"Attempts: {attempts}")

    while attempts > 0:
        raw = input_fn("Enter your guess (or type 'q' to quit): ").strip()

        if raw.lower() == "q":
            return None

        try:
            guess = parse_guess(raw, low, high)
        except ValueError as exc:
            output(str(exc))  # invalid input does not cost an attempt
            continue

        result = evaluate_guess(guess, secret)
        if result == CORRECT:
            output("✅ Correct! You win this round!")
            return True

        attempts -= 1
        if result == TOO_LOW:
            output(f"⬆️ Too low! Attempts left: {attempts}")
        else:
            output(f"⬇️ Too high! Attempts left: {attempts}")

    output(f"\n❌ Game over! The number was {secret}.")
    return False


def run_game(
    rng=random,
    input_fn: Callable[[str], str] = input,
    output: Callable[[str], None] = print,
) -> None:
    output("🎮 Welcome to Number Quest!")
    output("Guess the secret number. You have limited attempts per round.\n")

    level = 1
    while True:
        result = play_round(level, rng, input_fn, output)
        if result is None:
            output("\nThanks for playing! 👋")
            return
        if result:
            level += 1
        else:
            output("Starting a new game from level 1.\n")
            level = 1


def main() -> None:
    try:
        run_game()
    except (KeyboardInterrupt, EOFError):
        print("\n\nThanks for playing! 👋")


if __name__ == "__main__":
    main()
