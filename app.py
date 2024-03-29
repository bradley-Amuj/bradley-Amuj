import requests
import chess.pgn
import io
import os 

board = None

def main():
    #endpoint_url = "https://lichess.org/api/puzzle/daily"
    endpoint_url = "https://lichess.org/api/puzzle/Uk3YD"
    
    response = requests.get(url=endpoint_url)
    data = response.json()
    pgn = data['game']['pgn']
    sln = data['puzzle']['solution']
    rating = data['puzzle']['rating']
    
    input_sln = os.environ['INPUT_SLN']
    checkSln(input_sln)
 
def checkSln(sln):
    print("This is the entered  solution " + str(sln))
    
    

    
if __name__ == '__main__':
    main()
