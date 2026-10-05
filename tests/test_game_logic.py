from logic_utils import check_guess, hint_message

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"

def test_reported_bug_guess_10_secret_29():
    # Regression: guess 10 with secret 29 should be "Too Low" and say Go HIGHER
    result = check_guess(10, 29)
    assert result == "Too Low"
    assert "HIGHER" in hint_message(result)

def test_numeric_string_secret_compares_as_number():
    # Regression: as text, "9" > "29", but 9 is less than 29
    assert check_guess(9, "29") == "Too Low"

def test_numeric_string_secret_win():
    # Regression: a numeric-string secret still counts as a win
    assert check_guess(29, "29") == "Win"

def test_too_high_message_says_lower():
    # Regression: messages were swapped
    assert "LOWER" in hint_message("Too High")

def test_too_low_message_says_higher():
    # Regression: messages were swapped
    assert "HIGHER" in hint_message("Too Low")

def test_win_message():
    assert hint_message("Win") == "🎉 Correct!"
