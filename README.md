# 🎮 Number Quest

A command-line number-guessing game with increasing difficulty, written in pure Python. Win a round and the next one gets harder: a bigger range and fewer attempts. Lose and you start over from level 1.

![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Dependencies](https://img.shields.io/badge/dependencies-none-brightgreen)

## Features

- Progressive difficulty: the range grows and attempts shrink as you level up
- "Too high / too low" hints after every guess
- Input validation: invalid or out-of-range guesses never cost an attempt
- Quit anytime with `q` (or Ctrl+C)
- Clean, testable code: game logic is separated from input/output
- Unit tests with `pytest`

## Demo

```text
🎮 Welcome to Number Quest!
Guess the secret number. You have limited attempts per round.

--- Round 1 ---
Range: 1 to 15
Attempts: 8
Enter your guess (or type 'q' to quit): 8
⬆️ Too low! Attempts left: 7
Enter your guess (or type 'q' to quit): 12
⬇️ Too high! Attempts left: 6
Enter your guess (or type 'q' to quit): 10
✅ Correct! You win this round!
--- Round 2 ---
Range: 1 to 20
Attempts: 7
```

## Getting Started

### Requirements

- Python 3.8 or newer (standard library only, no `pip install` needed)

### Run

```bash
git clone https://github.com/<your-username>/number-quest.git
cd number-quest
python main.py
```

## How Difficulty Works

| Level | Range  | Attempts |
| ----- | ------ | -------- |
| 1     | 1–15   | 8        |
| 2     | 1–20   | 7        |
| 4     | 1–30   | 6        |
| 10    | 1–60   | 3        |

Formula: `range = 1 … (10 + level × 5)` and `attempts = max(3, 8 − level // 2)`.
Tip: guess the middle of the range each time (binary search) to get the furthest.

## Running the Tests

```bash
pip install pytest
pytest
```

## Project Structure

```text
number-quest/
├── main.py                   # Game logic and CLI loop
├── conftest.py               # Lets pytest import main.py
├── tests/
│   └── test_number_quest.py  # Unit tests
├── README.md
├── LICENSE
└── .gitignore
```

## Roadmap

- [ ] Track and display the best level reached
- [ ] Difficulty modes (easy / normal / hard)
- [ ] Hot/cold hints based on distance
- [ ] Persist high scores to a JSON file

## Contributing

Issues and pull requests are welcome. For major changes, please open an issue first to discuss what you'd like to change.

## License

Distributed under the MIT License. See `LICENSE` for details.

## Author

**Mosyafa** — Computer Science student (AI/ML & Cybersecurity)
GitHub: [@Mostafa112-alt](https://github.com/Mostafa112-alt)
