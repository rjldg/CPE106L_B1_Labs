import os, random
import oxo_data

class Game:
    def __init__(self) -> None:
        self.list = self.newGame()
    
    def newGame(self):
        return list (" " * 9)
    
    def saveGame(self):
        oxo_data.saveGame(self.list)
    
    def restoreGame(self, list):
        try:
            list = oxo_data.restoreGame()
            if len(list) == 9:
                return list
            else: return self.newGame()
        except IOError:
            return self.newGame