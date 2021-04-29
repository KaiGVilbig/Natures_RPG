# file: Moves.py
# author: colin seifer
# description: stores and returns moves

import json
import os

class Moves:
    def __init__(self):
        self.ImportJson()

    # gets data from moves json by relative path
    def ImportJson(self):
        # open file for reading
        json_file = open("backend/Battle/moves.json")
        # parse into a dict called moves
        self.moves = json.load(json_file)
        # close file
        json_file.close()

    # returns data for a specific move
    def RetMove(self, name):
        for move in self.moves["moves"]:
            if(move["name"] == name):
                return move
        # return none if no move matches name
        return None