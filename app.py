import requests

endpoint_url = "https://lichess.org/api/puzzle/daily"

response = requests.get(url=endpoint_url)

data = response.json()

side_to_play = ''
pgn = data['game']['pgn']
sln = data['puzzle']['solution']
rating = data['puzzle']['rating']


print(side_to_play)
print(pgn)
print(sln)
print(rating)


def get_side_to_play():

    return None


def get_picture():
    return None


def check_sln():
    return None
