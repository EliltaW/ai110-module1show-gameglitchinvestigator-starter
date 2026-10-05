# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable.

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: _"How do I keep a variable from resetting in Streamlit when I click a button?"_
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [x] Describe the game's purpose.
- [x] Detail which bugs you found.
- [x] Explain what fixes you applied.

**Game purpose:** Glitchy Guesser is a Streamlit number guessing game. The player picks a difficulty, then tries to guess a secret number within a limited number of attempts. After each guess, a hint says whether to go higher or lower.

**Bugs found:**

1. **Wrong hints.** Guessing 10 when the secret was 29 said "Go LOWER" instead of "Go HIGHER", because the hint messages were swapped.
2. **New Game did not fully reset.** After a loss, New Game changed the secret and attempts but kept the old status and guess history, so the next guess was blocked with "Game over".
3. **Text comparison bug.** On even attempts, the secret was turned into text before comparing. Claude reproduced this in Python: `check_guess(9, "29")` returned "Too High", because the text "9" sorts after "29".

**Fixes applied:**

1. Moved `check_guess` into `logic_utils.py`, where it returns one outcome ("Win", "Too High" or "Too Low"). A new `hint_message` helper turns that outcome into the right message ("Too High" → "Go LOWER", "Too Low" → "Go HIGHER").
2. Added `start_new_round` in `app.py`. New Game and first load both use it to reset status, attempts, score and history, and to pick the secret from the selected difficulty's range. The "Guess a number between..." message now shows that range too.
3. The app no longer turns the secret into text, and `check_guess` converts both values to numbers before comparing.

**How to run:**

- App: `python -m streamlit run app.py`
- Tests: `python -m pytest -q` (from the project folder)

**Testing:** Running `python -m pytest -q` gave 10 passed. The tests cover the hints, the number comparison, and a Streamlit AppTest that checks New Game resets the round after a loss.

**Browser checks I performed:** On Easy, clicking New Game cleared the history and score and restored the attempts. The hint pointed in the correct direction, I was able to win, and guesses were accepted after another New Game.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. Start the app with `python -m streamlit run app.py` and open it in the browser.
2. In the sidebar, choose **Easy**. The sidebar shows the number range and attempts allowed for that difficulty.
3. Click **New Game 🔁**. The guess history and score are cleared, and the attempts are restored.
4. Enter a guess and click **Submit Guess 🚀**. The hint says "Go HIGHER" if the guess is too low and "Go LOWER" if it is too high.
5. Keep guessing until you find the secret number to win the game.
6. Click **New Game 🔁** again. The new round accepts guesses instead of showing "Game over".

**Screenshot** _(optional)_: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
$ python -m pytest -q
.......... [100%]
10 passed in 1.70s
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
