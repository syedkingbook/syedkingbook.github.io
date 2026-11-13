import random

LOWER_BOUND = 1
UPPER_BOUND = 100
ATTEMPT_LIMIT = 10

INVALID = "INVALID"
CORRECT = "CORRECT"
TOO_HIGH = "TOO_HIGH"
TOO_LOW = "TOO_LOW"


def parse_guess(raw_text):
    guessed_number = raw_text.strip()
    if not guessed_number:
        return INVALID


    try:
        number = float(guessed_number)
    except ValueError:
        return INVALID

    if not number.is_integer():
        return INVALID

    guessed_number = int(number)
    if not LOWER_BOUND <= guessed_number <= UPPER_BOUND:
        return INVALID
    return guessed_number


def compare_guess(guess, secret):
    if guess == secret:
        return CORRECT
    if guess > secret:
        return TOO_HIGH
    return TOO_LOW


def play_game():
    secret = random.randint(LOWER_BOUND, UPPER_BOUND)
    attempts_used = 0
    won = False

    while attempts_used < ATTEMPT_LIMIT and not won:
        raw_text = input(f"Guess a number from {LOWER_BOUND} to {UPPER_BOUND}: ")
        attempts_used += 1
        guess = parse_guess(raw_text)

        if guess == INVALID:
            print(
                f"Enter a whole number from {LOWER_BOUND} to {UPPER_BOUND}. "
                "That attempt was used."
            )
            continue

        outcome = compare_guess(guess, secret)
        if outcome == CORRECT:
            print(f"You guessed it in {attempts_used} attempts!")
            won = True
        else:
            print("Too high." if outcome == TOO_HIGH else "Too low.")
            print(f"Attempts remaining: {ATTEMPT_LIMIT - attempts_used}")

    if not won:
        print(f"Game over. The number was {secret}.")


if __name__ == "__main__":
    try:
        play_game()
    except (KeyboardInterrupt, EOFError):
        print("\nGoodbye!")
