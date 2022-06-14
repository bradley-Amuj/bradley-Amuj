
import requests
import chess.pgn
import io


def main():
    endpoint_url = "https://lichess.org/api/puzzle/daily"
    response = requests.get(url=endpoint_url)
    data = response.json()

    side_to_play = ''
    pgn = data['game']['pgn']
    sln = data['puzzle']['solution']
    rating = data['puzzle']['rating']

    game = chess.pgn.read_game(io.StringIO(pgn))
    board = game.board()

    print(get_side_to_play(pgn))


# for move in pgn.split():
#     print(move)


# print(side_to_play)
# print(pgn)
# print(sln)
# print(rating)


def get_side_to_play(pgn):
    game = chess.pgn.read_game(io.StringIO(pgn))
    board = game.board()

    for move in game.mainline_moves():
        board.push(move)

    return "White to move" if board.turn else "Black to move"


def get_picture():
    return None


def check_sln():
    return None


if __name__ == '__main__':
    main()
