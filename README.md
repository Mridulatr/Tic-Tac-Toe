# Tic-Tac-Toe Game in Python

## Description
This is a Python implementation of the classic Tic-Tac-Toe game. Two players take turns marking the spaces in a 3x3 grid with their respective symbols (X and O). The first player to get three of their symbols in a row (horizontally, vertically, or diagonally) wins the game.

---

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)

---

## Installation

### Clone the Repository
```bash
git clone https://github.com/yourusername/tic-tac-toe-ai.git
cd tic-tac-toe-ai

```





## Install Dependencies

This project only uses Python's standard library. Make sure you have Python 3.7 or above installed.

## Usage

Run the game from the terminal:

python tictactoe.py <player1_type> <player2_type>


Where <player1_type> and <player2_type> can be:

human_player – Play as a human

random_ai – AI picks a move randomly

minimax_ai – AI uses the Minimax algorithm

finds_own_winning_move_ai – AI tries to make a winning move

finds_all_winning_moves_ai – AI tries to win and block losing moves

Example:

python tictactoe.py human_player minimax_ai

## Features

Multiple AI Players: Play against different AI strategies or a human

Command-Line Interface (CLI): Simple and interactive gameplay

Custom AI Implementations: Includes random AI, Minimax AI, and strategic AI algorithms

Benchmarking: Run repeated matches between AI players to analyze win/draw rates (benchmark.py)

## Contributing

Contributions are welcome! If you have suggestions for improvements or bug fixes, feel free to:

Fork the project
Create a new branch (git checkout -b feature/AmazingFeature)
Make your changes
Commit your changes (git commit -m 'Add some AmazingFeature')
Push to the branch (git push origin feature/AmazingFeature)
Open a Pull Request project, as well as detailing how to contribute effectively.
