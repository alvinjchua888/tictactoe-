"""
Flask web application for Tic-Tac-Toe game.

This module provides a web interface for playing Tic-Tac-Toe using Flask.
The application maintains game state in user sessions and provides RESTful
API endpoints for game interactions.

Routes:
    GET /: Serves the main game interface
    GET /get_state: Returns current game state as JSON
    POST /move: Makes a move at specified coordinates
    POST /reset: Resets the game to initial state
"""

from flask import Flask, render_template, request, jsonify, session
from game import TicTacToe
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Generate a random secret key for session security

def get_game():
    """
    Retrieve the current game instance from the session.
    
    Creates a new game if none exists in the session.
    
    Returns:
        TicTacToe: Current game instance
    """
    if 'game' not in session:
        session['game'] = TicTacToe().to_dict()
    return TicTacToe.from_dict(session['game'])

def save_game(game):
    """
    Save the current game state to the session.
    
    Args:
        game (TicTacToe): Game instance to save
    """
    session['game'] = game.to_dict()

@app.route('/')
def index():
    """
    Serve the main game interface.
    
    Returns:
        str: Rendered HTML template for the game interface
    """
    return render_template('index.html')

@app.route('/get_state', methods=['GET'])
def get_state():
    """
    Get the current game state.
    
    Returns:
        Response: JSON response containing the current game state
        
    Example response:
        {
            "board": [["X", "", "O"], ["", "X", ""], ["", "", ""]],
            "current": "O",
            "winner": null
        }
    """
    game = get_game()
    return jsonify(game.to_dict())

@app.route('/move', methods=['POST'])
def move():
    """
    Make a move in the game.
    
    Expects JSON payload with 'row' and 'col' fields specifying the move position.
    
    Returns:
        Response: JSON response with success status and updated game state
        
    Example request:
        {"row": 1, "col": 2}
        
    Example response:
        {
            "success": true,
            "state": {
                "board": [["X", "", "O"], ["", "X", ""], ["", "", ""]],
                "current": "O",
                "winner": null
            }
        }
    """
    data = request.get_json()
    row = data.get('row')
    col = data.get('col')
    
    game = get_game()
    result = game.make_move(row, col)
    save_game(game)
    
    return jsonify({'success': result, 'state': game.to_dict()})

@app.route('/reset', methods=['POST'])
def reset():
    """
    Reset the game to its initial state.
    
    Creates a new game and saves it to the session.
    
    Returns:
        Response: JSON response confirming the reset operation
        
    Example response:
        {"success": true}
    """
    session['game'] = TicTacToe().to_dict()
    return jsonify({'success': True})

if __name__ == '__main__':
    app.run(debug=True)