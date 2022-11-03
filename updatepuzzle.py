import requests
import chess.pgn
import io
from pathlib import Path
from datetime import datetime

board = None

def main():
    #endpoint_url = "https://lichess.org/api/puzzle/daily"
    # endpoint_url = "https://lichess.org/api/puzzle/61uUR"
    endpoint_url = "https://lichess.org/api/puzzle/K69di"
    
    response = requests.get(url=endpoint_url)
    data = response.json()
    pgn = data['game']['pgn']
    sln = data['puzzle']['solution']
    rating = data['puzzle']['rating']
    
    # print('This is the pgn'+ pgn)
    # print('This is the rating'+ str(rating))
    # print('This is the solution' + str(sln))
    

    game = chess.pgn.read_game(io.StringIO(pgn))
    board = game.board()
    
    updateReadMe(pgn)

def get_side_to_play(pgn):
    game = chess.pgn.read_game(io.StringIO(pgn))
    board = game.board()
    for move in game.mainline_moves():
        board.push(move)
    return ["White to move" if board.turn else "Black to move",board]

def updateReadMe(pgn):
    side_to_play,board =get_side_to_play(pgn)
    
    print("This is the side to play " + side_to_play)
    board_img = chess.svg.board(board)
    
    with open('defaultImage.svg','w') as image_file:
        image_file.write(board_img)
        image_file.close()

    with open('README.md','r') as read_me_file:
        read_me_file_text =read_me_file.read()
        updatedReadME =read_me_file_text[:606]+side_to_play+'/n'+ str(datetime.now())+ read_me_file_text[619:] 
        read_me_file.close()
    
    with open('README.md', "w+") as f:
        f.write(updatedReadME)
        f.close()
        
    
if __name__ == '__main__':
    main()
