def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")


# FIX: Moved from app.py with Claude's help. Swapped hint messages made guess 10 vs
# secret 29 say "Go LOWER". Separately, the secret was turned into text on even
# attempts, which broke the comparison. I chose to keep a single outcome string
# (as the tests expect), and Claude ran pytest.
def check_guess(guess, secret):
    """
    Compare guess to secret and return the outcome.

    outcome is one of: "Win", "Too High", "Too Low"
    """
    # Normalize numeric strings like "29" so we never compare text ("9" > "29").
    guess = int(guess)
    secret = int(secret)

    if guess == secret:
        return "Win"
    if guess > secret:
        return "Too High"
    return "Too Low"


def hint_message(outcome: str):
    """Return the player-facing message for an outcome from check_guess."""
    if outcome == "Win":
        return "🎉 Correct!"
    if outcome == "Too High":
        return "📉 Go LOWER!"
    return "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")
