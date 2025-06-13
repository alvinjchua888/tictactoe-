from flask import Flask, render_template, request, jsonify, session
from game import TicTacToe
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

def get_game():
    if 'game' not in session:
        session['game'] = TicTacToe().to_dict()
    return TicTacToe.from_dict(session['game'])

def save_game(game):
    session['game'] = game.to_dict()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_state', methods=['GET'])
def get_state():
    game = get_game()
    return jsonify(game.to_dict())

@app.route('/move', methods=['POST'])
def move():
    data = request.get_json()
    row = data.get('row')
    col = data.get('col')
    game = get_game()
    result = game.make_move(row, col)
    save_game(game)
    return jsonify({'success': result, 'state': game.to_dict()})

@app.route('/reset', methods=['POST'])
def reset():
    session['game'] = TicTacToe().to_dict()
    return jsonify({'success': True})

if __name__ == '__main__':
    app.run(debug=True)