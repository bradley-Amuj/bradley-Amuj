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
    
    updateReadMe(pgn)


# print(side_to_play)
# print(pgn)
# print(sln)
# print(rating)


def get_side_to_play(pgn):
    game = chess.pgn.read_game(io.StringIO(pgn))
    board = game.board()
    for move in game.mainline_moves():
        board.push(move)
    return ["White to move" if board.turn else "Black to move",board]

def updateReadMe(pgn):
    side_to_play,board =get_side_to_play(pgn)
    board_img = chess.svg.board(board)
    
    outputfile = open('defaultImage.svg', "w")
    outputfile.write(board_img)
    outputfile.close()
    
    readme = Path('ReadME.md').read_text()
    updatedReadME =readme[:606]+side_to_play+'/n'+ readme[619:]
    
    with open('README.md', "w+") as f:
        f.write(updatedReadME)
    


def check_sln():
    return None


if __name__ == '__main__':
    main()
