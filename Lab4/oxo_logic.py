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
    
    def _generateMove(self):
        options = [i for i in range(len(self.list)) if self.list[i] == " "]
        if options:
            return random.choice(options)
        else: return -1
    
    
    def _isWinningMove(self, list):
        wins = ((0,1,2), (3,4,5), (6,7,8),
                (0,3,6), (1,4,7), (2,5,8),
                (0,4,8), (2,4,6))

        for a,b,c in wins:
            chars = list[a] + list[b] + list[c]
            if chars == 'XXX' or chars == 'OOO':
                return True
        return False

    def userMove(self, cell):
        if self.list[cell] != ' ':
            raise ValueError('Invalid cell')
        else:
            self.list[cell] = 'X'
        if _isWinningMove(self.list):
            return 'X'
        else:
            return ""

    def computerMove(self, cell):
        cell = _generateMove(self.list)
        if cell == -1:
            return 'D'
        self.list[cell] = 'O'
        if _isWinningMove(self.list):
            return 'O'
        else:
            return ""

    def test(self):
        result = ""
        self.list = newGame()
        while not result:
            print(self.list)
            try:
                result = userMove(self.list, _generateMove(self.list))
            except ValueError:
                print("Oops, that shouldn't happen")
            if not result:
                result = computerMove(self.list)
                
            if not result: continue
            elif result == 'D':
                print("Its a draw")
            else:
                print("Winner is:", result)
            print(self.list)

if __name__ == "__main__":
    game_obj = Game()
    game_obj.test()


            
