---
layout: default
title: "Number Guessing Game"
---

# Number Guessing Game

How the Number Guessing Game Works

The program starts by picking a secret whole number between 1 and 100. The player then gets ten attempts to find it. On each turn, the game reads the player’s text, trims extra spaces, and checks that it is a whole number within range. Invalid input is rejected but still costs an attempt. Valid guesses are compared with the secret, and the game replies “too high” or “too low.” A correct guess ends the game with the number of attempts used. If all ten attempts pass without success, the game reveals the secret. Pressing Ctrl+C or Ctrl+D exits cleanly anytime.

This describes the design from the corrected pseudocode, so it matches the choices we made: invalid input costs an attempt, the secret is revealed on a loss, and a win shows attempts used. If you change any of those in your code, update the article to match.

The following pseudocode depicts the program flow:

CONSTANTS
    LOWER_BOUND   = 1
    UPPER_BOUND   = 100
    ATTEMPT_LIMIT = 10
    Outcomes: INVALID, CORRECT, TOO_HIGH, TOO_LOW

FUNCTION parse_guess(raw_text)            # was CVI
    text = raw_text with spaces trimmed from both ends
    IF text is empty                      RETURN INVALID
    IF text is not a whole number         RETURN INVALID
        (an integer, or a decimal with zero fraction like 42.0)
    value = text as an integer
    IF value < LOWER_BOUND OR value > UPPER_BOUND   RETURN INVALID
    RETURN value                          # returns the number itself, no printing

FUNCTION compare_guess(guess, secret)     # was CIS
    IF guess == secret    RETURN CORRECT
    IF guess > secret     RETURN TOO_HIGH
    RETURN TOO_LOW

FUNCTION play_game()                      # was FR
    secret        = random whole number from LOWER_BOUND to UPPER_BOUND, inclusive
    attempts_used = 0
    won           = FALSE

    WHILE attempts_used < ATTEMPT_LIMIT AND NOT won
        raw_text = ask the player for a guess
        attempts_used = attempts_used + 1          # once per turn, valid or not
        guess = parse_guess(raw_text)

        IF guess is INVALID
            tell the player the allowed range and that the attempt was used
            go to the next turn
        outcome = compare_guess(guess, secret)
        IF outcome is CORRECT
            print win message with attempts_used
            won = TRUE
        ELSE
            print "too high" or "too low"
            print attempts remaining

    IF NOT won
        print game over and reveal the secret

MAIN
    TRY
        play_game()
    ON Ctrl+C or Ctrl+D
        print a goodbye message and exit
		
# Program code link
Refer to the following link for the Python program code for the game:

https://github.com/syedkingbook/syedkingbook.github.io/blob/main/Games_Daily/Number_Guessing_01.py