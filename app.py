import requests
import chess.pgn
import io
from pathlib import Path

board = None

def main():
    endpoint_url = "https://lichess.org/api/puzzle/daily"
    response = requests.get(url=endpoint_url)
    data = response.json()
    pgn = data['game']['pgn']
    sln = data['puzzle']['solution']
    rating = data['puzzle']['rating']

    game = chess.pgn.read_game(io.StringIO(pgn))
    board = game.board()
    
if __name__ == '__main__':
    main()
