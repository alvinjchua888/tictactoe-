# Tic-Tac-Toe Web Application

A simple, interactive Tic-Tac-Toe game built with Flask and vanilla JavaScript.

## Features

- **Web-based interface**: Play directly in your browser
- **Real-time gameplay**: Immediate feedback and game state updates
- **Session persistence**: Game state is maintained across page refreshes
- **Reset functionality**: Start a new game at any time
- **Responsive design**: Clean, centered layout that works on various screen sizes

## Technology Stack

- **Backend**: Python 3.x with Flask web framework
- **Frontend**: HTML5, CSS3, and vanilla JavaScript
- **Session Management**: Flask sessions for game state persistence
- **Testing**: Python unittest framework

## Project Structure

```
tictactoe-/
├── app.py              # Flask web application and routes
├── game.py             # Tic-Tac-Toe game logic
├── test_game.py        # Unit tests for game logic
├── templates/
│   └── index.html      # HTML template with embedded JavaScript
├── static/
│   └── style.css       # CSS styling
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/alvinjchua888/tictactoe-.git
   cd tictactoe-
   ```

2. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```bash
   python app.py
   ```

4. **Open your browser** and navigate to:
   ```
   http://localhost:5000
   ```

## How to Play

1. The game starts with player 'X' making the first move
2. Click on any empty cell to place your mark (X or O)
3. Players alternate turns automatically
4. The first player to get 3 marks in a row (horizontally, vertically, or diagonally) wins
5. If all 9 cells are filled without a winner, the game ends in a draw
6. Click the "Reset" button to start a new game

## Running Tests

Execute the unit tests to verify the game logic:

```bash
python test_game.py
```

Or use Python's unittest module:

```bash
python -m unittest test_game.py
```

## API Endpoints

The application provides the following REST API endpoints:

- `GET /` - Serves the main game interface
- `GET /get_state` - Returns the current game state as JSON
- `POST /move` - Makes a move at the specified row and column
- `POST /reset` - Resets the game to initial state

## Development

### Game Logic (`game.py`)

The `TicTacToe` class handles all game logic including:
- Board state management
- Move validation
- Win condition checking
- Draw detection
- Game state serialization

### Web Interface (`app.py`)

Flask application that provides:
- Session-based game state persistence
- RESTful API for game interactions
- Template rendering for the web interface

### Testing (`test_game.py`)

Comprehensive unit tests covering:
- Initial game state validation
- Move execution and player switching
- Invalid move handling
- Win condition detection
- Draw game scenarios

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add or update tests as needed
5. Ensure all tests pass
6. Submit a pull request

## License

This project is open source and available under the MIT License.