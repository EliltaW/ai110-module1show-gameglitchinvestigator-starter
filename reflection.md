# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

When I first ran the game, it opened in Streamlit with Normal difficulty, a range of 1–100, and eight allowed attempts. I noticed that submitting 10 when the secret was 29 gave the hint “Go LOWER,” although it should have said “Go HIGHER.” After the game ended, clicking New Game changed the secret and reset the attempts, but kept the previous guesses and still blocked submissions with a “Game over” message. Claude also reported reproducing a separate comparison bug in Python: the function treated 9 as higher than the text value "29".

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input                                    | Expected Behavior              | Actual Behavior                 | Console Output / Error                    |
| ---------------------------------------- | ------------------------------ | ------------------------------- | ----------------------------------------- |
| Guess 10; secret 29                      | Go HIGHER                      | Go LOWER                        | Wrong hint shown                          |
| New Game after loss; guess new secret 48 | Clear history and accept guess | Old history kept; guess blocked | "Game over"                               |
| Claude tested check_guess(9, "29")       | Too Low                        | Too High                        | Reproduced by Claude; regression test now passes. |

---

## 2. How did you use AI as a teammate?

I used Claude in VS Code, and ChatGPT for guidance and review. Claude correctly identified that the hint messages were swapped and that New Game did not fully reset the game, and I checked in the game that the hints were right, that I could win, and that a fresh game accepted guesses. One suggestion I did not accept as written was Claude's idea to make check_guess return two values and change the existing tests. With ChatGPT's guidance, I asked Claude to keep check_guess returning a single string and to keep the existing tests, and to add a separate hint_message helper instead. This preserved the existing test contract and kept comparison separate from hint text; I verified it by running the tests, which all passed.

---

## 3. Debugging and testing your fixes

I decided a bug was fixed when I could check the correct behavior in the browser myself. On Easy, I clicked New Game and saw that the history and score cleared, the attempts were restored, the hint was correct, I could win, and guesses were accepted after another New Game. Claude added regression tests, including a Streamlit AppTest that checks the New Game reset. Claude reported that the reset test fails against the old reset code. I then ran python -m pytest -q myself, and all 10 tests passed in 1.70 seconds.

---

## 4. What did you learn about Streamlit and state?

Streamlit reruns the whole script from top to bottom every time a user interacts with the app, like clicking a button. That means normal variables start over on each rerun. Session state is how values like the secret, attempts, and history are kept between reruns. Our old New Game handler changed the secret and attempts but left status and history unchanged, so the game still thought it was over. Explicitly resetting those values made a fresh round work.

---

## 5. Looking ahead: your developer habits

A habit I want to reuse is reproducing a bug first, reviewing the AI's diff, and verifying the fix before committing. Next time, I would explain the expected behavior and the existing test contract more clearly before asking AI to change code. This project showed me that AI-generated code needs review and testing, even when it looks convincing.
