from pathlib import Path

from streamlit.testing.v1 import AppTest

APP_PATH = str(Path(__file__).resolve().parent.parent / "app.py")


def test_new_game_after_loss_resets_round():
    # Regression: New Game kept status "lost" and old history, so the next
    # guess was blocked with "Game over".
    at = AppTest.from_file(APP_PATH).run()
    at.sidebar.selectbox[0].set_value("Easy").run()

    at.session_state.status = "lost"
    at.session_state.attempts = 6
    at.session_state.history = [5, 10, 15]
    at.session_state.score = -30
    at.run()
    assert any("Game over" in e.value for e in at.error)

    at.button[1].click().run()  # New Game

    assert at.session_state.status == "playing"
    assert at.session_state.attempts == 0
    assert at.session_state.history == []
    assert at.session_state.score == 0
    assert 1 <= at.session_state.secret <= 20
    assert not any("Game over" in e.value for e in at.error)
    assert "between 1 and 20" in at.info[0].value
