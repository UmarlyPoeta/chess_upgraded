````markdown
# Chess Upgraded

A Python-based chess game that allows two players to compete in a terminal environment. The game follows standard chess rules and includes features such as move validation, piece capture, and a visual display of the chessboard using Unicode symbols.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Game Rules](#game-rules)
- [Contributing](#contributing)
- [License](#license)

## Features

- Fully playable chess game for two players.
- Supports all chess pieces (King, Queen, Rook, Bishop, Knight, Pawn) with their unique moves.
- Simple user interface with a terminal-based board display using Unicode symbols.
- Input validation for moves.
- Turn-based play between black and white pieces.
- Piece capture mechanism.

## Installation

To play Chess Upgraded, clone this repository and ensure you have Python 3.x installed.

1. Clone the repository:

```bash
git clone https://github.com/UmarlyPoeta/chess_upgraded.git
```
````

2. Navigate to the project directory:

```bash
cd chess_upgraded
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt  # (If any dependencies are listed)
```

## Usage

To start the game, run the `main.py` file:

```bash
cd src
```

```bash
python main.py
```

Players take turns by entering their moves in standard algebraic notation (e.g., `e2 e4` to move a piece from e2 to e4).

## Project Structure

```
chess_upgraded/
│
├── src/
│   ├── __init__.py
│   ├── main.py          # The entry point for the game
│   ├── game_model.py    # Contains the main Game class and logic
│   └── utils/
│       ├── chess_board.py  # Handles chessboard initialization and display
│       ├── pieces.py       # Contains the definitions of all chess pieces
│       └── valid_moves.py  # Implements move validation for each piece
│
| #####################################
|
└── README.md            # This file
```

## Game Rules

- **Pawn:** Moves forward one square, two squares on its first move, captures diagonally.
- **Rook:** Moves horizontally or vertically.
- **Knight:** Moves in an "L" shape: two squares in one direction and one square perpendicular.
- **Bishop:** Moves diagonally.
- **Queen:** Moves any number of squares horizontally, vertically, or diagonally.
- **King:** Moves one square in any direction.

Players alternate turns between black and white pieces.

## Contributing

Contributions are welcome! Please fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```

```
